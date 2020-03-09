<template>
  <div>
    <div class="a-title" :key=update>
      <span>博文标题：</span>
      <Input style="width:80%" v-model="submit.title"/>
    </div>
    <mavon-editor
      v-model="submit.mdText"
      ref="md"
      @change="change"
      style="min-height: 500px;overflow:auto;max-height:70vh;z-index:999"
    
    />
    <div style="width:100%;text-align:left;margin-top:1rem">

         <RadioGroup v-model="mode" >
        <Radio label="self">对自己可见</Radio>
        <Radio label="pub">公开可见</Radio>
    </RadioGroup>
    </div>
    <Button @click="handleSubmit" type="primary" style="margin:2rem 0;float:left">提交</Button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      content: "", // 输入的markdown
      mode:'self',
      submit:{
        title:'',
        content:'',
        mdText:''
      },
      edit:false,
      update:new Date()
    };
  },
  created(){
    this.update = new Date()
    if(this.$route.params.id){
      let data = JSON.parse(sessionStorage.getItem('cache'))
      console.log(data)
      // this.submit.title = data.title
      // console.log(data)
      // this.submit.content = data.content
      // this.submit.mdText = data.mdText
      // this.edit = true
    }else{
      this.submit={
        title:'',
        content:'',
        mdText:''
      }
    }
  },
  methods: {
    // 所有操作都会被解析重新渲染
    change(value, render) {
      this.submit.mdText = value
      this.submit.content = render;
    },
    // 提交
    handleSubmit() {
      // console.log(this.submit.mdText)
      // return false
      // console.log(this.content);
      // console.log(this.htmlContent);
      this.$ajax.post(`/blog/publishArticle`,this.submit).then(res=>{
        if(res.success){
          this.$Message.success(res.message)
        }
      })
    }
  },

};
</script>

<style scoped>
.a-title {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}
</style>