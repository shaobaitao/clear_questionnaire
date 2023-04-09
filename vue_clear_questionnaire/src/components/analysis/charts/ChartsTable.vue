<!-- 数据图表 用在数据分析页面中 -->
<template>
  <div class="ChartsTable">
    <el-table
        :data="options"
        border
        show-summary
        :summary-method="getSummaries"
        size="mini"
        style="width: 100%"
    >
      <el-table-column
          prop="title"
          sortable
          align="center"
          min-width="30%"
          label="选项">
      </el-table-column>
      <el-table-column
          prop="count"
          sortable
          align="center"
          min-width="25%"
          label="小计">
      </el-table-column>
      <el-table-column
          prop="count"
          sortable
          min-width="45%"
          label="比例">
        <template slot-scope="scope">
          <el-progress color="#6246ea"
                       :percentage="totalSubmit===0?0:parseFloat((scope.row.count/totalSubmit*100).toFixed(1))"></el-progress>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "ChartsTable",
  props: {
    options: Array,
    totalSubmit: {
      type: Number,
      default: 0
    }
  },
  methods: {
    getSummaries(param) {
      const {columns,} = param;
      const sums = [];
      columns.forEach((column, index) => {
        switch (index) {
          case 0:
            sums[index] = '提交次数'
            break
          case columns.length - 1:
            sums[index] = ''
            break
          default:
            sums[index] = this.totalSubmit
        }
      });
      return sums;
    }
  }
}
</script>

<style scoped>

</style>