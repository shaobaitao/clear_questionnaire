<!-- Echarts词云图 用在数据分析页面中 -->
<template>
  <div class="ChartsWordCloud" :id="id" :style="styles"></div>
</template>

<script>
const echarts = require('echarts/lib/echarts');
import 'echarts-wordcloud';

export default {
  name: "ChartsWordCloud",
  props: {
    id: {
      type: String,
      default: "WordCloud",
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
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b} : {c}'
        },
        legend: {
          type: 'scroll',
          bottom: 5
        },
        series: [{
          // https://github.com/ecomfe/echarts-wordcloud
          type: 'wordCloud',
          shape: 'circle',
          keepAspect: false,
          left: 'center',
          top: 'center',
          width: '100%',
          height: '100%',
          right: null,
          bottom: null,
          sizeRange: [12, 60],
          rotationRange: [-90, 90],
          rotationStep: 45,
          gridSize: 8,
          drawOutOfBound: false,
          layoutAnimation: true,
          textStyle: {
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            color: function () {
              return 'rgb(' + [
                Math.round(Math.random() * 255),
                Math.round(Math.random() * 255),
                Math.round(Math.random() * 255)
              ].join(',') + ')';
            }
          },
          emphasis: {
            focus: 'self',
            textStyle: {
              textShadowBlur: 10,
              textShadowColor: '#333'
            }
          },
          data: this.chartData.map(item => {
            item.name = item.title;
            item.value = item.count
            return item;
          })
        }]
      };
      option && myChart.setOption(option);
      // window.addEventListener("resize", () => {
      //   myChart.resize();
      // });
    },
  },
  mounted() {
    this.draw();
  }
}
</script>

<style scoped>

</style>