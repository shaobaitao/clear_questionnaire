<!-- 单选和多选题编辑预览 用在题目编辑页面中 -->
<template>
    <div class="EChoice">
      <van-radio-group style="margin-top: 15px" v-if="type===1">
        <van-radio
            v-for="(item,index) in options" :key="index"
            :name="index"
        >
          {{ item.title }}
        </van-radio>
      </van-radio-group>
      <van-checkbox-group style="margin-top: 15px" v-else>
        <van-checkbox
            v-for="(item,index) in options" :key="index"
            :name="index"
            shape="square"
        >
          {{ item.title }}
        </van-checkbox>
      </van-checkbox-group>
    </div>
</template>

<script>
export default {
  name: "EChoice",
  props: {
    options: Array,
    type: Number,
  }
}
</script>

<style scoped lang="less">
.van-radio, .van-checkbox {
  margin-bottom: 10px;
  font-size: 0.9rem;
}
</style>