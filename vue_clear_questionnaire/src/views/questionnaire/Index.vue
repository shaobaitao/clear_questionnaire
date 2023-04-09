<template>
  <div class="Index">
    <van-sticky v-if="showBar">
      <van-nav-bar title="问卷查看" left-arrow @click-left="$router.back()"></van-nav-bar>
    </van-sticky>

    <van-empty
        v-show="!showLoading&&emptyDisplay"
        :description="description"
        style="margin-top: 30%"
    />
    <van-loading style="margin-top: 30vh" v-show="showLoading" size="60px" vertical>加载中</van-loading>
    <QuestionPage v-if="!showLoading" mode="submit" :questions-data="questionList.data"></QuestionPage>
  </div>
</template>

<script>
import QuestionPage from "../../components/questions/QuestionPage"
import api from "../../axios/api";

export default {
  name: "Index",
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
      description: '这里的项目空空如也:(',
      showLoading: true,
      emptyDisplay: false,
      showBar: false
    }
  },
  methods: {
    getQuestions() {
      api.questionnaire.getQuestionsPublic({
        projectID: this.$route.params.id
      }).then(response => {
        if (response.data.code === 20403) {
          document.title = this.description = '问卷未发布'
          this.emptyDisplay = true
          return
        }
        this.questionList = response.data
        window.document.title = this.questionList.data.title

        this.showLoading = false
      })
    }
  },
  created() {
    this.getQuestions()
    this.showBar = this.$route.query.bar === '1'
  }
}
</script>

<style scoped lang="less">
.main {
  padding: 5px 20px;

  h2 {
    font-size: 1.4rem;
    text-align: center;
  }

  p {
    text-align: center;
  }
}

</style>