<script setup lang="ts">

  import PopupHandler from './PopupHandler.vue';

  defineProps<{ msg: string }>()

</script>

<template>
  <h1 class="text-lg font-bold underline text-white">{{ msg }}</h1>
  <PopupHandler></PopupHandler>
</template>

<style scoped></style>
