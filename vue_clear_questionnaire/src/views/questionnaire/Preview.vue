<template>
  <div class="preview">
    <van-sticky>
      <van-nav-bar title="项目预览" safe-area-inset-top left-arrow @click-left="$router.back()"></van-nav-bar>
    </van-sticky>
    <van-empty
        v-if="!isShow"
        description="这里的项目空空如也:("
        :image="require('../../assets/svg/undraw_no_data_re_kwbl.svg')"
        style="margin-top: 30%"
    />
    <QuestionPage v-else :questions-data="questionList.data" mode="show"></QuestionPage>
  </div>
</template>

<script>
import api from "../../axios/api";
import QuestionPage from "../../components/questions/QuestionPage"

export default {
  name: "Preview",
  components: {
    QuestionPage
  },
  props: {
    projectID: String
  },
  data() {
    return {
      isShow: false,
      questionList: {},
    }
  },
  methods: {
    getQuestions() {
      api.questionnaire.getQuestionsPrivate({
        projectID: this.$route.params.id
      }).then(response => {
        this.questionList = response.data
        this.isShow = true
      })
    }
  },
  created() {
    this.getQuestions()
  }
}
</script>

<style scoped lang="less">

</style>