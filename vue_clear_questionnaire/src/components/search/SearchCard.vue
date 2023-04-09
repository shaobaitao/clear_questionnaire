<!-- 问卷搜索小卡片 用在问卷搜索页 -->
<template>
  <div class="searchCard">
    <div class="main">
      <el-image
          :src="require('../../assets/svg/card/'+data.imgUrl+'.svg')"
          fit="contain"
          @click="$router.push({ path: `/questionnaire/${data.id}`, query: { bar: '1' } })"
      ></el-image>
      <div class="textDiv" @click="$router.push({ path: `/questionnaire/${data.id}`, query: { bar: '1' } })">
        <p class="title van-multi-ellipsis--l2">{{ data.title }}</p>
        <p class="id van-ellipsis">{{ 'ID:' + data.id }}</p>
        <p class="submits van-ellipsis">{{ '答卷:' + data.submits }}</p>
        <p class="username van-ellipsis">{{ data.username }}</p>
        <p class="date van-ellipsis">{{ new Date(data.created_time * 1000).toLocaleString() }}</p>
      </div>
    </div>
    <van-divider/>
  </div>
</template>

<script>
export default {
  name: "SearchCard",
  props: {
    data: {
      type: Object
    }
  }
}
</script>

<style scoped lang="less">
.van-divider {
  border-color: #ddd;
  margin: 8px 0;
}

.searchCard {
  margin: 16px 0;
  padding: 0 6px;
  height: calc((50vw - 6px) / 16 * 9);

  .main {
    width: 100%;
    height: 100%;
  }
}

.el-image {
  background-color: @theme-background-color;
  float: left;
  border-radius: 4px;
  width: 50%;
  height: 100%;
}

.textDiv {
  display: block;
  width: 50%;
  height: 100%;
  float: left;
  //padding: 5px;
  text-align: left;
  position: relative;

  p {
    margin: 0 5px;
    font-size: 0.7rem;
    color: @text-gray;
    position: absolute;
  }

  .title {
    font-size: 0.9rem;
    color: @text-color;
  }

  .submits {
    color: @theme-color;
    bottom: 2.7rem;
  }

  .id {
    bottom: 1.8rem;
  }

  .username {
    bottom: 0.9rem;
  }

  .date {
    bottom: 0;
  }

}
</style>