import axios from "axios"
// import qs from 'qs';

let service = axios.create()

// 请求拦截器
service.interceptors.request.use(
    config => {
        if (['post', 'get'].includes(config.method)) {
            // post、put 提交时，将对象转换为string, 为处理Java后台解析问题
            // config.data = JSON.stringify(config.data)

            //这里对图片的上传做点处理
            let uploadUrl = [
                'user/upload/avatar'
            ]
            if(!uploadUrl.includes(config.url)){
                // config.data = qs.stringify(config.data)
                config.data = JSON.stringify(config.data)
                // console.log(  config.data  )
            }
            // console.log(config)
        }
        // 带个token
        localStorage.getItem('token') && (config.headers.Authorization = localStorage.getItem('token'))
        return config
    },
    (error) => {
        // 请求错误处理
        return Promise.reject(error)
    }
)

export default service