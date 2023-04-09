<template>
  <p>{{msg}}</p>
</template>

<script>
export default {
  name: "Tip",
  props: {
    msg: String
  }
}
</script>

<style scoped lang="less">
p{
  font-size: 0.9rem;
  color: #888888;
  margin-left: 5vw;
}
</style>