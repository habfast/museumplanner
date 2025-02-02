<script setup lang="ts">

import ExhibitionDescription from "@/components/ExhibitionDescription.vue";
import HelpText from "@/components/HelpText.vue";
import WeatherChart from "@/components/WeatherChart.vue";
import {useExhibitionAndWeather} from "@/stores/useExhibitionAndWeather.ts";
import {onMounted} from "vue";

const store = useExhibitionAndWeather()

onMounted(store.actions.fetchData)

</script>

<template lang="pug">
  v-row.pa-12
    v-col(cols="12")
      div.text-h3 Welcome to Art Museum Planner
      v-card.mt-3(variant="tonal" elevation="0" color="primary" )
        v-card-text
          help-text
    v-col(cols="6")
      v-card(variant="tonal" elevation="0" color="secondary" )
        v-card-title 3-day weather forecast
        v-card-text
          weather-chart(
            v-if="store.state.data"
            :weather="store.state.data.weather"
          )

    v-col(cols="6")
      v-card(variant="tonal" elevation="0" color="secondary" )
        v-card-title Getting there
        v-card-actions
          a(href="https://www.google.com/maps?saddr=My+Location&daddr=32+Quincy+St,+Cambridge,+MA+02138" target="_blank")
            | Open directions in Google Maps

    v-col(cols="12")
      div.d-flex
        span.text-h3 Exhibitions
        v-text-field.ml-3(
          label="Search"
          variant="underlined"
          v-model="store.state.searchText"
        )

    v-col(cols="6" v-if="store.state.data" v-for="exhibition of store.state.data.records")
      exhibition-description(:exhibition="exhibition")
    v-col.text-center(cols="12")
      v-btn(
        v-if="store.state.data && store.state.data.info.next"
        @click="store.state.page = store.state.page + 1"
        color="primary"
      ) Load more
      span.text-h6(v-else) Nothing else to load
</template>
