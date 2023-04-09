<template>
  <div class="EditProfile">
    <van-nav-bar
        left-text="返回"
        @click-left="$router.back()"
        left-arrow
        :border="false"
    />
    <van-cell @click="usernameDialog=!usernameDialog" center title="用户名" is-link :value="username"/>
    <van-dialog
        v-model="usernameDialog"
        @confirm="commitUsername"
        :close-on-click-overlay="true"
        show-cancel-button
        title="修改用户名">
      <p style="font-size: 0.7rem;text-align: center" v-text="usernameMsg"></p>
      <van-field
          v-model="newUsername"
          name="newUsername"
          placeholder="请输入用户名"
      />
    </van-dialog>
    <van-cell @click="avatarDialog=!avatarDialog" center title="头像" is-link :value="username">
      <template>
        <van-image fit="cover" round width="3rem" height="3rem" :src="avatar"/>
      </template>
    </van-cell>
    <van-dialog
        style="text-align: center;"
        v-model="avatarDialog"
        @confirm="commitAvatar"
        :close-on-click-overlay="true"
        show-cancel-button
        title="修改头像">
      <van-uploader
          preview-size="150px"
          v-model="fileList"
          :max-count="1"
          :after-read="afterRead"
          :max-size="1024 * 1024"
          @oversize="onOversize"
      />
    </van-dialog>
  </div>
</template>

<script>
import {mapState} from "vuex";
import api from "../../axios/api";
import {Toast} from "vant";

export default {
  name: "EditProfile",
  data() {
    return {
      usernameDialog: false,
      avatarDialog: false,
      newUsername: '',
      usernameMsg: "6~20个字符\n不能含有'@''qw_'\n不能数字开头",
      usernamePattern: /^\w{1,20}$/,
      fileList: [],
      avatarFile: {}
    }
  },
  methods: {
    onOversize() {
      Toast({
        message: '文件不得大于1MB',
        position: 'bottom',
      })
    },
    commitAvatar() {
      let param = new FormData()
      param.append('avatar', this.avatarFile.file)
      console.log(param)
      api.uploadAvatar(param).then(response => {
        response.data.code === 10206 && this.getUserInfo()
        this.avatarFile = {}

        this.fileList = []
      })
    },
    afterRead(file) {
      let imgTypes = [
        'png', 'jpeg', 'jpg', 'gif', 'webp'
      ]
      imgTypes = imgTypes.map(item => {
        return 'image/' + item
      })
      if (!imgTypes.includes(file.file.type)) {
        Toast({
          message: '图片格式只能为png、jpeg、jpg、gif、webp',
          position: 'bottom',
        })
        return
      }
      this.avatarFile = file
    },
    /**
     * @param {string} username
     * @returns {boolean}
     */
    usernameCheck(username) {
      return !(!this.usernamePattern.test(username) ||
          username.includes('@') ||
          username.includes('qw_') ||
          (username.charAt(0) >= '0' && username.charAt(0) <= '9'))
    },
    commitUsername() {
      if (this.$store.state.username === this.newUsername) {
        Toast({
          message: '用户名未改动',
          position: 'bottom',
        })
        return
      }
      if (this.usernameCheck(this.newUsername)) {
        api.changeUsername({
          newUsername: this.newUsername
        }).then(response => {
          Toast({
            message: response.data.msg,
            position: 'bottom',
          })
          response.data.code === 10205 && this.getUserInfo()
        })
      } else {
        Toast({
          message: '用户名格式不正确',
          position: 'bottom',
        })
      }
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
  computed: {
    ...mapState([
      'username',
      'avatar'
    ])
  }
}
</script>

<style scoped lang="less">
.EditProfile {
  background-color: #f7f8fa;
  height: 100vh;
  width: 100vw;
}
</style>