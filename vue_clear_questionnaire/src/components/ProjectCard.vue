<!-- 问卷项目展示 用在'项目'页面 -->
<template>
  <div class="ProjectCard">
    <p class="title">{{ title }}</p>
    <p class="state" :style="'color:'+states[state].color">{{ states[state].title }} <span
        class="answerCount">答卷:{{ answerCount }}</span></p>
    <div class="buttons">
      <el-link
          :underline="false"
          v-for="(item,index) in buttons" :key="index"
          :icon="item.icon"
          @click="functions[index](id)"
      >
        {{ item.title }}
      </el-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectCard",
  props: {
    id: Number,
    title: String,
    buttons: Array,
    state: Number,
    shareShow: Boolean,
    actionShow: Boolean,
    createdTime: Number,
    answerCount: Number,
    // functions:Object,

  },
  data() {
    return {
      functions: {
        0: id => {
          // this.$store.commit('setCurrentProjectID', id)
          this.$router.push(`/questionnaire/edit/${id}`)
        },
        1: () => {
          this.$emit("changeShareShow", this.id)
        },
        2: id => {
          this.$router.push(`/questionnaire/analysis/${id}`)
        },
        3: () => {
          this.$emit("changeActionShow", this.id)
        },
      },
      states: [
        {title: '●未发布', color: 'orange'},
        {title: '●收集中', color: '#6246ea'},
        {title: '●已停止', color: 'red'}
      ],

    }
  },
  methods: {
    share() {
      this.$emit("changeShareShow", this.id)
    },
  }
}
</script>

<style scoped lang="less">
.ProjectCard {
  position: relative;
  height: 130px;
  width: 100%;
  padding: 10px 20px;
  margin: 6px 0;
  border-radius: 6px;
  border: 1px solid #ebeef5;
  box-shadow: 0 2px 6px 0 rgb(230, 230, 230);
  box-sizing: border-box;
  background-color: #fdfdfd;

  .title {
    font-size: 1.1rem;
    text-align: left;
    color: @text-color;
    margin: 0;
    font-weight: 500;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .state {
    font-size: 0.9rem;
    text-align: left;
    margin: 5px 0;
    font-weight: 400;
  }

  .buttons {
    width: calc(100% - 40px);
    position: absolute;
    display: flex;
    justify-content: space-between;
    align-items: center;
    bottom: 10px;
  }

}

.answerCount {
  margin-left: 0.5rem;
  color: #808080;
}

.el-link {
  color: @theme-color;
}

/deep/ .el-link--inner {
  color: #808080;
}
</style>