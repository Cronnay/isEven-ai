<template>
    <div class="popup-container" :style="positionStyle">
        <div class="popup-header">
            <p>{{ props.title }}</p>
            <button :onclick="closePopup">X</button>
        </div>
        <div class="popup-content">
            <img v-if="props.imageUrl.length > 0" :src="props.imageUrl" alt="">
            <p>{{ props.message }}</p>
        </div>
        <div class="popup-buttons">
            <button :onclick="closePopup">OK</button>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { computed, type PropType } from 'vue';

    const props = defineProps({
        title: {
            required: false,
            type: Object as PropType<string>,
            default: ""
        },
        message: {
            required: false,
            type: Object as PropType<string>,
            default: ""
        },
        imageUrl: {
            required: false,
            type: Object as PropType<string>,
            default: ""
        },
        onExit: {
            required: false,
            type: Object as PropType<Function>,
            default: () => {}
        },
        id: {
            required: true,
            type: Object as PropType<number>,
            default: 0
        },
        top: {
            required: true,
            type: Object as PropType<number>
        },
        left: {
            required: true,
            type: Object as PropType<number>
        }
    });

    const positionStyle = computed(() => {
        return {
            'top': `${props.top}px`,
            'left': `${props.left}px`
        };
    });

    const emits = defineEmits(['close-popup']); // close-popup should parse the id to the parent!

    const closePopup = () => {
        emits("close-popup", props.id);
        props.onExit();
    };
</script>

<style>
    @font-face {
        font-family: byte;
        src: url('../assets/Orange.otf');
    }

    :root {
        --popup-primary-color: #C2C2C2;
        --popup-primary-hover-color: #dadada;
        --popup-primary-hover-color-1: #e8e5e5;
        --popup-shadow-color: black;
        --popup-header-color-1: #0754B0;
        --popup-header-color-2: #3D97D6;
        --popup-warning-color: rgb(248, 53, 53);
    }

    .popup-container {
        z-index: 100;

        position: fixed;
        display: flex;
        flex-direction: column;

        top: 150px;
        left: 150px;
        min-width: 300px;
        max-width: 400px;
        min-height: 150px;
        max-height: 600px;
        background-color: var(--popup-primary-color);
        border: 2px solid var(--popup-primary-hover-color);

        box-shadow: 5px 5px var(--popup-shadow-color);
    }

    .popup-header {
        display: flex;
        justify-content: space-between;

        background: linear-gradient(90deg, var(--popup-header-color-1), var(--popup-header-color-2));

        padding: 0.2em;
    }

    .popup-content {
        display: flex;
        flex-direction: column;
        gap: 15px;
        
        flex-grow: 1;
        padding: 20px;
    }

    .popup-buttons {
        display: flex;
        justify-content: center;
        margin: 10px 0;
    }

    .popup-content > p {
        text-align: center;
        color: var(--popup-warning-color);
    }
</style>

<style scoped>
    img {
        max-width: 300px;
    }

    button {
        background-color: var(--popup-primary-color);
        padding: 0 0.4em;
        font-family: byte;
    }
    
    button:hover {
        background-color: var(--popup-primary-hover-color);
    }

    p {
        font-family: byte;
    }

    .popup-buttons > button {
        background-color: var(--popup-primary-hover-color);
    }

    .popup-buttons > button:hover {
        background-color: var(--popup-primary-hover-color-1);
    }
</style>