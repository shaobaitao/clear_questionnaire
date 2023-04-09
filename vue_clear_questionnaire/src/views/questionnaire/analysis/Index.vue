<template>
  <div class="index">
    <van-sticky placeholder>
      <van-nav-bar title="数据分析" left-arrow @click-left="$router.back()"></van-nav-bar>
    </van-sticky>
    <van-loading style="margin-top: 30vh" v-show="showLoading" type="spinner" size="60px" vertical>加载中</van-loading>
    <van-empty v-if="!showLoading&&analysisData.submit===0" style="margin-top: 20vh" description="这里的数据空空如也"/>
    <div v-show="active===0&&analysisData.submit!==0" class="main">
      <van-grid :border="false" :column-num="3">
        <van-grid-item>
          <h4>今日回收</h4>
          <p>{{ analysisData.todaySubmit }}</p>
        </van-grid-item>
        <van-grid-item>
          <h4>总回收量</h4>
          <p>{{ analysisData.submit }}</p>
        </van-grid-item>
        <van-grid-item>
          <h4>平均时长</h4>
          <p>{{
              Math.floor(Math.floor(analysisData.averageDuration / 1000) / 60)
            }}分{{ Math.floor(analysisData.averageDuration / 1000) % 60 }}秒</p>
        </van-grid-item>
      </van-grid>
      <AnalysisCard
          v-for="(item,index) in analysisData.questions" :key="index"
          :index="index+1"
          :title="item.title"
          :type="item.type"
          :required="item.required"
          :questionID="item.id"
      >
        <component
            :is="componentName[item.type]"
            :index="index"
            :answers="item.answers"
            :totalSubmit="item.totalSubmit"
            :title="item.title"
        >
        </component>
      </AnalysisCard>
    </div>
    <div v-show="active===1&&analysisData.submit!==0">
      <SubmitTable></SubmitTable>
    </div>
    <div v-show="active===2&&analysisData.submit!==0">
      <van-collapse v-model="activeNames">
        <van-collapse-item title="按选项序号下载CSV文件" name="1">
          <van-button color="#6246ea" plain type="info" size="large" @click="downloadData(1)">下载数据</van-button>
          <van-cell title="按选项序号下载到Excel的效果"
                    label="如图所示，这里的1，2，3，4，5数字分别表示的是，第1个选项，第2个选项到第5个选项。如果填写者选择的是“B，不满意”这个选项，那么在数据中就会呈现“2”，代表这个选项。"
                    style="padding: 0"
          >
          </van-cell>
          <van-image
              width="100%"
              fit="contain"
              src="https://pubnew.paperol.cn/36306761/1606782745ppe5Ye.JPG"
          />
        </van-collapse-item>

        <van-collapse-item title="按选项标题下载CSV文件" name="2">
          <van-button color="#6246ea" plain type="info" size="large" @click="downloadData(2)">下载数据</van-button>
          <van-cell title="按选项文本下载到Excel的效果"
                    label="按选项文本下载的意思就是：下载到的数据，不会以数字形式呈现，而是会原样呈现选项的内容。如果填写者选择的是“B，不满意”，那么数据中同样呈现的也是“B，不满意”。不会呈现其他内容来代表这个选项。"
                    style="padding: 0"
          >
          </van-cell>
          <van-image
              width="100%"
              fit="contain"
              src="https://pubnew.paperol.cn/36306761/1606782976R54bin.JPG"
          />
        </van-collapse-item>
      </van-collapse>
    </div>

    <van-tabbar z-index="888" placeholder v-model="active">
      <van-tabbar-item icon="chart-trending-o">统计图表</van-tabbar-item>
      <van-tabbar-item icon="orders-o">收集答卷</van-tabbar-item>
      <van-tabbar-item icon="down">下载数据</van-tabbar-item>
    </van-tabbar>
  </div>

</template>

<script>
import api from "../../../axios/api";
import AnalysisCard from '../../../components/analysis/AnalysisCard'
import ARadio from "../../../components/analysis/ARadio"
import AImage from "../../../components/analysis/AImage"
import ACompletion from '../../../components/analysis/ACompletion'
import SubmitTable from '../../../components/analysis/SubmitTable'

import FileSaver from 'file-saver';
// import uaParser from 'ua-parser-js'

export default {
  name: "Index",
  components: {
    AnalysisCard,
    ARadio,
    ACompletion,
    AImage,
    SubmitTable
  },
  data() {
    return {
      active: 0,
      activeNames: [],
      componentName: {
        1: 'ARadio',
        // 2: 'ACheckBox',
        2: 'ARadio',
        3: 'ACompletion',
        7:'AImage'
      },

      analysisData: {
        submit: 0
      },
      tableData: [],
      showLoading: true
    }
  },
  methods: {
    downloadData(mode) {
      api.questionnaire.downloadData({
        projectID: this.$route.params.id,
        mode: mode
      }).then(response => {
        let json = []
        response.data.data.forEach(item => {
          let temp = {}
          item.forEach((value, index) => {
            temp[response.data.data[0][index]] = value
          })
          json.push(temp)
        })
        json.splice(0, 1)
        this.tableData = json
        const Json2csvParser = require('json2csv').Parser
        const csvData = new Json2csvParser().parse(this.tableData)
        const blob = new Blob(['\uFEFF' + csvData], {type: 'text/plain;charset=utf-8;'})
        const filename = `${this.analysisData.title}${new Date().toLocaleString('chinese', {hour12: false})}.csv`
        FileSaver.saveAs(blob, filename)
      })
    },
    getAnalysis() {
      api.questionnaire.getAnalysis({
        projectID: this.$route.params.id
      }).then(response => {
        this.showLoading = false
        this.analysisData = response.data.data
      })
    }
  },
  mounted() {
    this.getAnalysis()
  }
}
</script>

<style scoped lang="less">
.van-grid-item {
  h4, p {
    margin: 10px 0;
  }
}
</style>