import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: () => import('../views/home/Home'),
        meta: {
            title: '首页',
        },
        children: [
            {
                path: '/',
                component: () => import('../views/home/Index'),
                meta: {
                    title: '首页',
                },
            },
        ]
    },
    {
        path: '/home',
        component: () => import('../views/home/Home'),
        meta: {
            title: '首页',
        },
        children: [
            {
                path: '/',
                component: () => import('../views/home/Index'),
                meta: {
                    title: '首页',
                },
            },
            {
                path: 'project',
                name: "Project",
                component: () => import('../views/home/Project'),
                meta: {
                    title: '项目',
                },
            },
            {
                path: 'search',
                component: () => import('../views/home/Search'),
                meta: {
                    title: '搜索',
                },
            },
            {
                path: 'mine',
                component: () => import('../views/home/Mine'),
                meta: {
                    title: '我的',
                },
            },
        ]
    },
    {
        path: '/user',
        component: () => import('../views/user/User'),
        children: [
            {
                path: '/',
                component: () => import('../views/user/Index'),
                meta: {
                    title: '用户系统',
                },
            },
            {
                path: 'login',
                component: () => import('../views/user/Login'),
                meta: {
                    title: '登录',
                },
            },
            {
                path: 'register',
                component: () => import('../views/user/Register'),
                meta: {
                    title: '注册',
                },
            },
            {
                path: 'forgot',
                component: () => import('../views/user/Forgot'),
                meta: {
                    title: '忘记密码',
                },
            },
            {
                path: 'edit/profile',
                component: () => import('../views/user/EditProfile'),
                meta: {
                    title: '修改资料',
                },
            },
        ]
    },
    {
        path: '/questionnaire',
        component: () => import('../views/questionnaire/Questionnaire'),
        children: [
            {
                path: '/',
                component: () => import('../views/questionnaire/Create'),
                meta: {
                    title: '创建问卷',
                },
            },
            {
                path: 'create',
                component: () => import('../views/questionnaire/Create'),
                meta: {
                    title: '创建问卷',
                },
            },
            {
                path: 'edit',
                component: () => import('../views/questionnaire/edit/Edit'),
                children: [
                    {
                        path: 'radio',
                        name: 'VRadio',
                        component: () => import('../views/questionnaire/edit/VRadio'),
                        meta: {
                            title: '创建单选题',
                        },
                    },
                    {
                        path: 'checkBox',
                        name: 'VCheckBox',
                        component: () => import('../views/questionnaire/edit/VCheckBox'),
                        meta: {
                            title: '创建多选题',
                        },
                    },
                    {
                        path: 'completion',
                        name: 'VCompletion',
                        component: () => import('../views/questionnaire/edit/VCompletion'),
                        meta: {
                            title: '创建填空题',
                        },
                    },
                    {
                        path: 'image',
                        name: 'VImage',
                        component: () => import('../views/questionnaire/edit/VImage'),
                        meta: {
                            title: '创建图片题',
                        },
                    },
                    {
                        path: ':id',
                        props: true,
                        component: () => import('../views/questionnaire/edit/Index'),
                        meta: {
                            title: '项目编辑',
                        },
                    },
                ],
                meta: {
                    title: '编辑问卷',
                },
            },
            {
                path: 'analysis',
                component: () => import('../views/questionnaire/analysis/Analysis'),
                children: [
                    {
                        path: '/',
                        component: () => import('../views/questionnaire/analysis/Index'),
                        meta: {
                            title: '问卷数据分析',
                        },
                    },
                    {
                        path: ':id',
                        props: true,
                        component: () => import('../views/questionnaire/analysis/Index'),
                        meta: {
                            title: '问卷数据分析',
                        },
                    }
                ],
                meta: {
                    title: '数据分析',
                },
            },
            {
                path: 'preview/:id',
                component: () => import('../views/questionnaire/Preview'),
                meta: {
                    title: '预览问卷',
                },
            },
            {
                path: 'thanks',
                component: () => import('../views/questionnaire/Thanks'),
                meta: {
                    title: '感谢答卷',
                },
            },
            {
                path: 'search',
                name: 'Search',
                props: true,
                component: () => import('../views/questionnaire/Search'),
                meta: {
                    title: '问卷搜索',
                },
            },
            {
                path: ':id',
                props: true,
                component: () => import('../views/questionnaire/Index'),
            },
        ]
    }
]

const router = new VueRouter({
    routes
})

// 路由守卫 在路由改变前
router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    // console.log(to.fullPath)
    if (localStorage.getItem('token')) {
        next();
    } else {
        next()
        // ([
        //     "/user/login",
        //     "/questionnaire"
        //     ].includes(to.fullPath)) ? next() : next({path: '/user/login'})
        // if (to.fullPath.includes("/questionnaire")) next()
    }
})

export default router
