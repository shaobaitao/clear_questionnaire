<!-- 多选题问题展示 用在问卷收集页 -->
<template>
  <van-checkbox-group v-model="answer" @input="emitValue">
    <van-cell-group>
      <van-cell
          v-for="(item,index) in options" :key="index"
          clickable
          :title="item.title"
          @click="toggle(index)"
      >
        <template #right-icon>
          <van-checkbox shape="square" :name="item.id" ref="checkboxes"/>
        </template>
      </van-cell>
    </van-cell-group>
  </van-checkbox-group>
</template>

<script>

export default {
  name: "QCheckBox",
  data() {
    return {
      answer: []
    }
  },
  props: {
    options: Array,
    showAnswer: {
      type: Array,
    }
  },
  methods: {
    emitValue() {
      this.$emit("input", this.answer)
    },
    toggle(index) {
      this.$refs.checkboxes[index].toggle();
    }
  },
  mounted() {
    this.answer = this.showAnswer
  }
}
</script>

<style scoped>

</style>