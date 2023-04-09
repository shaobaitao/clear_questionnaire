<!-- 问卷问题页面 用在问卷收集和展示 -->
<template>
  <div class="QuestionPage">
    <h2>{{ questionList.title }}</h2>
    <p>{{ questionList.desc }}</p>
    <QuestionCard
        v-for="(item,index) in questionList.questions" :key="index"
        :index="index+1"
        :title="item.title"
        :type="item.type"
        :required="item.required"
        :questionID="item.id"
        :desc="item.desc"
    >
      <component
          :is="ComponentName[item.type]"
          v-model="item.answer"
          :options="item.options"
      >
      </component>
    </QuestionCard>

    <van-button type="info" size="large" @click="submit">提交</van-button>
    <p>
      <el-link>{{ questionList['creator'] }}</el-link>
    </p>
    <p>
      <el-link>{{ `清问问卷 2021~${new Date().getFullYear()}` }}</el-link>
    </p>
  </div>
</template>

<script>

import QuestionCard from "./QuestionCard"
import QRadio from "./QRadio"
import QCheckBox from "./QCheckBox"
import QCompletion from "./QCompletion"
import QImage from "./QImage"
import api from "../../axios/api";

export default {
  name: "QuestionPage",
  components: {
    QRadio,
    QCheckBox,
    QCompletion,
    QuestionCard,
    QImage
  },
  props: {
    mode: {
      type: String,
      default: 'show'
    },
    questionsData: {
      type: Object
    }
  },
  data() {
    return {
      ComponentName: {
        1: 'QRadio',
        2: 'QCheckBox',
        3: 'QCompletion',
        6: 'ENote',
        7: 'QImage',
      },
      questionList: {},
      startTime: '', //问卷开答时间 格式时间戳
      duration: '', //问卷用时
    }
  },
  methods: {
    submit() {
      if (this.mode === 'show') {
        this.$toast.fail('预览状态不能提交');
      } else if (this.mode === 'submit') {
        this.questionsNullCheck(this.questionList.questions) ?
            api.questionnaire.postQuestionnaire(
                this.processingSubmitData(this.questionList)
            ).then(res => {
              res.data.code === 20210 && this.$router.push('/questionnaire/thanks')
            })
            : this.$toast.fail('有必答题未答！')
      }
    },
    processingSubmitData(data) {
      delete data.desc
      delete data.title
      delete data.creator
      delete data.avatar
      for (let q of data.questions) {
        delete q.desc
        delete q.title
        delete q.random
        delete q.state
        delete q.serial_number
        delete q.options
      }
      this.duration = Date.now() - this.startTime
      data.duration = this.duration
      return data
    },
    questionsNullCheck(questions) {
      for (let q of questions) if (q.required && !q.answer) return false
      return true
    },
  },
  watch: {
    questionData() {
      this.questionList = this.questionsData
    }
  },
  mounted() {
    this.questionList = this.questionsData
    console.log(this.questionList)
    this.startTime = Date.now()
  }
}
</script>

<style scoped lang="less">
.QuestionPage {
  padding: 2rem 20px 5px 20px;

  h2 {
    font-size: 1.4rem;
    text-align: center;
  }

  p {
    text-align: center;
  }
}

.el-link {
  color: @theme-color;
}
</style>