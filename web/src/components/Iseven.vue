<script setup>
import PopupHandler from './PopupHandler.vue';
import { ref } from 'vue';

const firstStep = ref(false);
const toCheck = ref(0);

const isEven = ref("")

function validate() {
  const parsed = parseInt(toCheck.value, 10)
  if (parsed > 56) {
    isEven.value = "Too high of a number"
    return
  }

  if (parsed % 2 != 0) {
    isEven.value = "Sorry. It's odd"
    return
  }
  isEven.value = "Congratulations!!! It's even!"
}
</script>

<template>
  <div class="flex align-center justify-center">
    <form v-if="!secondStep && !thirdStep" class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-gray-800">IsEven?</h2>

      <div class="mb-4">
        <label for="email" class="block text-sm font-medium text-gray-700">Value</label>
        <input v-model="toCheck" type="number" id="email" name="email" placeholder="1337"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>

      <div class="mb-4" v-if="isEven">
        <h3 class="text-xl">{{ isEven }}</h3>
      </div>
      <button @click.prevent="validate()" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Check!
      </button>
    </form>
  </div>
</template>

<style scoped></style>
