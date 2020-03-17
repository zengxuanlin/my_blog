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
      <Layout :style="{padding: '0 50px'}">
        <Content :style="{padding: '24px 0', minHeight: '280px', }">
          
            <Content
              :style="{padding: '24px', minHeight: '280px', background: '#fff',textAalign:'left'}"
            >
              <div class="title">
                <h1>{{text.artTitle}}</h1>
                <Divider dashed />
              </div>
              <div class="content" v-html="text.artContent"></div>
            </Content>

            <Card style="margin-top:20px;text-align:left">
              <p slot="title" style="text-align:left">留言板</p>
              <List>
                <ListItem v-for="(item,index) in comment" :key="index">
                  <ListItemMeta
                    avatar="https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar"
                    :title="item.name"
                    :description="item.content"
                  />
                   <template slot="action">
                <li>
  
                    <Icon type="md-time" /> {{item.time}}
                </li>
            </template>
                </ListItem>
              </List>
            </Card>

            <Card style="margin-top:20px">
              <p slot="title" style="text-align:left">发表留言</p>
              <div class="flex">
                <Input v-model="submit.name" style="width:30%;margin-bottom:20px">
                  <span slot="prepend">您的昵称：</span>
                </Input>
                <Input
                  v-model="submit.content"
                  style="width:50%;margin-bottom:20px"
                  type="textarea"
                  placeholder="说点什么吧 老铁"
                ></Input>
                <Button style="width:10%" type="primary" @click="handleComment">确定</Button>
              </div>
            </Card>
        
        </Content>
      </Layout>
      <Footer class="layout-footer-center">2011-2016 &copy; my blog</Footer>
    </Layout>
  </div>
</template>
<script>
import status from "../mixins/index";
import { gmtToDate } from "../utils";
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
      },
      submit: {
        name: "",
        content: "",
        id:''
      }
    };
  },
  created() {
    this.loadDetail(this.$route.query.id);
    this.submit.id = this.$route.query.id
  },
  methods: {
    async loadDetail(id) {
      let data = await this.$ajax.get("/blog/articles/" + id);
      this.comment = data.data.data.c;
      this.text = data.data.data.text;
      this.comment.forEach(item=>{
        item.time = gmtToDate(item.time);
      })
    },
    handleComment(){
      if(!this.submit['name']){
        this.$Message.warning('请填写姓名')
        return
      }
       if(!this.submit['content']){
        this.$Message.warning('请填写姓名')
        return
      }
      this.$Modal.confirm({
        title:'tip',
        content:'确定发表吗',
        onOk:async ()=>{
          let res = await this.$ajax.post(`/blog/publishRemark`,this.submit);
      if(res.success){
        this.$Message.success(res.message)
        this.loadDetail(this.submit.id);
      }
        }
      })
    }
  }
};
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  position: relative;
  border-radius: 4px;
    background: #f5f7f9;
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
.flex {
  display: flex;
  flex-direction: column;
}
</style>