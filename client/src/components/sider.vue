<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-18 15:02:16
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/components/sider.vue
 -->
<template>
  <div >
    <Sider hide-trigger :style="{background: '#fff',margin:'0 auto'}">
      <div class="demo-avatar" style="text-align:center">
        <Avatar icon="ios-person" size="100" :src="'http://118.89.125.57/images/'+info.avatar" v-if="info.avatar"/>
        <Avatar icon="ios-person" size="100"  v-else/>
        <div>{{info.nickName}}</div>
        <div>{{info.address}}</div>
        <div>{{info.sign}}</div>
      </div>
    </Sider>
  </div>
</template>

<script>
export default {
  name: "zSider",
  props: {
    info: {
      type: Object,
      default: {},
    }
  },
  mounted(){
    
  }
};
</script>

<style  scoped>
.demo-avatar>div{
  margin:20px 0;
}
.demo-avatar{
  margin-top:30px;
}
</style>