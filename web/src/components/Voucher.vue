<script setup lang="ts">
import { ref } from 'vue'

defineProps<{}>()

const textInput = ref("")
const correctInput = ref(false)
const submitted = ref(false)

function voucherCheck() {

    if (textInput.value == "abba") {
        correctInput.value = true
    } else {
        correctInput.value = false
    }
    submitted.value = true

}

</script>

<template>

  <div v-if="!correctInput" class="flex align-center justify-center">
    <form class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
        
      <div class="mb-4">
        <label for="Voucher input" class="block text-sm font-medium text-gray-700">Input Voucher</label>
        <input v-model="textInput" type="text" id="voucherInput" name="voucherInput" placeholder=""
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>

      <button @click.prevent="voucherCheck()" type="submit"
        class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        Submit
      </button>  

      <div v-if="submitted && !correctInput" class="mb-4">
        <p class="pt-2">Voucher wrong</p>
      </div>

    </form>
  </div>
  <div v-if="correctInput" class="flex align-center justify-center">
    <form class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">

        <div class="mb-4">
            <div class=""></div>
        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
        <input type="email" id="email" name="email" placeholder="Your Email"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
      </div>
    </form>
  </div>
</template>