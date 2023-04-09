<template>
  <div class="thanks">
    <van-empty
        :image="require('../../assets/svg/undraw_sync_re_492g.svg')"
        description="感谢填写本次问卷"
    >
      <van-button plain round hairline type="info" @click="$router.back()">再填一次</van-button>
    </van-empty>
  </div>
</template>

<script>
export default {
  name: "Thanks"
}
</script>

<style scoped lang="less">
.thanks {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;

  .van-empty {
    margin-bottom: 100px;

    p{
      color: @theme-color;
    }
  }
}
</style>