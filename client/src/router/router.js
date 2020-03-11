/*
 * @Author: zeng
 * @Date: 2020-03-11 16:52:14
 * @LastEditTime: 2020-03-11 16:56:07
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /client/src/router/router.js
 */
import router from './index'
import ViewUI from 'view-design';
import Vue from 'vue'
Vue.use(ViewUI);

const LOGIN_PAGE_PATH = '/login'
router.beforeEach((to,from,next) => {
    ViewUI.LoadingBar.start();
    let token = localStorage.getItem('token')
    if(token){
        if(to.path === LOGIN_PAGE_PATH){
            next('/admin')
        }else{
            next()
        }
    }else{
        if(to.path === LOGIN_PAGE_PATH){
            next()
        }else if(to.path === '/' || to.path === '/detail'){
            next()
        }else{
            next(LOGIN_PAGE_PATH)
        }
    }
})

router.afterEach(()=>{
    ViewUI.LoadingBar.finish();
})
export default router