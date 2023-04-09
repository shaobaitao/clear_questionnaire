<template>
  <div class="VCompletion">
    <van-sticky>
      <van-nav-bar
          title="填空题"
          right-text="完成"
          left-arrow
          @click-left="$router.go(-1)"
          @click-right="submit"
      >
      </van-nav-bar>
    </van-sticky>

    <van-form>
      <van-field
          v-model="question.title"
          placeholder="点击编辑题目名称"
      />
      <van-field input-align="right" label="此题必答">
        <template #input>
          <van-switch active-color="#6246ea" v-model="question.required" size="20"/>
        </template>
      </van-field>
      <!--      <van-field input-align="right" name="switch" label="输入框行数">-->
      <!--        <template #input>-->
      <!--          <van-stepper v-model="question.row"/>-->
      <!--        </template>-->
      <!--      </van-field>-->
      <van-field
          v-model="question.desc"
          placeholder="点击编辑题目描述"
      />
      <van-field
          readonly
          clickable
          input-align="right"
          label="内容限制"
          :value="conditionName"
          placeholder="选择限制条件"
          @click="showPicker = true"
      />
      <van-field
          v-model="question.regex"
          placeholder="点击编辑正则表达式"
          v-show="regexShow"
      />
    </van-form>

    <van-popup v-model="showPicker" round position="bottom">
      <van-picker
          show-toolbar
          :columns="columns"
          @cancel="showPicker = false"
          @confirm="onConfirm"
      />
    </van-popup>
  </div>
</template>

<script>
import api from "../../../axios/api";
import {Toast} from "vant";

export default {
  name: "VCompletion",
  data() {
    return {
      question: {
        title: '',
        row: 1,
        required: true,
        regex: '',
        desc: ''
      },
      showPicker: false,
      conditionName: '',
      columns: ['数字', '字母', '中文', '邮箱', '手机号码', '自定义正则表达式'],
      conditions: [
        String.raw`1`,
        String.raw`2`,
        String.raw`3`,
        String.raw`4`,
        String.raw`5`,
        String.raw``,
      ],
      regexShow: false
    }
  },
  methods: {
    questionCheck() {
      return this.question.title.length !== 0
    },
    submit() {
      this.questionCheck() ?
          api.createCompletion({
            projectID: this.$store.state.currentProjectID,
            question: this.question
          }).then(response => {
                response.data.code === 20206 ?
                    this.$router.go(-1) :
                    Toast({
                      message: '创建失败',
                      position: 'bottom',
                    })
              }
          ) : Toast({
            message: '题目标题不能为空',
            position: 'bottom',
          })
    },
    addOption() {
      this.question.options.push({title: ''})
    },
    deleteOption(index) {
      this.question.options.splice(index, 1)
    },
    onConfirm(value) {
      this.conditionName = value
      let name = value
      this.question.regex = this.conditions[this.columns.findIndex(item => {
        return item === name
      })]
      this.showPicker = false;
      (value === '自定义正则表达式') ? this.regexShow = true : this.regexShow = false
    }
  }
}
</script>

<style scoped lang="less">

</style>