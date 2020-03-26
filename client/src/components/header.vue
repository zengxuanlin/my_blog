<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-26 15:35:20
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/components/header.vue
 -->
<template>
  <Header>
    <Menu mode="horizontal" theme="dark" active-name="1">
      <div style="color:#fff;font-size: 26px;float:left">
        <router-link to="/">{{webTitle}}</router-link>
      </div>
      <div class="layout-nav" v-if="!hasLogin">
        <MenuItem name="1">
          <router-link to="/login">
            <Icon type="ios-analytics"></Icon>登陆
          </router-link>
        </MenuItem>
        <MenuItem name="2">
          <router-link to="/register">
            <Icon type="ios-paper"></Icon>注册
          </router-link>
        </MenuItem>
      </div>
      <div class="layout-nav" v-if="hasLogin">
        <MenuItem name="1">
          <router-link to="/admin/articles-list" v-if="!isHomePage">进入后台</router-link>
          <a href="#" @click="toHome" v-else>个人主页</a>
        </MenuItem>
        <MenuItem name="2">
          <span @click="logout">退出</span>
        </MenuItem>
      </div>
    </Menu>
  </Header>
</template>

<script>
import status from "../mixins/index";
export default {
  name: "zHeader",
  mixins: [status],
  data() {
    return {
      isHomePage: false
    };
  },
  created() {
    if (this.$route.path.includes("admin") && this.hasLogin) {
      this.isHomePage = true;
    } else {
      this.isHomePage = false;
    }
  },
  methods:{
    toHome(){
      this.$router.push(`/home/${localStorage.getItem('home_id')}`)
    }
  }
};
</script>

<style scoped>
a {
  color: #fff;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>>