<template>
  <div class="create">
    <van-nav-bar
        title="创建问卷"
        @click-left="$router.push('/home/project')"
        @click-right="submit"
        left-arrow
        right-text="创建"
    />
    <van-form>
      <Tip msg="创建问卷"></Tip>
      <van-field
          name="问卷标题"
          placeholder="问卷标题"
          v-model="title"

          show-word-limit
          :rules="[{ required: true, message: '请填写问卷标题' }]"
      />
      <Tip msg="欢迎语"></Tip>
      <van-field
          type="textarea"
          name="欢迎语"
          placeholder="欢迎语"
          v-model="desc"
          maxlength="300"
          show-word-limit
          :rules="[{ required: true, message: '请填写欢迎语' }]"
      />
    </van-form>
  </div>
</template>

<script>
import Tip from '../../components/Tip'
import api from "../../axios/api";
import {Toast} from "vant";

export default {
  name: "Create",
  components: {
    Tip
  },
  data() {
    return {
      title: '',
      desc: '感谢您能抽出几分钟时间来参加本次答题，现在我们马上开始吧！'
    }
  },
  methods: {
    createCheck() {
      if (this.title.length === 0 || this.desc.length === 0) {
        Toast({
          message: '问卷标题或者欢迎语不能为空',
          position: 'bottom',
        })
        return false
      }
      return true
    },
    submit() {
      this.$store.commit('changeIsRefreshProject', true)
      if (this.createCheck())
        api.createQuestionnaire({
          title: this.title,
          desc: this.desc
        }).then(response => {
          this.$store.commit('pushExcludeCachePages', 'Project') //把Project组件的缓存去掉
          response.data.code === 20200 && this.$router.push(`/questionnaire/edit/${response.data.data.projectID}`)
          Toast({
            message: response.data.msg,
            position: 'bottom',
          })
        })

    }
  }
}
</script>

<style scoped lang="less">
.create {
  height: 100vh;
  width: 100vw;
  background-color: rgba(247, 248, 250, 1);
}

</style>