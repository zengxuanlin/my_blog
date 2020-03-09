<template>
  <div class="page" >
    <p>文章管理</p>
    <Table border :columns="columns1" :data="data1.list">
        <template  slot="action" slot-scope="{ row, index }">
            <Button type="primary" @click="handleEdit(row)">编辑</Button>
            <Button type="error" style="margin-left:10px">删除</Button>
        </template>
         <template  slot="detail" slot-scope="{ row, index }">
            <Button type="primary" @click="handleView(row)">查看</Button>
        </template>
    </Table>
    <Page :total="data1.total"  style="margin-top:4rem"/>
    <Drawer title="详情" :closable="false" v-model="showDetail"   width="640" >
        <div v-html='content'></div>
    </Drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDetail:false,
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
            title:'操作',
            slot:'action'
        }
      ],
      data1: {
        list:[],
        total:'0'
      },
      content:'',
    };
  },
  created(){
    this.$ajax.get('/blog/getMyAllArticles').then(res=>{
      this.data1 = res.data
    })
  },
  methods:{
    handleView(row){
      console.log(row)
      this.content = row.content
      this.showDetail = true
    },
    handleEdit(row){
      sessionStorage.removeItem('cache')
      sessionStorage.setItem('cache',JSON.stringify(row))
      this.$router.push({'path':'/admin/publish/'+row.id})
    }
  }
};
</script>

<style scoped>
.page{
    background: #fff;
    height:80vh;
    padding: 20px;
}
</style>