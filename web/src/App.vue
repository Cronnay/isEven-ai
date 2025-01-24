<script setup lang="ts">
import { ref } from 'vue';
import HelloWorld from './components/HelloWorld.vue'
import Login from './components/Login.vue'
import Download from './components/Download.vue'
import Voucher from './components/Voucher.vue';
import Credit from './components/Credit.vue';
import IsEven from './components/Iseven.vue';

const loginDone = ref(false);
const downloadDone = ref(false);
const voucherDone = ref(false);
const creditDone = ref(false);
const isEvenDone = ref(false);
</script>

<template>
  <div class="w-screen h-screen bg-white">
    <Login @done="loginDone = true" v-if="!loginDone" />
    <Download @done="downloadDone = true" v-if="loginDone && !downloadDone" />
    <Voucher @done="voucherDone = true" v-if="downloadDone && !voucherDone" />
    <Credit @done="creditDone = true" v-if="voucherDone && !creditDone" />
    <IsEven v-if="creditDone" />
  </div>
</template>

<style scoped></style>
