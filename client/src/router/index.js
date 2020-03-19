/*
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-19 13:42:27
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/router/index.js
 */
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const routes = [
  { path: '/', component: () => import('../view/index') },
  { path: '/login', component: () => import('../view/login'),name:'login' },
  {
    path: '/detail', 
    name:'detail',
    component: () => import('../view/detail'),
  },
  {
    path: '/admin', 
    component: () => import('../view/admin'), 
    children: [
      {
        path: 'publish/', 
        name:'publish',
        component: () => import('../view/publish'),
      },
      {
        path: 'articles-list', 
        name:'articles-list',
        component: () => import('../view/art-list'),
      },
      {
        path: 'personal-data', 
        name:'personal-data',
        component: () => import('../view/personal-data'),
      },
      {
        path: 'comment-list', 
        name:'comment-list',
        component: () => import('../view/comment-list'),
      },
    ]
  },
  {path:'*',redirect:'/'}
]


export default new VueRouter({
  routes,
  mode:'history'
})