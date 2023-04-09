<template>
  <div class="register">
    <van-nav-bar
        left-text="返回"
        @click-left="$router.back()"
        left-arrow
        :border="false"
    />
    <van-tabs v-model="active">
      <van-tab title="邮箱注册">
        <van-form validate-first @submit="emailSubmit">
          <van-field
              v-model="email"
              name="email"
              placeholder="邮箱"
              :rules="[{ pattern:emailPattern, message: '请填写正确邮箱' }]"
          />
          <van-field
              v-model="emailVCode"
              name="emailVCode"
              type="digit"
              center
              clearable
              placeholder="请输入验证码"
              :rules="[{ pattern:VCodePattern, message: '请填写正确验证码' }]"
          >
            <template #button>
              <van-button style="width: 5rem;" :disabled="emailDisabled" size="small" plain hairline type="info"
                          @click="sentEmail">
                <p v-show="!emailDisabled">发送验证码</p>
                <van-count-down
                    v-show="emailDisabled"
                    ref="emailCountDown"
                    :time="time"
                    format="ss "
                    :auto-start="false"
                    @finish="emailFinish"
                />
              </van-button>
            </template>
          </van-field>
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
      <!--      <van-tab title="手机注册">-->
      <!--        <van-form @submit="phoneSubmit">-->
      <!--          <div class="inputDiv">-->
      <!--            <van-field-->
      <!--                v-model="phoneNumber"-->
      <!--                name="phoneNumber"-->
      <!--                placeholder="手机号"-->
      <!--                :rules="[{ pattern:phonePattern, message: '请填写正确手机号' }]"-->
      <!--            />-->
      <!--            <van-field-->
      <!--                v-model="phoneVCode"-->
      <!--                center-->
      <!--                clearable-->
      <!--                placeholder="请输入验证码"-->
      <!--                :rules="[{ pattern:VCodePattern, message: '请填写正确验证码' }]"-->
      <!--            >-->
      <!--              <template #button>-->
      <!--                <van-button size="small" plain hairline type="info">-->
      <!--                  发送验证码-->
      <!--                  <van-count-down-->
      <!--                      ref="CountDown"-->
      <!--                      :time="time"-->
      <!--                      format="ss "-->

      <!--                  />-->
      <!--                </van-button>-->
      <!--              </template>-->
      <!--            </van-field>-->
      <!--          </div>-->
      <!--          <div style="margin: 0 auto; width: 90vw">-->
      <!--            <van-button round block type="info" native-type="submit">提交</van-button>-->
      <!--          </div>-->
      <!--        </van-form>-->
      <!--      </van-tab>-->
    </van-tabs>
    <div class="options">
      <p>已经有清问账号？<a @click="$router.push('login')">去登录</a></p>
    </div>
  </div>
</template>

<script>
import api from "../../axios/api";
import {Toast} from "vant";

export default {
  name: "Register",
  data() {
    return {
      active: 0,
      time: 30 * 1000,
      email: "",
      password: "",
      phoneNumber: "",
      phoneVCode: '',
      emailVCode: '',
      emailPattern: /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
      passwordPattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,20}$/,//最少8位并且至少同时包含一个字母和一个数字
      phonePattern: /^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$/,
      VCodePattern: /^\d{6}$/,
      emailDisabled: false
    };
  },
  methods: {
    emailFinish() {
      this.emailDisabled = false
    },
    sentEmail() {
      if (this.emailPattern.test(this.email)) {
        this.emailDisabled = true
        this.$refs.emailCountDown.reset();
        this.$refs.emailCountDown.start();
        api.emailRegister({
          'email': this.email
        }).then(response => {
          Toast({
            message: response.data.msg,
            position: 'bottom',
          })
        })
      }
    },
    emailSubmit(values) {
      Toast({
        message: '已提交',
        position: 'bottom',
      })
      api.emailActivate({
        email: values['email'],
        emailVCode: values['emailVCode'],
        password: require('js-sha256').sha256.hmac('123', values['password'])
      }).then(response => {
        Toast({
          message: response.data.msg,
          position: 'bottom',
        })
        response.data.code === 10200 && (this.email = this.emailVCode = this.password = '')
      })
    },
    // phoneSubmit(values) {
    //   console.log("phone submit", values);
    // },
  },

}
</script>

<style scoped lang="less">
.register {
  height: 100vh;
  width: 100vw;
  background-color: rgba(247, 248, 250, 1);
}

.options {
  p {
    a {
      font-size: 0.8rem;
      color: @theme-color;
    }

    font-size: 0.8rem;
    color: #929292;
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