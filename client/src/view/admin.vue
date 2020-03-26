<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-26 15:20:51
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/view/admin.vue
 -->
<template>
  <div class="layout">
    <Layout>
      <z-header></z-header>
      <Layout style="height:90vh">
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu :active-name="0" theme="light" width="auto" :open-names="['1']">
            <!-- <Submenu name="1">
              <template slot="title">
                <Icon type="ios-navigate"></Icon>Item 1
              </template>
              <MenuItem name="1-1">Option 1</MenuItem>
              <MenuItem name="1-2">Option 2</MenuItem>
              <MenuItem name="1-3">Option 3</MenuItem>
            </Submenu>-->
            <MenuItem
              :name="index"
              v-for="(item,index) in routers"
              :key="index"
              :to="{name:item.name}"
              
            >{{item.title}}</MenuItem>
          </Menu>
        </Sider>
        <Layout :style="{padding: '0 24px 24px',height:'100vh'}">
          <Content :style="{padding: '24px', minHeight: '280px', marginTop:'20px',overflow:'auto'}">
            <router-view></router-view>
          </Content>
        </Layout>
      </Layout>
    </Layout>
  </div>
</template>

<script>
import status from "../mixins/index";
import zHeader from "../components/header";
export default {
  components: { zHeader },
  data() {
    return {
      routers: [
        {
          path: "articles-list",
          title: "我的文章",
          name: "articles-list"
        },
        {
          path: "comment-list",
          name: "comment-list",
          title: "我的留言"
        },
        {
          path: "publish",
          title: "发布文章",
          name: "publish"
        },
        {
          path: "personal-data",
          title: "个人资料",
          name: "personal-data"
        }
      ]
    };
  },
  created() {
  },
  methods: {

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