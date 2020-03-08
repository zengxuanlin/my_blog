<template>
  <div>
     <Card style="width:100%;text-align:left;margin-bottom:40px" v-for="(item,index) in arts.list" :key="index">
        <p slot="title">
            <Icon type="ios-pricetags-outline" />
            {{item.title}}
        </p>
        <a href="#" slot="extra" @click.prevent="changeLimit">
            <Icon type="ios-loop-strong"></Icon>
            
        </a>
        <ul>
            <div v-html="item.content">

            </div>
        </ul>
         <Input v-model="value" maxlength="100" show-word-limit type="textarea" placeholder="Enter something..." style="width: 400px" />
    </Card>
  </div>
</template>

<script>
import "mavon-editor/dist/css/index.css";
export default {
  name: 'artices',
  data(){
    return {
      value:'',
      arts:{

      },
    }
  },
  created(){
    this.$ajax.get(`/blog/allArticles`).then(res=>{
      this.arts = res.data
    })

  }
}
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

</style>
