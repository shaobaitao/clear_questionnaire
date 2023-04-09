<template>
  <div class="VRadio">
    <van-sticky>
      <van-nav-bar
          title="单选题"
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
      <van-field
          v-for="(item,index) in question.options" :key="index"
          v-model="item.title"
          placeholder="点击编辑选项"
      >
        <template #button>
          <van-button icon="minus" size="mini" type="info" @click="deleteOption(index)"></van-button>
        </template>
      </van-field>
      <div class="btn">
        <el-link type="primary" :underline="false" icon="el-icon-plus" @click="addOption">添加选项</el-link>
      </div>

      <van-field
          v-model="question.desc"
          placeholder="点击编辑题目描述"
      />
      <van-field label="此题必答">
        <template #input>
          <van-switch active-color="#6246ea" style="left: 80%" v-model="question.required" size="20"/>
        </template>
      </van-field>
      <van-field label="选项随机打乱">
        <template #input>
          <van-switch active-color="#6246ea" style="left: 80%" v-model="question.random" size="20"/>
        </template>
      </van-field>
    </van-form>
  </div>
</template>

<script>
import api from "../../../axios/api";
import {Toast} from "vant";

export default {
  name: "VRadio",
  data() {
    return {
      question: {
        id: null,
        title: '',
        desc: '',
        options: [
          {title: ''},
          {title: ''},
        ],
        required: true,
        random: false,
        mode: 0 //0是新建，1是修改
      }
    }
  },
  methods: {
    questionCheck() {
      if (this.question.title.length === 0 || this.question.options.length < 2)
        return false
      for (let i in this.question.options) {
        if (this.question.options[i].title.length === 0) return false
      }
      return true
    },
    submit() {
      if (!this.questionCheck()) {
        Toast({
          message: '题目标题不能为空，题目选项大于等于两个，题目选项标题不能为空',
          position: 'bottom',
        })
        return
      }
      if (this.question.mode === 0) {
        api.createSingleChoice({
          projectID: this.$store.state.currentProjectID,
          question: this.question
        }).then(response => {
          response.data.code === 20204 ?
              this.$router.go(-1) :
              Toast({
                message: response.data.msg,
                position: 'bottom',
              })
        })
      } else {
        api.editSingleChoice({
          projectID: this.$store.state.currentProjectID,
          question: this.question
        }).then(response => {
          Toast({
            message: response.data.msg,
            position: 'bottom',
          })
        })
      }
    },
    addOption() {
      this.question.options.push({title: ''})
    },
    deleteOption(index) {
      this.question.options.splice(index, 1)
    }
  }
}
</script>

<style scoped lang="less">
@import "../../../style/vant";

.btn {
  height: 40px;
  display: flex;
  align-items: center;
  padding-left: 16px;

  .el-link {
    color: @theme-color;
  }
}

</style>