<!-- 大问卷卡片 用在首页展示问卷 -->
<template>
  <div class="CardBoard">
    <el-card
        :body-style="{ padding: '0px' }" shadow="never"
    >
      <el-image
          style="width: 100%;height: 25vh;"
          :src="require('../../assets/svg/card/'+data.imgUrl+'.svg')"
          fit="contain"
          @click="$router.push({ path: `/questionnaire/${data.id}`, query: { bar: '1' } })"
      ></el-image>
      <div class="textDiv" @click="$router.push({ path: `/questionnaire/${data.id}`, query: { bar: '1' } })">
        <p class="title van-multi-ellipsis--l2">{{ data.title }}</p>
        <!--      <p class="username van-ellipsis">{{ item.username }}</p>-->
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "CardBoard",
  props: {
    data: {
      type: Object
    }
  }
}
</script>

<style scoped lang="less">
.CardBoard {
  padding: 6px;
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
    height: 1rem;
    margin-top: 0;
  }

  .username {
    font-size: 0.7rem;
    color: @theme-color;
  }
}
</style>