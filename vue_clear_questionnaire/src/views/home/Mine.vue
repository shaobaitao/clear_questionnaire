<template>
  <div class="mine">
    <ProfileCard :username="username" :avatar-url="avatar"></ProfileCard>
    <van-cell-group>
      <van-cell title="账号信息" icon="info-o" is-link to="/user/edit/profile"/>
<!--      <van-cell title="设置" icon="setting-o"/>-->
      <van-cell title="去登录" icon="info-o" is-link to="/user/login"/>
      <van-cell @click="logOut" title="退出登录" style="text-align: center;color: red"/>
    </van-cell-group>
  </div>
</template>

<script>
import ProfileCard from "../../components/ProfileCard";
import {Dialog} from 'vant';
import {mapState} from 'vuex'
import api from "../../axios/api";

export default {
  name: "Mine",
  data() {
    return {}
  },
  components: {
    ProfileCard
  },
  computed: {
    ...mapState([
      'username',
      'avatar'
    ])
  },
  methods: {
    logOut() {
      Dialog.confirm({
        title: '退出登录',
        message: '是否退出登录？',
        closeOnClickOverlay: true
      })
          .then(() => {
            this.logOutClean()
            this.$router.push("/user/login")
          })
          .catch(() => {
          });
    },
    logOutClean() {
      localStorage.removeItem('token')
      this.$store.commit('setUsername', '未登录')
      this.$store.commit('setAvatar', '')
      this.$store.commit('cleanSearchHistory')
      this.$store.commit('changeIsRefreshProject', true) //清除项目
    },
    getUserInfo() {
      api.getUserInfo().then(response => {
        if (response.data.code === 10204) {
          this.$store.commit('setUsername', response.data.data.user.username)
          this.$store.commit('setAvatar', response.data.data.user.avatar)
        }
      })
    }
  },
  mounted() {
    this.getUserInfo()
  }
}
</script>

<style scoped>

</style>