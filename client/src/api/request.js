import axios from 'axios'
import Vue from 'vue'
import route from '../router/router'
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
        if(res.data.message.includes('token')){
            vueInstance.$Message.error(res.data.message)
            localStorage.removeItem('token')
            route.push({name:'login'})
            return 
        }else{
            return res.data
        }
    }else{
        vueInstance.$Message.error('服务器错误')
    }
},error=>{
    return Promise.reject(error)
})


export default instance