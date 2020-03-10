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
    ]
  },
  // { path: '/login', name:'login',component: ()=>import('../views/login')},
  // { path: '/create_order', component: ()=>import('../views/create_order')},
]


export default new VueRouter({
  routes,
  mode:'history'
})