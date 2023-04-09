<template>
  <div class="project">
    <van-sticky>
      <van-nav-bar title="我的项目" safe-area-inset-top>
<!--        <template #left>-->
<!--          <i class="el-icon-sort"></i>-->
<!--        </template>-->
        <template #right>
          <van-icon name="plus" size="18" @click="$router.push('/questionnaire/create')"/>
        </template>
      </van-nav-bar>
    </van-sticky>

    <van-search
        v-show="!showLoading"
        v-model="searchValue"
        shape="round"
        placeholder="请输入搜索关键词"
    />

    <van-empty
        v-show="!showLoading&&emptyDisplay"
        description="你的项目空空如也"
        :image="require('../../assets/svg/undraw_no_data_re_kwbl.svg')"
    />

    <van-loading style="margin-top: 30vh" v-show="showLoading" type="spinner" size="60px" vertical>加载中</van-loading>

    <van-list
        v-show="listDisplay"
        @load="onLoad"
        :finished="finished"
        finished-text="没有更多了"
    >
      <ProjectCard v-for="(item,index) in list" :key="index"
                   :title="item.title"
                   :id="item.id"
                   :buttons="buttons"
                   :state="item.state"
                   :created-time="item['created_time']"
                   :answer-count="item['submits']"
                   @changeShareShow="changeShareShow($event)"
                   @changeActionShow="changeActionShow($event)"
      >
      </ProjectCard>
    </van-list>

    <van-share-sheet
        v-model="shareShow"
        :title="chooseProjectTitle"
        :options="shareOptions"
        @select="shareSelect"
    />

    <van-action-sheet
        v-model="actionShow"
        :actions="actions"
        cancel-text="取消"
        :title="chooseProjectTitle"
    >
      <van-cell-group>
        <van-cell class="actionCell" title="发布项目" icon="play-circle-o" @click="publishProject"/>
        <van-cell class="actionCell" title="暂停项目" icon="pause-circle-o" @click="suspendProject"/>
        <van-cell class="actionCell" title="预览项目" icon="browsing-history-o"
                  @click="$router.push(`/questionnaire/preview/${chooseProjectID}`)"/>
        <van-cell class="actionCell" title="删除项目" icon="delete-o" @click="deleteProject"/>
        <!--        <van-cell class="actionCell" title="设置项目" icon="setting-o" is-link to="index"/>-->
      </van-cell-group>
    </van-action-sheet>

    <van-popup v-model="showQrcode" :lazy-render="false">
      <!--      <img width="250" height="250" id="qrcode" alt="" src="">-->
      <canvas width="250" height="250" id="qrcode"></canvas>
      <el-link style="color:#6246ea;margin-bottom: 20px" type="primary" @click="saveQrcode">点我保存二维码</el-link>
      <!--      <el-button type="info" plain @click="saveQrcode">保存图片</el-button>-->
    </van-popup>

    <!--    <van-popup v-model="showPost" :lazy-render="false">-->
    <!--      <canvas width="250" height="400" id="post"></canvas>-->
    <!--      <el-link style="color:#6246ea;margin-bottom: 20px" type="primary" @click="savePost">点我保存海报</el-link>-->
    <!--    </van-popup>-->
  </div>
</template>

<script>
import api from "../../axios/api";
import ProjectCard from "../../components/ProjectCard"
import {Toast, Dialog} from "vant";

export default {
  name: "Project",
  components: {
    ProjectCard
  },
  data() {
    return {
      actionShow: false,
      actions: [],
      shareShow: false,
      shareOptions: [
        // 这里发现h5端分享安卓端的这些都不太好整，先不弄了
        // [
        //   {name: '微信', icon: 'wechat', className: 'wechat'},
        //   {name: '朋友圈', icon: 'wechat-moments', className: 'wechat-moments'},
        //   {name: '微博', icon: 'weibo', className: 'weibo'},
        //   {name: 'QQ', icon: 'qq', className: 'qq'},
        // ],
        [
          {name: '网页链接', icon: 'link', className: 'link'},
          {name: '二维码', icon: 'qrcode', className: 'qrcode'},
          // {name: '分享海报', icon: 'poster', className: 'poster'},
          // {name: '小程序码', icon: 'weapp-qrcode', className: 'weapp-qrcode'},
        ],
      ],
      list: [],
      loading: false,
      finished: false,
      page: 1,
      emptyDisplay: false,
      listDisplay: true,
      projectsCount: 9999999,
      buttons: [
        {icon: "el-icon-edit-outline", title: "编辑"},
        {icon: "el-icon-share", title: "分享"},
        {icon: "el-icon-data-analysis", title: "数据"},
        {icon: "el-icon-more", title: "更多"},
      ],
      searchValue: "",
      chooseProjectID: -1,
      chooseProjectTitle: '',
      showLoading: true,
      showQrcode: false,
      qrcodeSrc: '',
      showPost: false,
    }
  },
  watch: {
    "$store.state.isRefreshProject"() {
      if (this.$store.state.isRefreshProject) {
        this.refreshProject()
        this.$store.commit('changeIsRefreshProject', false)
      }
    }
  },
  methods: {
    refreshProject() {
      this.list = []
      this.page = 1
      this.getProjects(this.page)
    },
    publishProject() {
      if (this.list[this.list.findIndex(item => item.id === this.chooseProjectID)].state === 1) {
        Toast({
          message: "项目已发布！",
          position: 'bottom',
        })
        return
      }

      api.publishProject({
        projectID: this.chooseProjectID
      }).then(response => {
        if (response.data.code === 20209) {
          this.list[this.list.findIndex(item => item.id === this.chooseProjectID)].state = 1
        }
        this.actionShow = false
        Toast({
          message: response.data.msg,
          position: 'bottom',
        })
      })
    },
    suspendProject() {
      if (this.list[this.list.findIndex(item => item.id === this.chooseProjectID)].state === 0) {
        Toast({
          message: "项目已暂停！",
          position: 'bottom',
        })
        return
      }

      api.suspendProject({
        projectID: this.chooseProjectID
      }).then(response => {
        if (response.data.code === 20210) {
          this.list[this.list.findIndex(item => item.id === this.chooseProjectID)].state = 0
        }
        this.actionShow = false
        Toast({
          message: response.data.msg,
          position: 'bottom',
        })

      })
    },
    deleteProject() {
      Dialog.confirm({
        title: '确认删除项目？',
      })
          .then(() => {
            api.deleteProject({
              projectID: this.chooseProjectID
            }).then(response => {
              if (response.data.code === 20203) {
                this.actionShow = false
                Toast({
                  message: response.data.msg,
                  position: 'bottom',
                })
              }
              this.list.splice(
                  this.list.findIndex(item => item.id === this.chooseProjectID), 1);
            })
          })
          .catch(() => {
            // on cancel
          });
    },
    shareSelect(option) {
      let f = {
        // "wechat": () => {
        // },
        // "wechat-moments": () => {
        // },
        // "weibo": () => {
        // },
        // "qq": () => {
        // },
        "link": () => {
          this.$copyText(window.location.origin + "/#/questionnaire/" + this.chooseProjectID).then(() => {
            Toast({
              message: '分享链接已复制',
              position: 'bottom',
            })
          }, () => {
            Toast({
              message: '复制失败',
              position: 'bottom',
            })
          })
        },
        // "poster": () => {
        //   this.showPost = true
        //   setTimeout(() => {
        //     const post = document.getElementById("post");
        //     const ctx = post.getContext("2d");
        //     // const img = document.getElementById("postImg");  // 创建一个<img>元素
        //     const img = new Image()
        //     img.src = 'http://192.168.3.5:8080/img/undraw_romantic_getaway_re_3f45.d164bf88.svg'; // 设置图片源地址
        //     img.onload = function () {
        //       ctx.drawImage(img, 0, 0, 250, 200);
        //     }
        //   }, 300)
        // },
        "qrcode": () => {
          this.showQrcode = true
          let QRCode = require('qrcode');
          QRCode.toCanvas(document.getElementById('qrcode'),
              window.location.origin + "/#/questionnaire/" + this.chooseProjectID,
              {
                width: 250,
                height: 250,
                color: {
                  dark: "#6246ea",
                  light: "#ffffff",
                }
              })
        },
      }
      f[option.className]()
    },
    saveQrcode() {
      let FileSaver = require('file-saver')
      let canvas = document.getElementById("qrcode");
      canvas.toBlob(function (blob) {
        FileSaver.saveAs(blob, "wj.png");
      });
    },
    changeShareShow(id) {
      this.shareShow = !this.shareShow
      this.chooseProjectID = id
      this.chooseProjectTitle = this.list.find(item => item.id === this.chooseProjectID).title
    },
    changeActionShow(id) {
      this.actionShow = !this.actionShow
      this.chooseProjectID = id
      this.chooseProjectTitle = this.list.find(item => item.id === this.chooseProjectID).title
    },
    getProjects(page) {
      api.getProjects({
        projectPage: page
      }).then(response => {
        // 如果获取到的项目数量为0，并且获取的页面是第一页
        if (response.data.data['length'] === 0 && page === 1) {
          this.emptyDisplay = true
          this.listDisplay = false
          this.page++
          this.showLoading = false
          return
        }

        response.data.data.forEach(item => {
          if (this.list['length'] < this.projectsCount) {
            this.list.push(item)
          }
        })
        this.$store.commit('deleteExcludeCachePages', 'Project')

        this.page++
        this.showLoading = false
      })
    },
    getProjectsCount() {
      api.getProjectsCount().then(response => {
        this.projectsCount = response.data.data
      })
    },
    onLoad() {
      this.getProjects(this.page)
      if (this.list['length'] >= this.projectsCount) {
        this.finished = true;
      }
    },
  },
  mounted() {
    this.getProjectsCount()
  }
}
</script>

<style scoped lang="less">
@import "../../style/vant";

.project {
  text-align: center;
}

.van-list {
  padding: 0 6px;
}

.van-empty {
  margin-top: 10vh;
  width: 100vw;
}

.actionCell {
  text-align: left;
}

.el-icon-sort {
  font-size: 16px;
  color: @white;
}
</style>