<!-- 单选题问题展示 用在问卷收集页 -->
<template>
  <van-radio-group v-model="answer" @input="emitValue">
    <van-cell-group>
      <van-cell
          v-for="(item,index) in options" :key="index"
          clickable
          :title="item.title"
          @click="toggle(index)"
      >
        <template #right-icon>
          <van-radio :name="item.id" ref="radio"/>
        </template>
      </van-cell>
    </van-cell-group>
  </van-radio-group>

</template>

<script>

export default {
  name: "QRadio",
  data() {
    return {
      answer: -1
    }
  },
  props: {
    options: Array,
    showAnswer: {
      type: Number,
      default: -1
    }
  },
  methods: {
    emitValue() {
      this.$emit("input", this.answer)
    },
    toggle(index) {
      this.$refs.radio[index].toggle();
    },
  },
  mounted() {
    this.answer = this.showAnswer
  }
}
</script>

<style scoped>

</style>