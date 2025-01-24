<script setup>
import PopupHandler from './PopupHandler.vue';
import { ref } from 'vue';

const firstStep = ref(false);

</script>

<template>
  <PopupHandler />
  <div class="flex align-center justify-center">
    <form v-if="!secondStep && !thirdStep" class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-gray-800">Download!</h2>
      <button @click.prevent="$emit('done')" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Downloaded
      </button>
    </form>
  </div>
</template>

<style scoped></style>
