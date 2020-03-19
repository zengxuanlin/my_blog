<template>
  <div class="page">
    <Card title="我的留言">
      <Table border :columns="columns1" :data="data1.list">
      <template slot="action" slot-scope="{ row, index }">
        <Button type="error" style="margin-left:10px" @click="handleDel(row)">删除</Button>
      </template>
      <template slot="detail" slot-scope="{ row, index }">
        <Button type="primary" @click="handleView(row)">查看</Button>
      </template>
    </Table>
    <Page :total="data1.total" style="margin-top:4rem" />
    </Card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDetail: false,
      showEdit: false,
      columns1: [
        {
          title: "所属博文",
          key: "fromArtTitle"
        },
        {
          title: "留言内容",
          slot: "detail"
        },
        {
          title: "昵称",
          key: "remarkName"
        },
        {
          title: "发表时间",
          key: "remarkName"
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
    async loadList() {
      let res = await this.$ajax.get("/blog/commentList")
      this.data1.list =  res.data
    },
    handleDel(row) {
      this.$Modal.confirm({
        title: "提示",
        content: "确定删除吗",
        onOk: async () => {
          let res = await this.$ajax.get(`/blog/delRemark/${row.remarkId}`)
          if(res.success){
              this.$Message.success(res.message)
              this.loadList()
              return
          }
          this.$message.error('error')
        }
      });
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