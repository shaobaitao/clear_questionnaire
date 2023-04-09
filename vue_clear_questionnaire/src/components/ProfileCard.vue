<!-- 用户信息展示卡片 用在'我的'页面 -->
<template>
  <div class="ProfileCard">
    <van-image fit="cover" round width="4rem" height="4rem" :src="avatarUrl"/>
    <p>{{ username }}</p>
  </div>
</template>

<script>
export default {
  name: "ProfileCard",
  props: {
    avatarUrl: String,
    username: String
  },
  data() {
    return {}
  }
}
</script>

<style scoped lang="less">
.ProfileCard {
  width: 100vw;
  height: 20vh;
  //background: #39a9ed;
  background-image: url("../assets/svg/undraw_moonlight_-5-ksn.svg");
  background-size: 100%;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
  align-items: center;

  p {
    margin: 20px;
    font-size: 1.4rem;
    color: #eeeeee;
  }
}
</style>