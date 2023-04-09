<!-- 题目展示卡片 问卷收集中题目外包的一个卡片样式 -->
<template>
  <div class="questionCard">
    <h4>
      <span v-if="required" style="color: red;position: absolute;left: 20px;top:30px">*</span>
      {{ index + '.' + title }}
      <span style="font-size: 0.8em;color: #aaa;margin: 0 5px">{{ desc + ' ' + questionType[type] }}</span>
    </h4>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "QuestionCard",
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
    desc: String,
    index: Number,
    type: Number,
    required: Boolean
  }
}
</script>

<style scoped lang="less">
.questionCard {
  position: relative;
  min-height: 15vh;
  padding: 15px;
  margin: 20px 0;
  border: 1px solid #ebeef5;
  box-shadow: 0 2px 12px 0 rgb(230, 230, 230);
  //backdrop-filter: blur(8px);

  background-color: #fdfdfd;

  h4 {
    padding-left: 16px;
    margin: 10px 0;
  }
}
</style>