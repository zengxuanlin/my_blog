<!--
 * @Author: your name
 * @Date: 2020-03-17 17:47:21
 * @LastEditTime: 2020-03-18 10:58:14
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/view/personal_data.vue
 -->
<template>
  <div>
    <Card title="我的资料" style="width:60%;margin-bottom:30px;text-align:left">
      <div style="margin-left:10%;margin-bottom:20px">
        <div :key="update">
          <Avatar icon="ios-person" size="100" :src="host + info.avatar" v-if="info.avatar" />
          <Avatar icon="ios-person" size="100" v-else />
        </div>
        <Upload
          action="http://118.89.125.57/blog/upload"
          style="margin:10px;"
          :on-success="onUpload"
          :show-upload-list='false'
        >
          <Button>点击上传</Button>
        </Upload>
      </div>
      <Form :model="formItem" :label-width="80">
        <FormItem label="昵称：">
          <Input style="width:30%;" v-model="info.nickName"></Input>
        </FormItem>
        <FormItem label="性别：">
          <RadioGroup v-model="info.sex">
            <Radio label="男">男</Radio>
            <Radio label="女">女</Radio>
          </RadioGroup>
        </FormItem>
        <FormItem label="出生日期">
          <DatePicker
            type="date"
            placeholder="日期"
            style="width: 200px"
            @on-change="onChange"
            value="yyyy"
          ></DatePicker>
        </FormItem>
        <FormItem label="来自：">
          <Input style="width:50%;" v-model="info.address"></Input>
        </FormItem>
        <FormItem label="Text">
          <Input
            type="textarea"
            :autosize="{minRows: 2,maxRows: 5}"
            placeholder="写点什么名言吧"
            v-model="info.sign"
          ></Input>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="save">确定</Button>
          <Button style="margin-left: 8px">Cancel</Button>
        </FormItem>
      </Form>
    </Card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrl: "",
      info: {
        address:"",
        age:"",
        avatar:"",
        nickName:"",
        sex:"",
        sign:""
      },
      host: "http://118.89.125.57/images/",
      update: new Date()
    };
  },
  created() {
    this.loadInfo();
  },
  methods: {
    async loadInfo() {
      let res = await this.$ajax.post("/blog/myInfo");
      this.info = res.data.info;
      delete this.info["id"];
      delete this.info["createTime"];
      delete this.info["role_id"];
    },
    onChange(v) {
      let date = v.split("-");
      let born_date = new Date().getFullYear() - parseInt(date[0]);
      this.info.age = born_date.toString();
    },
    onUpload(v) {
      if (v.success) {
        this.$Message.success(v.message);
        this.info.avatar = v.data.uploadUrl;
        this.update = new Date();
        return;
      }
      this.$Message.error("error");
    },
    async save(){
      console.log(this.info)
      let res = await this.$ajax.post('/blog/editData',this.info);
      if(res.success){
        this.$Message.success(res.message)
        this.loadInfo()
        return
      }
    }
  }
};
</script>

<style scoped>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>