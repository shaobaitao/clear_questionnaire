<template>
  <div class="index">
    <van-sticky>
      <van-nav-bar title="项目编辑" right-text="发布" left-arrow
                   @click-left="$router.back()"
                   @click-right="publishProject"
      ></van-nav-bar>
    </van-sticky>

    <van-loading style="margin-top: 30vh" v-show="showLoading" type="spinner" size="60px" vertical>加载中</van-loading>

    <EditCard
        v-show="active===0||active===1"
        class="e-choice"
        :title="title"
        :desc="desc"
        :pop="false"
    >
    </EditCard>

    <van-empty
        v-if="!showLoading&&questions.length===0"
        description="这里的问题空空如也:("
        style="margin-top: 30%"
    />

    <EditCard
        v-show="active===0||active===1"
        class="e-choice"
        v-for="(item,index) in questions" :key="index"
        :title="item.title"
        :desc="item.desc"
        :index="index+1"
        :type="item.type"
        :required="item.required"
        :questionID="item.id"
        @onSelect="onSelectCard"
    >
      <component
          :is="ComponentName[item.type]"
          :options="item.options"
          :type="item.type"
      >
      </component>
    </EditCard>


    <div class="settings"
         v-show="active===3"
    >
      <van-cell-group inset>
        <van-field
            v-model="title"
            label="标题"
            placeholder="请输入用户名"
            @blur="onBlur('title')"
        />
        <van-field
            v-model="desc"
            rows="3"
            autosize
            label="描述"
            type="textarea"
            placeholder="请输入留言"
            @blur="onBlur('desc')"
        />
      </van-cell-group>
    </div>

    <van-share-sheet v-model="showShare" :options="options" @select="onSelect"/>

    <van-tabbar fixed v-model="active">
      <van-tabbar-item replace icon="plus" @click="showShare=!showShare">添加</van-tabbar-item>
      <van-tabbar-item replace icon="orders-o">题目</van-tabbar-item>
      <van-tabbar-item replace icon="browsing-history-o"
                       @click="$router.push(`/questionnaire/preview/${$route.params.id}`)">预览
      </van-tabbar-item>
<!--      <van-tabbar-item replace icon="setting-o">设置</van-tabbar-item>-->
    </van-tabbar>
  </div>
</template>

<script>
import api from '../../../axios/api'
import {Dialog, Toast} from "vant";
import EditCard from '../../../components/edit/EditCard'
import ENote from '../../../components/edit/ENote'
import ECompletion from '../../../components/edit/ECompletion'
import EChoice from '../../../components/edit/EChoice'
import EImage from '../../../components/edit/EImage'

export default {
  name: "Index",
  components: {
    EditCard,
    ENote,
    ECompletion,
    EChoice,
    EImage
  },
  props: {
    id: String
  },
  data() {
    return {
      questions: {},
      title: '',
      desc: '',
      active: 1,
      showShare: false,
      options: [
        {
          name: '单选题',
          icon: 'https://img01.yzcdn.cn/vant/custom-icon-fire.png',
          className: 'radio'
        },
        {
          name: '多选题',
          icon: 'https://img01.yzcdn.cn/vant/custom-icon-light.png',
          className: 'checkBox'
        },
        {
          name: '填空题',
          icon: 'https://img01.yzcdn.cn/vant/custom-icon-water.png',
          className: 'completion'
        },
        {
          name: '图片题',
          icon: 'https://img01.yzcdn.cn/vant/custom-icon-fire.png',
          className: 'image'
        },
      ],
      ComponentName: {
        1: 'EChoice',
        2: 'EChoice',
        3: 'ECompletion',
        6: 'ENote',
        7: 'EImage',
      },
      showLoading: true
    }
  },
  methods: {
    onBlur(option) {
      const f = {
        'title': () => {

        },
        'desc': () => {

        },
      }
      f[option]()
    },
    onSelect(option) {
      let link = {
        'radio': `radio`,
        'checkBox': `checkBox`,
        'completion': `completion`,
        'image': `image`,
      }
      this.$router.push(link[option.className])
      this.showShare = false;
    },
    onSelectCard(questionID, order) {
      const questionIndex = this.questions.findIndex(item => item.id === questionID)
      switch (order) {
        case 0:
          if (questionIndex !== 0) {
            api.moveQuestion({
              projectID: this.$route.params.id,
              questionID: questionID,
              direction: order
            }).then(response => {
              console.log(response.data)
              Toast({
                message: '上移成功',
                position: 'bottom',
              })
            }).catch(e => {
              Toast({
                message: '移动失败' + e,
                position: 'bottom',
              })
            })
            this.questions[questionIndex] = this.questions.splice(questionIndex - 1, 1, this.questions[questionIndex])[0];
          } else {
            Toast({
              message: '已经是第一个了',
              position: 'bottom',
            })
          }
          break
        case 1:
          if (questionIndex !== this.questions.length - 1) {
            api.moveQuestion({
              projectID: this.$route.params.id,
              questionID: questionID,
              direction: order
            }).then(response => {
              console.log(response.data)
              Toast({
                message: '下移成功',
                position: 'bottom',
              })
            }).catch(e => {
              Toast({
                message: '移动失败' + e,
                position: 'bottom',
              })
            })
            this.questions[questionIndex] = this.questions.splice(questionIndex + 1, 1, this.questions[questionIndex])[0];
          } else {
            Toast({
              message: '已经是最后一个了',
              position: 'bottom',
            })
          }
          break
        case 2:
          Dialog.confirm({
            title: '退出问题',
            message: '是否删除问题？',
            closeOnClickOverlay: true
          })
              .then(() => {
                api.deleteQuestion({
                  projectID: this.$route.params.id,
                  questionID: questionID
                }).then(response => {
                  if (response.data.code === 20208) {
                    this.questions.splice(questionIndex, 1)
                  }
                })
              })
              .catch(() => {
              });
      }
    },
    getQuestions() {
      api.questionnaire.getQuestionsPrivate({
        projectID: this.$route.params.id
      }).then(response => {
        this.questions = response.data.data.questions
        this.title = response.data.data['title']
        this.desc = response.data.data['desc']
        this.showLoading = false
      })
    },
    publishProject() {
      api.publishProject({
        projectID: this.$route.params.id
      }).then(response => {
        Toast({
          message: response.data.msg,
          position: 'bottom',
        })
        this.$store.commit('changeIsRefreshProject', true)
      })
    },
  },
  mounted() {
    this.getQuestions()
    this.$store.commit('setCurrentProjectID', this.$route.params.id)
  }
}
</script>

<style scoped lang="less">
.index {
  margin-bottom: 80px;
}

</style>