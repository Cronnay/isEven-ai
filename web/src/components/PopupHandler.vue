<template>
    <Popup v-for="popup in popups" :top="popup.top" :left="popup.left" :title="popup.t" :imageUrl="popup.i" :message="popup.m" @close-popup="onPopupClosed"></Popup>
</template>

<script setup lang="ts">
    import Popup from './Popup.vue';

    import { onMounted, ref } from 'vue';

    const onPopupClosed = (id: number) => {
        popups.value.splice(popups.value.findIndex(x => x.id == id), 1);
    };

    const maxTime = 5000;
    const maxPopups = 20;

    onMounted(() => {
        windowWidth = window.innerWidth;
        windowHeight = window.innerHeight;

        for (let i = 0; i < maxPopups; i++) { 
            setTimeout(() => {
                addPopup();
            }, Math.random() * maxTime);
        }
    });

    let windowWidth = 0;
    let windowHeight = 0;

    let id = 0;
    
    const popupMaxWidth  = 400;
    const popupMaxHeight = 600;

    const titles = [
        "WARNING!!!",
        "ERROR",
        "W adds zz",
        "Compiler error",
        "Uncaught exception"
    ];
    
    const messages = [
        "YOUR COMPUTER IS INFECTED!!!",
        "Please call 911...",
        "I have your credit card and phone number! :O",
        "You forgot a lambda expression on line 4142331.3"
    ];

    const images = [
        "/img1.jpg",
        "/img2.png",
        "/img3.jpg",
        "/img4.jpg",
        "/img5.jpg",
        "/img6.jpg",
        "/img7.jpg"
    ]

    interface IPopup {
        t: string,
        m: string,
        i: string,
        top: number,
        left: number,
        id: number
    };

    const addPopup = () => {
        popups.value.push({
            t: getTitle(),
            m: getMessage(),
            i: getImage(),
            top: getTop(),
            left: getLeft(),
            id: id++
        });

        return;
    };

    const getTitle = () => {
        return titles[Math.floor(Math.random() * titles.length)];
    };

    const getMessage = () => {
        return messages[Math.floor(Math.random() * messages.length)];
    };

    const getImage = () => {
        return images[Math.floor(Math.random() * images.length)];
    };

    const getTop = () => {
        return Math.random() * (windowHeight - popupMaxHeight);
    };

    const getLeft = () => {
        return Math.random() * (windowWidth - popupMaxWidth);
    };
    
    const popups = ref<IPopup[]>([]);
</script>