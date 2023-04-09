<!-- 填空题问题展示 用在问卷收集页 -->
<template>
<!--  <van-field style="border: 1px solid #eee;" clickable v-model="answer" @input="emitValue"/>-->
  <van-uploader v-model="answer" multiple result-type="dataUrl" @input="emitValue" />
  <!--    这里还有一些正则控制的没加上  -->
</template>

<script>

export default {
  name: "QImage",
  data() {
    return {
      answer: []
    }
  },
  methods: {
    emitValue() {
      this.$emit("input", this.answer)
      console.log(this.answer)
    }
  },
  mounted() {
    // this.answer = this.showAnswer
  }
}
</script>

<style scoped>

</style>