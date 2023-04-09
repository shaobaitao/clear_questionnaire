<!-- 注释题编辑预览 用在题目编辑页面中 -->
<template>
  <EditCard class="e-note">
    {{index+'.'+title}}
  </EditCard>
</template>

<script>
import EditCard from './EditCard'
export default {
  name: "ENote",
  props:{
    index:Number,
    title:String
  },
  components:{
    EditCard
  }
}
</script>

<style scoped>

</style>