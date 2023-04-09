<!-- 提交详情 用在数据分析表格中 -->
<template>
  <div class="SubmitDetail">
    <van-skeleton title :row="10" :loading="showSkeleton">
      <van-tabs swipeable v-model="active">
        <van-tab title="提交详情">
          <van-cell-group>
            <van-cell :title="`提交ID:${submitSubmitData.submitID }`"/>
            <van-cell :title="`提交IP:${ submitSubmitData.ip }`"/>
            <van-cell :title="`提交时间:${ new Date(submitSubmitData.submitTime * 1000).toLocaleString()}`"/>
            <van-cell
                v-for="({answerText, questionTitle},index) in submitSubmitData.list" :key="index"
                :title="`${index + 1}.${questionTitle}`"
                :label="answerText"
            />
          </van-cell-group>
        </van-tab>
        <van-tab title="还原作答">
          <QuestionPage :questions-data="submitQuestionData"></QuestionPage>
        </van-tab>
        <van-tab title="更多操作">
          <van-button size="normal" plain hairline type="info" @click="deleteSubmit">删除提交</van-button>
        </van-tab>
      </van-tabs>
    </van-skeleton>
  </div>
</template>

<script>
import QuestionPage from './../questions/QuestionPage'
import api from "../../axios/api";

export default {
  name: "SubmitDetail",
  components: {
    QuestionPage
  },
  props: {
    submitQuestionData: {type: Object},
    submitSubmitData: {type: Object},
    submitID: {type: Number, default: -1}
  },
  data() {
    return {
      active: 0,
      showSkeleton: true
    };
  },
  watch: {
    submitSubmitData() {
      this.showSkeleton = !this.showSkeleton
    }
  },
  methods: {
    deleteSubmit() {
      api.questionnaire.deleteSubmit({
        submitID: this.submitID
      }).then(() => {
        this.$emit('refresh')
      })
    }
  },
}
</script>

<style scoped lang="less">
.SubmitDetail {
  width: 80vw;
  height: 70vh;
}

</style>