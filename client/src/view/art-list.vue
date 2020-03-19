<template>
  <div class="page">
    <Card title="文章管理">
      <Table border :columns="columns1" :data="data1.list">
      <template slot="action" slot-scope="{ row, index }">
        <Button type="primary" @click="handleEdit(row)">编辑</Button>
        <Button type="error" style="margin-left:10px" @click="delArticle(row)">删除</Button>
      </template>
      <template slot="detail" slot-scope="{ row, index }">
        <Button type="primary" @click="handleView(row)">查看</Button>
      </template>
    </Table>
    <Page :total="data1.total" style="margin-top:4rem" />
    </Card>
    <Drawer title="详情" :closable="false" v-model="showDetail" width="640">
      <div v-html="content"></div>
    </Drawer>
    <Drawer title="编辑" :closable="false" v-model="showEdit" width="100" :mask-closable="false">
      <div class="a-title">
        <span>博文标题：</span>
        <Input style="width:80%" v-model="detail.title" />
      </div>
      <mavon-editor
        v-model="detail.mdText"
        ref="md"
        @change="change"
        style="min-height: 500px;overflow:auto;max-height:100vh;z-index:999"
      />
      <div style="width:100%;text-align:left;margin-top:1rem">
        <RadioGroup >
          <Radio label="self">对自己可见</Radio>
          <Radio label="pub">公开可见</Radio>
        </RadioGroup>
      </div>
      <div class="demo-drawer-footer" style="margin-top:3rem">
        <Button style="margin-right: 8px" @click="showEdit = false">取消</Button>
        <Button type="primary" @click="handleSubmit">确定</Button>
      </div>
    </Drawer>
  </div>
</template>

<script>
import {gmtToDate} from '../utils'
export default {
  data() {
    return {
      showDetail: false,
      showEdit: false,
      columns1: [
        {
          title: "标题",
          key: "title"
        },
        {
          title: "内容",
          slot: "detail"
        },
        {
          title: "发布时间",
          key: "time"
        },
        {
          title: "操作",
          slot: "action"
        }
      ],
      data1: {
        list: [],
        total: 2
      },
      content: "",
      detail: {
        title: "",
        content: "",
        mdText: ""
      }
    };
  },
  created() {
    this.loadList();
  },
  methods: {
    change(value, render) {
      this.detail.mdText = value;
      this.detail.content = render;
    },
    handleView(row) {
      console.log(row);
      this.content = row.content;
      this.showDetail = true;
    },
    handleEdit(row) {
      this.showEdit = true;
      this.detail = row;
    },
    loadList() {
      this.$ajax.get("/blog/getMyAllArticles").then(res => {
        this.data1 = res.data;
        for(let t of res.data.list){
          t.time = gmtToDate(t.time)
        }
      });
    },
    handleSubmit() {
      this.$Modal.confirm({
        title: "提示",
        content: "确定提交吗",
        onOk: () => {
          this.$ajax.post(
            `/blog/edit/${this.detail.id}`,
            this.detail
          ).then(res=>{
            if(res.success){
              this.$Message.success('修改成功')
              this.showEdit = false;
              this.loadList()
            }
          })
        }
      });
    },
    delArticle(row){
      this.$Moadl.confirm({
        title:'提示',
        content:'确定删除吗?',
        onOk:async ()=>{
          let res = await this.$ajax.get(`/blog/delete/${row.id}`);
          if(res.success){
            this.$Message.success(res.message)
            return
          }
          this.$Message.error('删除失败')
        }
      })
    }
  }
};
</script>

<style scoped>
.page {
  background: #fff;
  height: 80vh;
  padding: 20px;
}
.a-title {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}
</style>