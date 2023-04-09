<!-- 问卷搜索历史 用在问卷搜索页 -->
<template>
  <div class="SearchHistory">
    <van-cell-group>
      <van-cell
          v-for="(item,index) in listData.slice(0,row)" :key="index"
          :title="item.title"
          icon="clock-o"
          @click="$emit('onClick',item)"
      >
        <template #right-icon>
          <van-icon name="cross" class="cross" @click.stop="$emit('onDelete',item,index)"/>
        </template>
      </van-cell>

      <van-cell v-if="!fold&&listData.length!==0" @click="$emit('onClean')" title="清除所有"
                style="text-align: center;color: #888"/>
      <van-cell v-if="fold&&listData.length>maxRow" @click="fold=false" title="展开"
                style="text-align: center;color: #888"/>
    </van-cell-group>
  </div>
</template>

<script>
export default {
  name: "SearchHistory",
  props: {
    listData: {
      type: Array
    },
    maxRow: {
      type: Number,
      default: 3
    }
  },
  data() {
    return {

      fold: true
    }
  },
  computed: {
    row() {
      return this.fold ? this.maxRow : this.listData.length
    }
  }
}
</script>

<style scoped>

.cross {
  font-size: 16px;
  line-height: inherit;
}
</style>