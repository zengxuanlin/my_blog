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
        }else if(to.path === '/'){
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