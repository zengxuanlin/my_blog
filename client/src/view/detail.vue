<template>
  <div class="layout">
    <Layout>
      <Header>
        <Menu mode="horizontal" theme="dark" active-name="1">
          <div style="color:#fff;font-size: 26px;float:left">你曾是少年</div>
          <div class="layout-nav" v-if="!hasLogin">
            <MenuItem name="1">
              <router-link to="/login">
                <Icon type="ios-analytics"></Icon>登陆
              </router-link>
            </MenuItem>
            <MenuItem name="2">
              <Icon type="ios-paper"></Icon>注册
            </MenuItem>
          </div>
          <div class="layout-nav" v-else>
            <MenuItem name="1">
              <router-link to="/admin/articles-list">进入后台</router-link>
            </MenuItem>
            <MenuItem name="2">
              <span @click="logout">退出</span>
            </MenuItem>
          </div>
        </Menu>
      </Header>
      <Layout :style="{padding: '0 50px',height:'100vh'}">
        <Content :style="{padding: '24px 0', minHeight: '280px', background: '#fff'}">
          <Layout>
            <!-- <Sider hide-trigger :style="{background: '#fff'}">神的孩子都在跳舞哦</Sider> -->
            <Content
              :style="{padding: '24px', minHeight: '280px', background: '#fff',textAalign:'left'}"
            >
              <div class="title">
                <h1>{{text.artTitle}}</h1>
                <Divider dashed />
              </div>
              <div class="content" v-html="text.artContent"></div>
            </Content>
          </Layout>
        </Content>
      </Layout>
      <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
    </Layout>
  </div>
</template>
<script>
import status from "../mixins/index";
export default {
  mixins: [status],
  data() {
    return {
      comment: [],
      text: {
        artContent: "",
        artTitle: "",
        author: "",
        time: ""
      }
    };
  },
  created() {
    this.loadDetail(this.$route.query.id);
  },
  methods: {
    async loadDetail(id) {
      let data = await this.$ajax.get("/blog/articles/" + id);
      //console.log(data.data.data);
      this.comment = data.data.data.c;
    this.text = data.data.data.text
      console.log(data.data.data.text);
    }
  }
};
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #515a6e;
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
  display: flex;
  justify-content: flex-end;
}
.layout-footer-center {
  text-align: center;
}
a {
  color: #fff;
}
.title {
  margin-bottom: 30px;
}
.content {
  text-align: left;

  padding: 0 40px;
}
</style>