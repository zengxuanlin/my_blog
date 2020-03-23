<!--
 * @Author: your name
 * @Date: 2020-03-11 16:52:14
 * @LastEditTime: 2020-03-18 15:59:15
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /client/src/components/artices.vue
 -->
<template>
  <div v-if="arts.list.length">
    <Card
      style="width:100%;text-align:left;margin-bottom:40px;"
      v-for="(item,index) in arts.list"
      :key="index"
    >
      <p slot="title">
        <Icon type="ios-pricetags-outline" />
        {{item.title}}
      </p>
      <p slot="extra">发表时间:{{item.createTime | formatDate}}</p>
      <a href="#" slot="extra" @click.prevent="changeLimit">
        <Icon type="ios-loop-strong"></Icon>
      </a>
      <ul class="art-container" @click="toDetail(item,index)" ref="art">
        <div class="mask" :style="{display:'block'}"></div>
        <div class="badge">
          <Badge :count="item.total" v-if="item.total>0">
            <Icon type="ios-notifications-outline" size="26"></Icon>
          </Badge>
        </div>
        <div v-html="item.content" class="art-content markdown-body"></div>
      </ul>
    </Card>
  </div>
  <div v-else>
    <p style="margin-top:50px;">暂时还没文章哦</p>
  </div>
</template>

<script>
import "mavon-editor/dist/css/index.css";
import { gmtToDate } from "../utils";
export default {
  name: "artices",
  props: {
    arts: {
      type: Object,
      default: {}
    }
  },
  created() {},
  methods: {
    toDetail(item, index) {
      this.$router.push({ name: "detail", query: { id: item.id } });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.art-content {
  max-height: 20vh;
  overflow: hidden;
}
.art-container {
  position: relative;
  cursor: pointer;
}
.mask {
  position: absolute;
  bottom: 0;
  background: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 1));
  width: 100%;
  height: 100%;
  opacity: 0.3;
}
.badge{
  float:right;
  margin-right:10px
}
</style>
