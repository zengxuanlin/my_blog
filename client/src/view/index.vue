<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-26 15:37:01
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/view/index.vue
 -->
<template>
  <div class="layout">
    <Layout>
      <zHeader></zHeader>
      <Layout :style="{padding: '0 50px'}" v-if="loaded">
        <Content :style="{padding: '24px 0', minHeight: '280px'}">
          <Layout :gutter="30">
            <Row style="background:#fff;">
              <Col :span="6">
                <z-sider :info="myInfo"></z-sider>
              </Col>
              <Col :span="16" style="height:100%;position:relative">
                <Content
                  :style="{padding: '24px', minHeight: '280px', background: '#fff',textAalign:'left'}"
                >
                  <artices :arts="all"></artices>
                  <Page :total="total" class="page" show-elevator @on-change="onChangePageNum"  :page-size="5" />
                </Content>
              </Col>
              
            </Row>
            
          </Layout>
        </Content>
      </Layout>

      <div v-else class="error">
        <Icon type="ios-alert" size="80" color="#ff9900" />
        <span style="margin-left:20px">出错啦 没有该作者的内容...</span>
      </div>
      <Footer class="layout-footer-center">2011-2020 &copy; My Blog</Footer>
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
    return {
      all: {
        list: [],
      },
      total:0,
      myInfo: {},
      loaded: false,
      homeId: this.$route.params.home_id
    };
  },
  created() {
    if (this.homeId) this.loadInfo();
  },
  methods: {
    loadInfo() {
      this.$ajax
        .post(`/blog/myArticles/${this.homeId}`, this.query)
        .then(res => {
          if (res.success) {
            this.loaded = true;
            this.all = res.data;
            this.myInfo = res.data.info;
            for (let item of res.data.list) {
              item.total = item.commonts.length;
            }
           
            this.total = parseInt(res.data.total)
             console.log(this.total)
          }
        });
    },
    onChangePageNum(num){
      this.query.pageNum = num;
      this.loadInfo()
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
}
.error {
  width: 80%;
  height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>