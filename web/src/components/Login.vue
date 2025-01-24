<script setup>
import { ref } from 'vue';

const firstStep = ref(false);
const secondStep = ref(false);
const thirdStep = ref(false);

const firstpassword = ref("");
const reenterPassword = ref("");

const emit = defineEmits(['done'])


function matchPW() {
  if (firstpassword.value != reenterPassword.value) {
    alert("Your password didn't match.")
    firstpassword.value = false;
    secondStep.value = false;
    thirdStep.value = false;

    firstpassword.value = ""
    reenterPassword.value = ""
  } else {
    emit("done");
  }
}
</script>

<template>
  <div class="flex align-center justify-center">
    <form v-if="!secondStep && !thirdStep" class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-gray-800">Login</h2>

      <div class="mb-4">
        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
        <input type="email" id="email" name="email" placeholder="Your Email"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>

      <div v-if="firstStep" class="mb-4">
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input v-model="firstpassword" type="password" id="password" name="password" placeholder="Password"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>

      <button v-if="!firstStep" @click.prevent="firstStep = true" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Submit
      </button>
      <button v-if="firstStep" @click.prevent="secondStep = true" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Submit
      </button>

    </form>

    <form v-if="secondStep" class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-gray-800">Reenter passowrd</h2>
      <div v-if="firstStep" class="mb-4">
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input v-model="reenterPassword" type="password" id="password" name="password" placeholder="Password"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>
      <button @click.prevent="matchPW()" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Submit
      </button>
    </form>

  </div>
</template>

<style scoped></style>
