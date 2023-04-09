<!-- 分析卡片 分析页面中题目外包的一个卡片样式 -->
<template>
  <div class="analysisCard">
    <van-divider />
    <h4>
      {{ index + '.' + title }}
      <span style="font-size: 0.8em;color: #aaa;margin: 0 5px">{{ questionType[type] }}</span>
    </h4>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "AnalysisCard",
  data() {
    return {
      questionType: {
        1: '单选题',
        2: '多选题',
        3: '填空题',
        7: '图片题',
      }
    }
  },
  props: {
    title: String,
    index: Number,
    type: Number,
    required: Boolean
  }
}
</script>

<style scoped lang="less">
.analysisCard {
  position: relative;
  min-height: 15vh;
  padding: 15px;

  background-color: #fdfdfd;

  h4 {
    margin: 10px 0;
  }
}
</style>