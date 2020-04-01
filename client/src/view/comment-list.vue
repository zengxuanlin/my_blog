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
        <template slot="remarkTime" slot-scope="{ row, index }" >
          {{row.remarkTime | gmtToDate}}
        </template>
      </Table>
      <Page :total="data1.total" style="margin-top:4rem" show-total @on-change="onChangePageNum" :page-size="5"/>
    </Card>
    <Modal v-model="show" title="留言内容">
      <p>{{content}}</p>
    </Modal>
  </div>
</template>

<script>
import mixins from '../mixins/index'
export default {
  mixins:[mixins],
  data() {
    return {
      showDetail: false,
      showEdit: false,
      columns1: [
        {
          title: "所属博文",
          slot: "art",
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
          slot: "remarkTime"
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
      let res = await this.$ajax.post("/blog/commentList",this.query);
      this.data1 = res.data;
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
    },
    onChangePageNum(num){
      this.query.pageNum = num
      this.loadList()
    },
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