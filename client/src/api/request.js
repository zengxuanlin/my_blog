import axios from 'axios'
import Vue from 'vue'

let vueInstance = new Vue();
let instance = axios.create({
    baseURL :'http://118.89.125.57'
})

instance.interceptors.request.use(config=>{
    let token = localStorage.getItem('token')
    if(token){
        config.headers.token = token
    }
    return config;
},error=>{
    return Promise.reject(error)
})


instance.interceptors.response.use(res=>{
    if(res.data.code === 200){
        return res.data
    }else{
        vueInstance.$Message.error('服务器错误')
    }
},error=>{
    return Promise.reject(error)
})


export default instance