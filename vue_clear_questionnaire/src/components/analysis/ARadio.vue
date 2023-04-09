<!-- 单选何多选题分析 用在数据分析页面中 -->
<template>
  <div class="ARadio">
    <van-tabs
        v-model="active"
        swipeable
    >
      <van-tab title="表格">
        <ChartsTable :options="answers" :totalSubmit="totalSubmit"></ChartsTable>
      </van-tab>
      <van-tab title="饼状图">
        <ChartsPie :id="'ChartsPie'+index" :chartData="answers" :title="title"></ChartsPie>
      </van-tab>
      <van-tab title="柱状图">
        <ChartsBar :id="'ChartsBar'+index" :chartData="answers" :title="title"></ChartsBar>
      </van-tab>
      <van-tab title="雷达图">
        <ChartsRadar :id="'ChartsRadar'+index" :chartData="answers" :title="title"></ChartsRadar>
      </van-tab>
      <van-tab title="玫瑰图">
        <ChartsRose  :id="'ChartsRose'+index" :chartData="answers" :title="title"></ChartsRose>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import ChartsTable from './charts/ChartsTable'
import ChartsPie from './charts/ChartsPie'
import ChartsBar from './charts/ChartsBar'
import ChartsRadar from './charts/ChartsRadar'
import ChartsRose from './charts/ChartsRose'

export default {
  name: "ARadio",
  components: {
    ChartsTable,
    ChartsPie,
    ChartsBar,
    ChartsRadar,
    ChartsRose
  },
  props: {
    answers: Array,
    title: String,
    index: Number,
    totalSubmit: Number
  },
  data() {
    return {
      active: 0
    };
  },
}
</script>

<style scoped>

</style>