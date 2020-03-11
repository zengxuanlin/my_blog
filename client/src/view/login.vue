<!--
 * @Author: your name
 * @Date: 2020-03-11 16:52:14
 * @LastEditTime: 2020-03-11 17:16:04
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /client/src/view/login.vue
 -->
<template>
  <div class="login">
    <div class="login-form">
      <h1 style="color:#333;margin-bottom:40px;">Myblog Admin Login</h1>
      <Form :label-width="80">
        <FormItem label="账号：">
          <Input type="text" placeholder="Username" v-model="submit.username" />
        </FormItem>
        <FormItem label="密码：">
          <Input type="password" v-model="submit.password" />
        </FormItem>
        <FormItem label="验证码：">
          <div class="flex">
            <Input type="text" style="width:40%;margin-right:30px" v-model="code"/>
            <canvas id="myCanvas"></canvas>
          </div>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="handleSubmit()">登陆</Button>
          <Button @click="handleReset('formCustom')" style="margin-left: 8px">重置</Button>
        </FormItem>
      </Form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      submit: {
        username: "",
        password: ""
      },
      createC:'',
      code:'',
    };
  },
  mounted() {
    this.createCode();
  },
  methods: {
    async handleSubmit() {
      if(this.code !== this.createC){
        this.$Message.error('验证码输入错误')
        return
      }
      this.$Spin.show();
      let res = await this.$ajax.post("/blog/login", this.submit);
      this.$Spin.hide();
      this.$Message.success(res.message);
      if (res.data.token) {
        localStorage.setItem("token", res.data.token);
        this.$router.push({ path: "/admin/articles-list" });
      }
    },
    createCode() {
      var c = document.getElementById("myCanvas");
      var ctx = c.getContext("2d");
      c.width = "120";
      c.height = "40";
      ctx.fillStyle = "#6adbcf";
      ctx.fillRect(0, 0, 120, 40);
      ctx.shadowOffsetX = 2;
      ctx.shadowOffsetY = 2;
      ctx.shadowBlur = 2;
      ctx.shadowColor = "#666666";
      ctx.font = "30px sans-serif";
      var codes = "qwertyuioplkjhgfdsazxcvbnm1234567890";
      var bgColor = ["#f5f5f5", "#666", "#bcbcbc", "yellow"];
      for (let i = 0; i < 4; i++) {
        var r = Math.floor(Math.random() * codes.length);
        var x = 10 + i * 20,
          y = 20 + Math.random() * 10;
          this.createC+=codes[r];
        var b = Math.floor(Math.random() * bgColor.length);
        ctx.fillStyle = bgColor[b];
        ctx.fillText(codes[r], x, y);
      }
    },
    
  }
};
</script>

<style >
.login {
  /* background: url("../assets/login.jpg") center center; */
  background: #f8f8f9;
  width: 100vw;
  height: 100vh;
  background-size: cover;
  display: flex;
  justify-content: center;
}
.login-form {
  text-align: center;
  padding: 20px;
  border-radius: 10px;
  color: #fff !important;
  margin-top: 4rem;
}
.flex{
  display: flex;
  align-items: center;
}
</style>