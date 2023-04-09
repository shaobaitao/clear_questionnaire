<template>
  <div class="index">
    <van-tabs v-model="active" swipeable>
      <van-tab title="推荐" class="test">
        <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
          <component
              v-for="(item,index) in recommendDataList" :key="index"
              :is="ComponentName[item.type]"
              :data="item.data"
          >
          </component>
        </van-pull-refresh>
      </van-tab>
      <van-tab title="热门">
        <SearchCard
            v-for="(item,index) in hotProjectsList" :key="index"
            :data="item"
        >
        </SearchCard>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import api from "../../axios/api";
import CardGroup from '../../components/Index/CardGroup'
import CardBoard from '../../components/Index/CardBoard'
import CardSwipe from '../../components/Index/CardSwipe'
import SearchCard from '../../components/search/SearchCard'

export default {
  name: 'Index',
  components: { // 各种类型的卡片
    CardGroup,
    CardBoard,
    CardSwipe,
    SearchCard
  },
  data() {
    return {
      active: 0,
      recommendDataList: [],
      ComponentName: {
        1: 'CardGroup',
        2: 'CardBoard',
        3: 'CardSwipe',
      },
      refreshing: false,
      pageNumber: 1, // 当前页码
      scrollY: 0,
      hotProjectsList: []
    }
  },
  methods: {
    onRefresh() {
      setTimeout(() => {
        this.getRecommendations()
        this.refreshing = false;
      }, 1000);
    },
    getRecommendations() {
      api.questionnaire.getRecommendations({
        pageNumber: this.pageNumber
      }).then(response => {
        for (const item of response.data.data.reverse()) {
          this.recommendDataList.unshift(item)
        }
        this.pageNumber++
      })
    },
    getHotProjects() {
      api.questionnaire.getHotProjects().then(response => {
        this.hotProjectsList = response.data.data
      })
    }
  },
  mounted() {
    this.getRecommendations()
    this.getHotProjects()
  },
}
</script>

<style scoped lang="less">
@import "../../style/vant";

.index {
  text-align: center;
}

</style>