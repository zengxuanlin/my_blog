<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-17 17:32:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/view/index.vue
 -->
<template>
  <div class="layout">
    <Layout>
      <zHeader></zHeader>
      <Layout :style="{padding: '0 50px'}">
        <Content :style="{padding: '24px 0', minHeight: '280px'}">
          <Layout :gutter="30">
            <Row style="background:#fff">
              <Col :span="6">
                <z-sider></z-sider>
              </Col>
              <Col :span="16">
                <Content
                  :style="{padding: '24px', minHeight: '280px', background: '#fff',textAalign:'left'}"
                >
                  <artices></artices>
                </Content>
              </Col>
            </Row>
          </Layout>
        </Content>
      </Layout>
      <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
    </Layout>
  </div>
</template>
<script>
import artices from "../components/artices";
import status from "../mixins/index";
import zHeader from "../components/header";
import zSider from "../components/sider";
export default {
  mixins: [status],
  components: { artices, zHeader, zSider },
  data() {
    return {};
  },
  created() {},
  methods: {}
};
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  height:100vh
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
}
</style>