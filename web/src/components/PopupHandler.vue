<template>
    <Popup :top="100" :left="150" title="WARNING!!!" imageUrl="/img1.jpg" message="YOUR COMPUTER IS INFECTED!!!"></Popup>
</template>

<script setup lang="ts">
    import Popup from './Popup.vue';
</script>