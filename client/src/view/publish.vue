<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-19 09:43:24
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/view/publish.vue
 -->
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
      @imgAdd="handleImgUpload"
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
      if(!this.submit.title){
        this.$Message.warning('请填写标题')
        return
      }
      if(!this.submit.mdText){
        this.$Message.warning('请填写内容')
        return
      }
      this.$ajax.post(`/blog/publishArticle`,this.submit).then(res=>{
        if(res.success){
          this.$Message.success(res.message)
          this.$router.push({name:'articles-list'})
        }
      })
    },
    async handleImgUpload(index,file){
      let fileName = file.name;
      let content = this.submit.mdText;
      let formdata = new FormData()
      formdata.append('file', file)
      let res = await this.$ajax.post('/blog/upload',formdata)
      this.$Message.success('上传成功')
      this.$refs.md.$img2Url(index,'http://118.89.125.57/images/'+res.data.uploadUrl)
      // if(content.includes(fileName)){
      //   let sIndex = content.indexOf(`(${index})`);
      //   let reText = content.slice(sIndex)
      //   let str = content.replace()
      // }
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