<!-- Echarts饼图 用在数据分析页面中 -->
<template>
  <div class="ChartsPie" :id="id" :style="styles"></div>
</template>

<script>
const echarts = require('echarts/lib/echarts');
require('echarts/lib/component/title');
require('echarts/lib/component/tooltip');
require('echarts/lib/component/legend');
require('echarts/lib/component/toolbox');
require('echarts/lib/chart/pie');

export default {
  name: "ChartsPie",
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
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          type: 'scroll',
          bottom: 5
        },
        series: [
          {
            name: this.title,
            radius: '55%',
            type: 'pie',
            center: ['50%', '50%'],
            data: this.chartData.map(item => {
              item.name = item.title;
              item.value = item.count
              return item;
            }),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            label: {
              show: true,
              // formatter: '{b} : {c} ({d}%)'
              formatter: '{b} : {c}'
            },
            labelLine: {show: true}

          }
        ]
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