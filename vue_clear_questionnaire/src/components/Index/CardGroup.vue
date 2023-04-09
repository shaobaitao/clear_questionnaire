<!-- 小问卷卡片组 用在首页展示问卷 -->
<template>
  <div class="cards">
    <el-card
        v-for="(item,index) in data" :key="index"
        :body-style="{ padding: '0px' }" shadow="never"
    >
      <el-image
          style="width: 100%;height: 15vh;"
          :src="require('../../assets/svg/card/'+item.imgNum+'.svg')"
          fit="contain"
          @click="$router.push({ path: `/questionnaire/${item.id}`, query: { bar: '1' } })"
      ></el-image>
      <div class="textDiv"  @click="$router.push({ path: `/questionnaire/${item.id}`, query: { bar: '1' } })">
        <p class="title van-multi-ellipsis--l2">{{ item.title }}</p>
        <p class="username van-ellipsis">{{ item.username }}</p>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "CardGroup",
  props: {
    data: {
      type: Array
    }
  }
}
</script>

<style scoped lang="less">
.cards {
  padding: 6px;
  display: grid;
  grid-template-columns: calc(50% - 3px) calc(50% - 3px);
  grid-gap: 6px;

}

.el-image {
  background-color: @theme-background-color;
}

.textDiv {
  padding: 5px;
  text-align: left;

  p {
    margin: 5px;
  }

  .title {
    font-size: 0.8rem;
    height: 2rem;
    margin-top: 0;
  }

  .username {
    font-size: 0.7rem;
    color: @theme-color;
  }
}
</style>