<template>
  <div class="page">
    <Card title="我的留言">
      <Table border :columns="columns1" :data="data1.list">
        <template slot="art" slot-scope="{ row, index }">
          <router-link :to="'/detail?id='+row.fromArtId">&lt;&lt;{{row.fromArtTitle}}&gt;&gt;</router-link>
        </template>
        <template slot="action" slot-scope="{ row, index }">
          <Button type="error" style="margin-left:10px" @click="handleDel(row)">删除</Button>
        </template>
        <template slot="detail" slot-scope="{ row, index }">
          <Button type="primary" @click="handleView(row)">查看</Button>
        </template>
      </Table>
      <Page :total="data1.total" style="margin-top:4rem" />
    </Card>
    <Modal v-model="show" title="留言内容">
      <p>{{content}}</p>
    </Modal>
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
          slot: "art"
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
          key: "createTime"
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
      show: false
    };
  },
  created() {
    this.loadList();
  },
  methods: {
    handleView(row) {
      this.content = row.remarkContent;
      this.show = true;
    },
    async loadList() {
      let res = await this.$ajax.get("/blog/commentList");
      this.data1.list = res.data;
    },
    handleDel(row) {
      this.$Modal.confirm({
        title: "提示",
        content: "确定删除吗",
        onOk: async () => {
          let res = await this.$ajax.get(`/blog/delRemark/${row.remarkId}`);
          if (res.success) {
            this.$Message.success(res.message);
            this.loadList();
            return;
          }
          this.$message.error("error");
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