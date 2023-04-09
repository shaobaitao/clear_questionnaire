let path = require("path")

// vue.config.js配置文档 https://cli.vuejs.org/zh/config/
module.exports = {


    /**
     * 当路由模式为history时应避免使用相对publicPath
     * publicPath配置说明 https://cli.vuejs.org/zh/config/#publicpath
     */
    publicPath: './',

    /**
     * devServer配置说明
     * https://webpack.docschina.org/configuration/dev-server/
     */
    devServer: {

        /**
         * devServer.proxy配置说明
         * https://cli.vuejs.org/zh/config/#devserver-proxy
         * https://www.cnblogs.com/edwardwzw/p/13261418.html
         */
        proxy: {
            '/user': {
                // target: 'http://192.168.3.5:5000',
                target: 'http://127.0.0.1:5000',
                // target: 'http://wj.shaobaitao.cn/',
                changeOrigin: true,
            },
            '/questionnaire': {
                // target: 'http://192.168.3.5:5000',
                target: 'http://127.0.0.1:5000',
                // target: 'http://wj.shaobaitao.cn/',
                changeOrigin: true,
            }
        },
        // 这里是ip获取城市的接口
        // 'api.php': {
        //     target: 'http://opendata.baidu.com',
        //     ws: true,
        //     changeOrigin: true,
        //     //http://opendata.baidu.com/api.php?query=${ip}9&co=&resource_id=6006&oe=utf8
        // }

    },
    css: {
        loaderOptions: {
            less: {
                modifyVars: {
                    // 直接覆盖变量
                    // 'text-color': '#111',
                    // 'tabs-default-color': 'green',
                    // 'border-color': '#eee',
                    // 'nav-bar-text-color': '#111',
                    // 'nav-bar-icon-color': '#111',
                    // 'tabs-nav-background-color': '#f7f8fa'
                    // 或者可以通过 less 文件覆盖（文件路径为绝对路径）
                    // hack: `true; @import "./src/style/vant.less";`,
                    hack: `true; @import "${path.join(
                        __dirname,
                        './src/style/vant.less'
                    )}";`
                },
            },
        },
    },



}