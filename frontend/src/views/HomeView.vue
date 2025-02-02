<script setup lang="ts">

import WeatherChart from "@/components/WeatherChart.vue";
import {useExhibitionAndWeather} from "@/stores/useExhibitionAndWeather.ts";
import {onMounted} from "vue";

const store = useExhibitionAndWeather()

onMounted(store.actions.fetchData)

</script>

<template lang="pug">
  main
    h1 3-day weather forecast
    weather-chart(
      v-if="store.state.data"
      :weather="store.state.data.weather"
    )

    h1 Getting there

    a(href="https://www.google.com/maps?saddr=My+Location&daddr=32+Quincy+St,+Cambridge,+MA+02138" target="_blank")
      | Open directions in Google Maps

    h1 Exhibitions

    div
      code(v-if="store.state.data") {{ JSON.stringify(store.state.data.records, null, 2) }}
</template>
