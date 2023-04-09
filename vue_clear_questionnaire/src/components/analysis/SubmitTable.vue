<!-- 提交表格 用在数据分析页面中 -->
<template>
  <div class="SubmitTable">
    <el-table
        :data="tableData"
        :height="tableMaxHeight"
        :max-height="tableMaxHeight"
        stripe
    >
      <el-table-column
          fixed
          prop="index"
          align="center"
          label="序号"
          width="50">
      </el-table-column>
      <el-table-column
          prop="submit_time"
          label="提交时间"
          align="center"
          width="200px"
      >
      </el-table-column>
      <el-table-column
          prop="duration"
          label="填卷用时"
          align="center"
          width="100px"
      >
      </el-table-column>
      <el-table-column
          prop="ip"
          label="提交IP"
          align="center"
          width="150px"
      >
      </el-table-column>
      <!--      <el-table-column-->
      <!--          prop="location"-->
      <!--          label="提交地点"-->
      <!--          align="center"-->
      <!--          width="150px"-->
      <!--      >-->
      <!--      </el-table-column>-->
      <el-table-column
          prop="browser"
          label="浏览器"
          align="center"
          width="80px"
      >
      </el-table-column>
      <el-table-column
          prop="os"
          label="操作系统"
          align="center"
          width="80px"
      >
      </el-table-column>
      <el-table-column
          fixed="right"
          label="操作"
          align="center"
          width="50">
        <template slot-scope="scope">
          <el-button
              @click="getDetail(scope.$index, scope.row.id)"
              type="text"
              size="small">
            详情
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <van-pagination
        v-model="currentPage"
        :page-count="pageCount"
        @change="getSubmits"
    >
      <template #prev-text>
        <van-icon name="arrow-left"/>
      </template>
      <template #next-text>
        <van-icon name="arrow"/>
      </template>
      <template #page="{ text }">{{ text }}</template>
    </van-pagination>

    <van-popup
        v-model="showPopup"
        closeable
        @closed="submitSubmitData={}"
    >
      <SubmitDetail
          :submitQuestionData="submitQuestionData"
          :submitSubmitData="submitSubmitData"
          :submitID="currentSubmitID"
          @refresh="getSubmits()"
      ></SubmitDetail>
    </van-popup>

  </div>
</template>

<script>
import api from "../../axios/api";
import uaParser from 'ua-parser-js'
import SubmitDetail from "./SubmitDetail";

export default {
  name: "SubmitTable",
  components: {
    SubmitDetail,
  },
  data() {
    return {
      tableData: [],
      currentPage: 1,
      pageCount: 0,
      tableMaxHeight: window.innerHeight - 136,
      currentSubmitID: -1,
      showPopup: false,
      submitQuestionData: {},
      submitSubmitData: {}
    }
  },
  methods: {
    getDetail(index, id) {
      this.showPopup = true
      this.currentSubmitID = id
      this.getSubmitDetail(id)
    },
    getSubmitDetail(submitID) {
      api.questionnaire.getSubmitDetail({
        submitID: submitID
      }).then(submitRes => {

        api.questionnaire.getQuestionsPrivate({
          projectID: this.$route.params.id
        }).then(questionsRes => {
          submitRes.data.data.list.forEach((item, index) => {
            questionsRes.data.data.questions[index].answerID = item.answerID
            questionsRes.data.data.questions[index].answerText = item.answerText
          })
          this.submitQuestionData = questionsRes.data.data
          this.submitSubmitData = submitRes.data.data
        })
      })
    },
    getSubmits() {
      api.questionnaire.getSubmits({
        projectID: this.$route.params.id,
        pageNumber: this.currentPage
      }).then(response => {
        const {pageCount, submitList} = response.data.data;
        this.tableData = this.tableDataProcessing(submitList)
        this.pageCount = pageCount
      })
    },
    tableDataProcessing(data) {
      data.map(item => {
        item.browser = uaParser(item.os).browser.name
        item.os = uaParser(item.os).os.name
        item.submit_time = new Date(parseInt(item.submit_time) * 1000).toLocaleString('chinese', {hour12: false})
        item.duration = `${Math.floor(Math.floor(item.duration / 1000) / 60)}分${Math.floor(item.duration / 1000) % 60}秒`
        // item.location = this.getIPLocation(item.ip, item.index - (this.currentPage - 1) * 10 - 1)
      })
      return data
    },
    // getIPLocation(ip, index) {
    //   //http://opendata.baidu.com/api.php?query=182.97.166.162&co=&resource_id=6006&oe=utf8
    //   axios.get(`api.php?query=${ip}&co=&resource_id=6006&oe=utf8`).then(
    //       response => {
    //         this.tableData[index].location = response.data.data[0].location.split(" ")[0]
    //       }
    //   )
    // }
  },
  mounted() {
    this.getSubmits()
    window.addEventListener("resize", () => {
      this.tableMaxHeight = window.innerHeight - 46 - 40 - 50
    });
  }
}
</script>

<style scoped>
.el-button{
  color: #6246ea;
}
</style>