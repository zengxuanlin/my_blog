<!--
 * @Author: your name
 * @Date: 2020-03-11 16:52:14
 * @LastEditTime: 2020-03-11 17:36:54
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /client/src/components/artices.vue
 -->
<template>
  <div>
    <Card
      style="width:100%;text-align:left;margin-bottom:40px;"
      v-for="(item,index) in arts.list"
      :key="index"
    >
      <p slot="title">
        <Icon type="ios-pricetags-outline" />
        {{item.title}}
      </p>
      <p slot="extra">发表时间:{{item.createTime}}</p>
      <a href="#" slot="extra" @click.prevent="changeLimit">
        <Icon type="ios-loop-strong"></Icon>
      </a>
      <ul class="art-container" @click="toDetail(item,index)" ref="art">
        <div class="mask" :style="{display:'block'}"></div>
          <div v-html="item.content" class="art-content"></div>

      </ul>
      <!-- <Input v-model="value" maxlength="100" show-word-limit type="textarea" placeholder="Enter something..." style="width: 400px;margin-top:10px" /> -->
    </Card>
  </div>
</template>

<script>
import "mavon-editor/dist/css/index.css";
import { gmtToDate } from "../utils";
export default {
  name: "artices",
  data() {
    return {
      value: "",
      arts: {}
    };
  },
  created() {
    this.$ajax.get(`/blog/allArticles`).then(res => {
      for (let t of res.data.list) {
        t.createTime = gmtToDate(t.createTime);
      }
      this.arts = res.data;
    });
  },
  methods: {
    toDetail(item, index) {
      this.$router.push({name:'detail',query:{id:item.id}})
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
</style>
