<!-- 填空题分析 用在数据分析页面中 -->
<template>
  <div class="ACompletion">
    <van-tabs
        v-model="active"
        swipeable
    >
      <van-tab title="详细信息">
        <ChartsTable :options="answers.slice((currentPage-1)*pageSize,currentPage*pageSize)"
                     :totalSubmit="totalSubmit"></ChartsTable>
        <el-pagination
            style="text-align: center"
            layout="prev, pager, next"
            :total="answers.length"
            :page-size="pageSize"
            hide-on-single-page
            @current-change="page=>{this.currentPage=page}"
        >
        </el-pagination>

      </van-tab>
      <van-tab title="词云图">
        <ChartsWordCloud :id="'WordCloud'+index" :chartData="answers"></ChartsWordCloud>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import ChartsTable from './charts/ChartsTable'
import ChartsWordCloud from './charts/ChartsWordCloud'

export default {
  name: "ACompletion",
  components: {
    ChartsWordCloud,
    ChartsTable
  },
  props: {
    answers: Array,
    title: String,
    index: Number,
    totalSubmit: Number
  },
  data() {
    return {
      show: false,
      active: 0,
      currentPage: 1,
      pageSize: 10,
    }
  },
}
</script>

<style scoped lang="less">
.ACompletion {
  .van-button {
    margin-right: 10px;
  }

  p {
    font-size: 0.8rem;
  }
}

.completionTable {
  padding: 5px;
  width: 90vw;
}

/deep/.el-pagination .el-pager li.active {
  color: @theme-color;
}
</style>