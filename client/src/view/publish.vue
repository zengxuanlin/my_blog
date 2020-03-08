<template>
  <div>
    <div class="a-title">
      <span>博文标题：</span>
      <Input style="width:80%" v-model="submit.title"/>
    </div>
    <mavon-editor
      v-model="content"
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
        content:''
      }
    };
  },
  methods: {
    // 所有操作都会被解析重新渲染
    change(value, render) {
      // render 为 markdown 解析后的结果[html]
      this.submit.content = render;
    },
    // 提交
    handleSubmit() {
      // console.log(this.content);
      // console.log(this.htmlContent);
      this.$ajax.post(`/blog/publishArticle`,this.submit).then(res=>{
        if(res.success){
          this.$Message.success(res.message)
        }
      })
    }
  }
};
</script>

<style scoped>
.a-title {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}
</style>