<!-- 问卷卡片轮播图 用在首页展示问卷 -->
<template>
  <div class="CardSwipe">
    <van-swipe style="height: 200px;margin-top: 10px" class="my-swipe" :autoplay="3000">
      <van-swipe-item v-for="(item,index) in data" :key="index">
        <van-image
            style="display: block"
            height="100%"
            fit="contain"
            :src="require('../../assets/svg/swipe/'+item.imgUrl)"
        />
        <span class="musk"></span>
        <span class="swipeTitle">{{ item.title }}</span>
      </van-swipe-item>
    </van-swipe>
  </div>
</template>

<script>
export default {
  name: "CardSwipe",
  props: {
    data: {
      type: Array
    }
  }
}
</script>

<style scoped lang="less">
.my-swipe {
  border-radius: 4px;
  width: calc(100vw - 12px);
  margin: 0 6px;
}

.my-swipe .van-swipe-item {
  color: #fff;
  font-size: 20px;
  line-height: 150px;
  text-align: center;
  background-color: #39a9ed;
}

.my-swipe .van-swipe-item {
  background-color: @theme-background-color;
  line-height: 2rem;
}

.my-swipe .musk {
  height: 2rem;
  width: 100%;
  background: linear-gradient(to bottom, #00000001, #00000077);
  position: absolute;
  bottom: 0;
  left: 0;
}

.swipeTitle {
  font-size: 0.9rem;
  font-weight: bold;
  color: @white;
  position: absolute;
  bottom: 0;
  left: 1rem;
}

/deep/ .van-swipe__indicators {
  left: 85%;
}
</style>