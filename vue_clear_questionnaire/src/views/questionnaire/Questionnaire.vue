<template>
  <div class="Questionnaire">
    <keep-alive :include="['Search']">
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: "Questionnaire"
}
</script>

<style scoped lang="less">

</style>