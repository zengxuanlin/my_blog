import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import axios from './api/request'
import router from './router/router'
import ViewUI from 'view-design';
import mavonEditor from 'mavon-editor'
import 'view-design/dist/styles/iview.css';
import 'mavon-editor/dist/css/index.css'
Vue.use(mavonEditor)
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(ViewUI);
Vue.prototype.$ajax = axios
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
