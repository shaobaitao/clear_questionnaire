<!-- 单选何多选题分析 用在数据分析页面中 -->
<template>
  <div class="AImage">
    <van-tabs
        v-model="active"
        swipeable
    >
      <van-tab title="最新9张" style="padding-top: 5px">
        <van-grid square :column-num="3" :gutter="5">
          <van-grid-item
              v-for="(answer,index) in urls" :key="index"

          >
            <van-image
                fit="cover"
                width="100%"
                height="100%"
                :src="answer"
                @click="preview(answer)"
            />

          </van-grid-item>
        </van-grid>
      </van-tab>

<!--      <van-tab title="下载图片">-->
<!--        123-->
<!--      </van-tab>-->
    </van-tabs>
  </div>
</template>

<script>
const {ImagePreview} = require("vant");
export default {
  name: "AImage",
  props: {
    answers: Array,
    title: String,
    index: Number,
    totalSubmit: Number
  },
  data() {
    return {
      active: 0,
      urls: []
    };
  },
  methods: {
    preview(url) {
      ImagePreview([url])
    }
  },
  mounted() {
    this.urls = this.answers.reverse().slice(0, 9)
  }
}
</script>

<style scoped>
/deep/ .van-grid-item__content {
  padding: 0;
}
</style>