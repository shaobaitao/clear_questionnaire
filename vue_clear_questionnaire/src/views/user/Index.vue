<template>
  <div class="index">
    <div class="main">
      <h2>免费易用的</h2>
      <h3>问卷调研·报名表单·考试测评</h3>
    </div>
    <div class="ways">
      <el-button type="primary" icon="el-icon-edit" circle></el-button>
      <el-button type="success" icon="el-icon-check" circle @click="axiosTest"></el-button>
      <el-button type="info" icon="el-icon-phone" circle @click="$router.push('/user/login')"></el-button>
    </div>
  </div>
</template>

<script>

export default {
  name: "Index",
}
</script>

<style scoped lang="less">
.index {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;

  h2, h3 {
    color: rgba(39, 114, 234, 1);
  }
}

.main {
  width: 80vw;
  position: absolute;
  bottom: 55vh;
}

.ways {
  width: 80vw;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: space-around;
  bottom: 20vh;
}
</style>