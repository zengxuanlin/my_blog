import Vue from 'vue'
import route from '../router/router'
const that = new Vue()
export default {
    data(){
        return{
            hasLogin:false
        }
    },
    created(){
        this.hasLogin = localStorage.getItem('token')?true:false
    },
    methods:{
        logout(){
            that.$Modal.confirm({
                title: '提示',
                content: '<p>确认退出了吗</p>',
                onOk: () => {
                    localStorage.removeItem('token')
                    this.hasLogin = false
                    route.push({path:'/'})
                },
                
            });
        }
    }
}