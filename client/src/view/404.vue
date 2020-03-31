<template>
  <div class="layout">
    <Layout>
      <zHeader></zHeader>

      <div class="error">
        <Icon type="ios-alert" size="80" color="#19be6b" />
        <h3 style="margin-left:20px">这是一个博客DEMO...</h3>
        <router-link to="/register">点击这里</router-link>
        创建个人blog,
        如果已创建,
        <router-link to="/login">请登录</router-link>
      </div>
      <Footer class="layout-footer-center">2011-2020 &copy; My Blog</Footer>
    </Layout>
  </div>
</template>

<script>
import zHeader from "../components/header";
export default {
  components: { zHeader }
};
</script>

<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  height: 100vh;
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
.layout-footer-center {
  text-align: center;
  position: absolute;
  width: 100%;
  bottom: 0;
}
.error {
  width: 80%;
  height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
a{
  margin-left:10px;
}
</style>