<template>
  <div class="layout">
    <Layout>
      <Header>
        <Menu mode="horizontal" theme="dark" active-name="1">
          <div class="layout-logo"></div>
          <div class="layout-nav">
            <MenuItem name="1" style="float:right" >
              <Icon type="ios-navigate"></Icon>
              <span @click="logout">退出</span>
            </MenuItem>
            <MenuItem name="1" style="float:right;">
              <router-link to='/'>
                  <Icon type="ios-navigate"></Icon>首页
              </router-link>
            </MenuItem>
          </div>
        </Menu>
      </Header>
      <Layout style="height:90vh">
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu active-name="0" theme="light" width="auto" :open-names="['1']">
            <!-- <Submenu name="1">
              <template slot="title">
                <Icon type="ios-navigate"></Icon>Item 1
              </template>
              <MenuItem name="1-1">Option 1</MenuItem>
              <MenuItem name="1-2">Option 2</MenuItem>
              <MenuItem name="1-3">Option 3</MenuItem>
            </Submenu>-->
            <MenuItem :name="index" v-for="(item,index) in routers" :key="index"  :to="{name:item.name}">
                {{item.title}}
            </MenuItem>
          </Menu>
        </Sider>
        <Layout :style="{padding: '0 24px 24px',height:'100vh'}">
          <Content :style="{padding: '24px', minHeight: '280px', marginTop:'20px',overflow:'auto'}">
            <keep-alive >
              <router-view></router-view>
            </keep-alive>
          </Content>
        </Layout>
      </Layout>
    </Layout>
  </div>
</template>

<script>
import status from '../mixins/index'
export default {
    mixins:[status],
    data(){
        return {
            routers:[
                {
                    path:'articles-list',
                    title:'我的文章',
                    name:'articles-list'
                },
                {
                    path:'',
                    title:'我的留言',
                  
                },
                {
                    path:'publish',
                    title:'发布文章',
                    name:'publish'
                    
                },
                {
                    path:'',
                    title:'个人资料',
                    
                }
            ]
        }
    },
    created(){
        // console.log(this.$router)
    },
    methods:{
        link(p){
   

           if(p){
               this.$router.push({path:p}) 
           }
        }
    }
};
</script>

<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;

}
.layout-logo {
  width: 100px;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 20px;
}


</style>