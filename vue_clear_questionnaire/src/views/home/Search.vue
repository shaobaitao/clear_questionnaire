<template>
  <div class="search">
    <van-sticky>
      <van-search
          v-model="searchValue"
          placeholder="请输入搜索关键词"
          @search="onSearch"
      />
    </van-sticky>
    <SearchHistory
        :list-data="$store.state.searchHistoryList"
        :max-row="3"
        @onDelete="onDelete"
        @onClick="onClick"
        @onClean="onClean"
    ></SearchHistory>
  </div>
</template>

<script>
import SearchHistory from '../../components/search/SearchHistory'

export default {
  name: "search",
  components: {
    SearchHistory
  },
  data() {
    return {
      searchValue: '',
      searchHistoryList: []
    }
  },
  watch: {
    "$store.state.searchHistoryList"() {
      window.localStorage.setItem(this.$store.state.username + 'SearchHistoryList', JSON.stringify(this.$store.state.searchHistoryList))
    }
  },
  methods: {
    onSearch(value) {
      this.$router.push({path: `/questionnaire/search`, query: {keyword: value, order: 'default'}})
      this.$store.commit('unshiftSearchHistory', {title: value, time: new Date().getTime()})
    },
    onClick(item) {
      this.$router.push({path: `/questionnaire/search`, query: {keyword: item.title, order: 'default'}})
      this.$store.commit('unshiftSearchHistory', {title: item.title, time: new Date().getTime()})
    },
    onDelete(item, index) {
      this.$store.commit('spliceSearchHistory', index)
    },
    onClean() {
      this.$store.commit('cleanSearchHistory')
    },
  },
  mounted() {
    if (JSON.parse(window.localStorage.getItem(this.$store.state.username + 'SearchHistoryList'))) {
      for (const item of JSON.parse(window.localStorage.getItem(this.$store.state.username + 'SearchHistoryList'))) {
        this.$store.commit('pushSearchHistory', item)
      }
    }
  }
}
</script>

<style scoped lang="less">

</style>