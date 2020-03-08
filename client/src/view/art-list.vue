<template>
  <div class="page" >
    <p>文章管理</p>
    <Table border :columns="columns1" :data="data1">
        <template  slot="action" :slot-scope="{ row, index }">
            <Button type="primary">编辑</Button>
            <Button type="error" style="margin-left:10px">删除</Button>
        </template>
    </Table>
    <Page :total="20"  style="margin-top:4rem"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      columns1: [
        {
          title: "Name",
          key: "name"
        },
        {
          title: "Age",
          key: "age"
        },
        {
          title: "Address",
          key: "address"
        },
        {
            title:'操作',
            slot:'action'
        }
      ],
      data1: [
        {
          name: "John Brown",
          age: 18,
          address: "New York No. 1 Lake Park",
          date: "2016-10-03"
        },
        {
          name: "Jim Green",
          age: 24,
          address: "London No. 1 Lake Park",
          date: "2016-10-01"
        },
        {
          name: "Joe Black",
          age: 30,
          address: "Sydney No. 1 Lake Park",
          date: "2016-10-02"
        },
        {
          name: "Jon Snow",
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-04"
        }
      ]
    };
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