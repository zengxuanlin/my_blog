<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-17 17:13:25
 * @LastEditors: your name
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/App.vue
 -->
<template>
  <div id="app">
    <transition name="fade">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>

export default {
  name: 'App',
  
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.fade-enter, .fade-leave-to {
      opacity: 0;
      position:absolute;
}
.fade-leave, .fade-enter-to {
      opacity: 1
}
.fade-enter-active, .fade-leave-active {
      transition: all .2s
}
</style>
