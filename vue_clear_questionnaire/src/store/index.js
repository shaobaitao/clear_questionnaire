import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        username: '未登录', // 用户名
        avatar: '', //用户头像
        excludeCachePages: [''], // 缓存排除的页面
        currentProjectID: null, // 目前选中的项目ID
        questions: [], //
        searchHistoryList: [], // 搜索历史
        isRefreshProject: false, // 是否刷新项目页

    },
    mutations: {
        pushExcludeCachePages(state, page) {
            state.excludeCachePages.push(page)
        },
        deleteExcludeCachePages(state, page) {
            let index = state.excludeCachePages.findIndex(item => item === page)
            state.excludeCachePages.splice(index, 1)
        },
        setUsername(state, username) {
            state.username = username
        },
        setAvatar(state, avatar) {
            state.avatar = avatar
        },
        setCurrentProjectID(state, id) {
            state.currentProjectID = id
        },
        setQuestions(state, questions) {
            state.questions = questions
        },
        unshiftSearchHistory(state, item) {
            state.searchHistoryList.unshift(item)
        },
        pushSearchHistory(state, item) {
            state.searchHistoryList.push(item)
        },
        cleanSearchHistory(state) {
            state.searchHistoryList = []
        },
        spliceSearchHistory(state, index) {
            state.searchHistoryList.splice(index, 1)
        },
        changeIsRefreshProject(state, is) {
            state.isRefreshProject = is
        },
    },
    actions: {},
    modules: {}
})
