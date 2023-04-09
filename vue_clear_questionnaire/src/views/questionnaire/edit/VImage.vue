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
      <van-field
        v-model="question.desc"
        placeholder="点击编辑题目描述"
      />
      <van-field input-align="right" name="switch" label="输入最大图片数量">
        <template #input>
          <van-stepper v-model="question.count"/>
        </template>
      </van-field>


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
        required: true,
        desc: '',
        size: null,
        count: null,
      },
      showPicker: false,
      conditionName: '',
      columns: ['数字', '字母', '中文', '邮箱', '手机号码', '自定义正则表达式'],

      regexShow: false
    }
  },
  methods: {
    questionCheck() {
      return this.question.title.length !== 0
    },
    submit() {
      this.questionCheck() ?
          api.createImage({
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