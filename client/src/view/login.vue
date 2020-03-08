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
          <Input type="text" />
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
      }
    };
  },
  methods: {
    async handleSubmit() {
      this.$Spin.show();
      let res = await this.$ajax.post("/blog/login", this.submit);
      this.$Spin.hide();
      this.$Message.success(res.message);
      if (res.data.token) {
        localStorage.setItem("token", res.data.token);
        this.$router.push({path:'/admin'})
      }
    }
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
</style>