<template>
  <div class="home">
    <keep-alive :exclude="excludeCachePages">
      <router-view/>
    </keep-alive>
    <van-tabbar placeholder route fixed v-model="active">
      <van-tabbar-item replace to="/" icon="home-o">首页</van-tabbar-item>
      <van-tabbar-item replace to="/home/project" icon="orders-o">项目</van-tabbar-item>
      <van-tabbar-item replace to="/home/search" icon="search">搜索</van-tabbar-item>
      <van-tabbar-item replace to="/home/mine" icon="setting-o">我的</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
import {mapState} from 'vuex'
//https://segmentfault.com/q/1010000022685143/a-1020000022686397

export default {
  name: 'Home',
  data() {
    return {
      active: 0,
    }
  },
  computed: {
    ...mapState([
      'excludeCachePages'
    ])
  },
}
</script>

<style scoped lang="less">

</style>