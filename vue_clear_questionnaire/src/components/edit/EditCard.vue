<!-- 编辑卡片 编辑页面中题目外包的一个卡片样式 -->
<template>
  <div class="editCard">
    <van-popover
        v-if="pop"
        style=" position:absolute;right: 10px"
        v-model="showPopover"
        trigger="click"
        :actions="actions"
        @select="onSelect"
        placement="left"
    >
      <template #reference>
        <van-icon name="ellipsis" size="1.2rem"/>
      </template>
    </van-popover>
    <h4 style="margin-right: 1rem">
      <span v-if="index">{{ index + '.'}}</span>
      {{ title }}

      <span v-if="type&&required" style="font-size: 0.8em;color: #6246ea;margin: 0 5px">
        {{ `【${questionType[type]}】` }}
        {{ `【${(required ? '必填' : '不必填')}】` }}
      </span>
    </h4>
    <h6>{{ desc }}</h6>
    <slot></slot>
  </div>
</template>

<script>

export default {
  name: "EditCard",
  props: {
    index: {
      type: Number,
    },
    title: String,
    desc: String,
    type: Number,
    questionID: Number,
    required: Boolean,
    pop: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      showPopover: false,
      // 通过 actions 属性来定义菜单选项
      actions: [{text: '上移'}, {text: '下移'}, {text: '删除'}],
      questionType: {
        1: '单选题',
        2: '多选题',
        3: '填空题',
        7: '图片题',
      }
    };
  },
  methods: {
    onSelect(action, order) {
      this.$emit('onSelect', this.questionID, order)
    },
  },
}
</script>

<style scoped lang="less">

.editCard {
  position: relative;
  padding: 20px 15px;
  margin: 30px 15px;
  border-radius: 6px;
  border: 1px solid #ebeef5;
  box-shadow: 0 2px 12px 0 rgb(230, 230, 230);
  background-color: #fdfdfd;
  color: #888888;
  font-size: 1.2rem;
  min-height: auto;

  h4 {
    color: #2b2c34;
    font-weight: bolder;
    font-size: 1.2rem;
    margin: 0;
  }

  h6 {
    font-size: 0.9rem;
    margin: 10px 0;
  }
}
</style>