<template>
  <div class="layout">
    <Layout>
      <zHeader></zHeader>

      <div class="error">
        <Icon type="ios-alert" size="80" color="#19be6b" />
        <h3 style="margin-left:20px">这是一个博客DEMO...每个人都可以有自己的主页</h3>
      </div>
      <Footer class="layout-footer-center">2011-2020 &copy; My Blog</Footer>
    </Layout>
  </div>
</template>

<script>
import zHeader from "../components/header";
export default {
  components:{zHeader}
}
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
</style>