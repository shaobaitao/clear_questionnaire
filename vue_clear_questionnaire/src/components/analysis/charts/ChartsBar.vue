<!-- Echarts柱形图 用在数据分析页面中 -->
<template>
  <div class="ChartsBar" :id="id" :style="styles"></div>
</template>

<script>
const echarts = require('echarts/lib/echarts');
require('echarts/lib/component/title');
require('echarts/lib/component/tooltip');
require('echarts/lib/component/toolbox');
require('echarts/lib/component/legend');
require('echarts/lib/component/grid');
require('echarts/lib/chart/bar');

export default {
  name: "ChartsBar",
  props: {
    id: {
      type: String,
      default: "PieChart",
    },
    height: {
      type: String,
      default: '300px'
    },
    width: {
      type: String,
      default: '100%'
    },
    chartData: Array,
    title: String
  },
  data() {
    return {
      styles: {
        height: this.height,
        width: this.width,
      },
    };
  },
  methods: {
    seriesData() {
      let data = []
      for (const index in this.chartData) {
        let serve = {
          name: '',
          type: 'bar',
          stack: "total",
          label: {
            show: true, //开启显示
            position: 'top', //在上方显示
          },
          data: [],
        }
        serve.name = this.chartData[index].title
        serve.data.length = this.chartData.length
        serve.data[index] = this.chartData[index].count
        data.push(serve)
      }
      return data
    },
    draw() {
      const chartDom = document.getElementById(this.id);
      const myChart = echarts.init(chartDom);
      const option = {
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        xAxis: {
          type: 'category',
          data: this.chartData.map(item => {
            return item.title;
          })
        },
        yAxis: {
          type: 'value'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a}：{c}'
        },
        legend: {
          type: 'scroll',
          bottom: 5,
          data: this.chartData.map(item => {
            return item.title;
          })
        },
        series: this.seriesData()
      };
      option && myChart.setOption(option);
      window.addEventListener("resize", () => {
        myChart.resize();
      });
    },
  },
  mounted() {
    this.draw();
  }
}
</script>

<style scoped>

</style>