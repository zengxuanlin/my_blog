/*
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-18 16:00:03
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/main.js
 */
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import axios from './api/request'
import router from './router/router'
import ViewUI from 'view-design';
import mavonEditor from 'mavon-editor'
import 'view-design/dist/styles/iview.css';
import 'mavon-editor/dist/css/index.css'
import {gmtToDate} from './utils'
Vue.use(mavonEditor)
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(ViewUI);
Vue.prototype.$ajax = axios
// 注册全局过滤器
Vue.filter('formatDate',value=>{
    return gmtToDate(value)
})
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
