<template>
  <div class="search">
    <van-sticky>
      <van-search
          v-model="searchValue"
          placeholder="请输入搜索关键词"
          show-action
          shape="round"
          @search="onSearch"
      >
        <template #action>
          <div @click="$router.back()">取消</div>
        </template>
      </van-search>

      <van-dropdown-menu>
        <van-dropdown-item v-model="order" :options="option" @change="onchange"/>
      </van-dropdown-menu>
    </van-sticky>
    <van-list
        @load="onLoad"
        finished-text="没有更多了"
        offset="200"
        :finished="numPages<=page"
    >
      <SearchCard
          v-for="(item,index) in searchDataList" :key="index"
          :data="item"
      >
      </SearchCard>
    </van-list>
  </div>
</template>

<script>
import api from "../../axios/api";
import SearchCard from './../../components/search/SearchCard'

export default {
  name: "Search",
  components: {
    SearchCard
  },
  data() {
    return {
      searchDataList: [],
      searchValue: '', //搜索值
      order: 'default', //排序方式
      page: 1, //第几页
      numPages: 0,
      option: [
        {text: '默认排序', value: 'default'},
        {text: '答卷排序', value: 'submit'},
        {text: '时间排序', value: 'time'},
      ],
    }
  },
  methods: {
    onLoad() {
      this.page++
      this.searchProjects(this.searchValue)
    },
    onchange(value) {
      this.order = value
      this.searchDataList=[]
      this.page = 1
      this.numPages = 0
      this.searchProjects(this.searchValue)
    },
    onSearch(value) {
      if (value !== this.$route.query.keyword) {
        this.$router.replace({path: `/questionnaire/search`, query: {keyword: value, order: this.order}})
      }
      this.searchDataList = []
      this.page = 1
      this.numPages = 0
      this.searchProjects(value)
      this.$store.commit('unshiftSearchHistory', {title: value, time: new Date().getTime()})
    },
    searchProjects(value) {
      api.questionnaire.searchProjects({
        keyword: value,
        order: this.order,
        page: this.page
      }).then(response => {
        for (const item of response.data.data.list) {
          this.searchDataList.push(item)
        }
        this.numPages = response.data.data.numPages
      })
    }
  },
  mounted() {
    if (this.$route.query.keyword) {
      this.searchValue = this.$route.query.keyword
      this.searchProjects(this.$route.query.keyword)
    }
  }
}
</script>

<style scoped>
/deep/ .van-dropdown-menu__bar {
  box-shadow: none;
}

</style>