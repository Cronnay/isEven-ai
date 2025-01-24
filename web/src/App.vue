<script setup lang="ts">
import { ref } from 'vue';
import HelloWorld from './components/HelloWorld.vue'
import Login from './components/Login.vue'
import Voucher from './components/Voucher.vue';

const loginDone = ref(false);
</script>

<template>
  <div class="w-screen h-screen bg-white">
    <Login @done="loginDone = true" v-if="!loginDone" />
    <Voucher v-if="loginDone" />
    <HelloWorld msg="Vite + Vue" />
  </div>
</template>

<style scoped></style>
