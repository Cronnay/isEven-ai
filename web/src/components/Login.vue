<script setup>
import { ref } from 'vue';

const firstStep = ref(false);
const secondStep = ref(false);
const thirdStep = ref(false);

const firstpassword = ref("");
const reenterPassword = ref("");

const phoneNumber = ref(0);


function matchPW() {
  if (firstpassword.value != reenterPassword.value) {
    alert("Your password didn't match.")
    firstpassword.value = false;
    secondStep.value = false;
    thirdStep.value = false;

    firstpassword.value = ""
    reenterPassword.value = ""
  } else {
    secondStep.value = false;
    thirdStep.value = true;
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

    <form v-if="thirdStep" class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-gray-800">Enter information</h2>
      <div class="mb-6">
        <label for="slider" class="block text-sm font-medium text-gray-700">Select your phonenumber</label>
        <input v-model="phoneNumber" type="range" id="slider" name="slider" min="0" max="1000000000" step="1"
          class="mt-1 block w-full">
        <div class="text-sm text-gray-500 mt-1">Value: <span id="sliderValue">{{ phoneNumber }}</span></div>
      </div>


      <div class="mb-4">
        <label for="mother-maiden-name" class="block text-sm font-medium text-gray-700">Your Mother's Maiden
          Name</label>
        <input type="text" id="mother-maiden-name" name="mother-maiden-name" placeholder="Maiden Name"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>

      <label for="credit" class="block text-sm font-medium text-gray-700">Credit Card Details</label>
      <div class="mb-4">
        <input :value="cardText"
          @input="event => cardText = event.value.replace(/[^\d]/g, '').replace(/(\d{4})(?=\d)/g, '$1 ')" type="text"
          id="credit" name="credit" placeholder="1234 5678 9012 3456" maxlength="19"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          oninput="this.value = this.value.replace(/[^\d]/g, '').replace(/(\d{4})(?=\d)/g, '$1 ')">
      </div>
      <div class="grid grid-cols-2 gap-4 mb-10">
        <div>
          <label for="expiry" class="block text-sm font-medium text-gray-700">Expiry Date</label>
          <input type="text" id="expiry" name="expiry" placeholder="MM/YY" maxlength="5"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            oninput="this.value = this.value.replace(/[^\d/]/g, '').replace(/^(\d{2})(\d)/, '$1/$2')">
        </div>
        <div>
          <label for="cvc" class="block text-sm font-medium text-gray-700">CVC</label>
          <input type="text" id="cvc" name="cvc" placeholder="123" maxlength="3"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            oninput="this.value = this.value.replace(/[^\d]/g, '')">
        </div>
      </div>
      <button @click.prevent="$emit('done')" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Submit
      </button>
    </form>
  </div>
</template>

<style scoped></style>
