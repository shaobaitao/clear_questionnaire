<!-- Echarts雷达图 用在数据分析页面中 -->
<template>
  <div class="ChartsRadar" :id="id" :style="styles"></div>
</template>

<script>
const echarts = require('echarts/lib/echarts');
require('echarts/lib/component/title');
require('echarts/lib/component/tooltip');
require('echarts/lib/component/toolbox');
require('echarts/lib/component/legend');
require('echarts/lib/chart/radar');

export default {
  name: "ChartsRadar",
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
          trigger: 'axis'
        },
        radar: {
          radius: '55%',
          indicator: this.chartData.map(item => {
            item.name = item.title;
            item.max = Math.max(...this.chartData.map(item => {
              return item.count
            }))
            return item;
          })
        },
        series: [
          {
            name: this.title,
            center: ['50%', '50%'],
            type: 'radar',
            tooltip: {
              trigger: 'item'
            },
            areaStyle: {},
            data: [
              {
                value: this.chartData.map(item => {
                  return item.count;
                }),
                // label: {
                //   normal: {
                //     show: true,
                //     formatter: function (params) {
                //       return params.value;
                //     }
                //   }
                // }
              },
            ],
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