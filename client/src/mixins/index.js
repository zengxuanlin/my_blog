/*
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-18 15:47:52
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/mixins/index.js
 */
import Vue from 'vue'
import route from '../router/router'
const that = new Vue()
export default {
    data(){
        return{
            hasLogin:false,
            webTitle:'My blog',
            isAdmin:false
        }
    },
    created(){
        this.hasLogin = localStorage.getItem('token')?true:false
    },
    methods:{
        logout(){
            console.log(this.isAdmin)
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