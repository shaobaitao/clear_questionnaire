<template>
  <div class="login">
    <van-nav-bar
        left-text="返回"
        @click-left="$router.back()"
        left-arrow
        :border="false"
    />
    <van-tabs v-model="active">
      <van-tab title="账号登录">
        <van-form @submit="accountSubmit">
          <van-field
              v-model="username"
              name="username"
              placeholder="用户名/邮箱"
              :rules="[{ required: true, message: '请填写用户名' }]"
          />
          <van-field
              v-model="password"
              type="password"
              name="password"
              placeholder="密码"
              :rules="[{ pattern:passwordPattern, message: '密码8~20位并且同时包含大小写字母和数字' }]"
          />
          <div style="margin: 0 auto; width: 90vw">
            <van-button block type="info" native-type="submit">提交</van-button>
          </div>
        </van-form>
      </van-tab>
      <!--      <van-tab title="手机登录">-->
      <!--        <van-form @submit="phoneSubmit">-->
      <!--          <van-field-->
      <!--              v-model="phoneNumber"-->
      <!--              name="phoneNumber"-->
      <!--              placeholder="手机号"-->
      <!--              :rules="[{ pattern:phonePattern, message: '请填写正确手机号' }]"-->
      <!--          />-->
      <!--          <van-field-->
      <!--              v-model="sms"-->
      <!--              center-->
      <!--              clearable-->
      <!--              placeholder="请输入验证码"-->
      <!--              :rules="[{ pattern:smsPattern, message: '请填写正确验证码' }]"-->
      <!--          >-->
      <!--            <template #button>-->
      <!--              <van-button size="small" plain hairline type="info">发送验证码</van-button>-->
      <!--            </template>-->
      <!--          </van-field>-->
      <!--          <div style="margin: 0 auto; width: 90vw">-->
      <!--            <van-button round block type="info" native-type="submit">提交</van-button>-->
      <!--          </div>-->
      <!--        </van-form>-->
      <!--      </van-tab>-->
    </van-tabs>
    <div class="options">
      <p style="float: left" @click="$router.push('forgot')">忘记密码</p>
      <p style="float: right" @click="$router.push('register')"> 注册新账号</p>
    </div>
  </div>
</template>

<script>
import {Toast} from "vant";
import api from "../../axios/api";

export default {
  name: "Login",
  data() {
    return {
      active: 0,
      username: "",
      password: "",
      phoneNumber: "",
      sms: '',
      emailPattern: /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
      passwordPattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,20}$/,//最少8位并且至少同时包含一个字母和一个数字
      phonePattern: /^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$/,
      smsPattern: /^\d{6}$/,
    };
  },
  methods: {
    getUserInfo() {
      api.getUserInfo().then(response => {
        if (response.data.code === 10204) {
          this.$store.commit('setUsername', response.data.data.user.username)
          this.$store.commit('setAvatar', response.data.data.user.avatar)
        }
      })
    },
    accountSubmit(values) {
      api.accountLogin({
        username: values['username'],
        password: require('js-sha256').sha256.hmac('123', values['password'])
      }).then(response => {
        if (response.data.code === 10202) {
          this.username = this.password = ''
          localStorage.setItem('token', response.data.data.token)
          this.getUserInfo()
          this.$store.commit('pushExcludeCachePages', 'Project') //把Project组件的缓存去掉
          this.$router.push('/')
        } else {
          Toast({
            message: response.data.msg,
            position: 'bottom',
          })
        }
      })
    },
    // phoneSubmit(values) {
    //   console.log("phone submit", values);
    // },
  },
};
</script>

<style scoped lang="less">
.login {
  height: 100vh;
  width: 100vw;
  background-color: rgba(247, 248, 250, 1);
}

.options {
  p {
    font-size: 0.8rem;
    color: @theme-color;
  }

  width: 90vw;
  margin: 0 auto;
}


.van-tabs {
  padding-top: 8vh;
}

.van-form {
  padding-top: 3vh;
  background-color: rgba(247, 248, 250, 1);
}

.van-field {
  width: 90vw;
  margin: 10px auto;
  border-radius: 4px;
}

.van-button {
  border-radius: 4px;
}
</style>
