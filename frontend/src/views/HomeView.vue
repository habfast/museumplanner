<script setup lang="ts">

import {useExhibitionAndWeather} from "@/stores/useExhibitionAndWeather.ts";
import {onMounted} from "vue";

const store = useExhibitionAndWeather()

onMounted(store.actions.fetchData)

</script>

<template lang="pug">
  main
    div Hello world
    div {{ store.state.data }}
</template>
