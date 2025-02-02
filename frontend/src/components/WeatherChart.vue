<script lang="ts" setup>
import type { Weather } from '@/types/exhibitionAndWeather.ts'
import { ref } from 'vue'

const props = defineProps<{
  weather: Weather
}>()

const chartOptions = ref({
  chart: {
    id: 'weather-chart',
  },
  xaxis: {
    type: 'category',
    stepSize: 6,
    categories: props.weather.timestamps.map((ts) => {
      const d = new Date(ts * 1000)
      if (d.getUTCHours() === 0) return `${d.getDay()}/${d.getMonth() + 1} ${d.getUTCHours()}h00`
      if (d.getUTCHours() % 6 === 0) return `${d.getUTCHours()}h00`
      return ''
    }),
    labels: {
      hideOverlappingLabels: true,
      rotate: -45,
    },
  },
  yaxis: {
    labels: {
      formatter: (value: number) => {
        return value.toFixed(2)
      },
    },
  },
})
const series = [
  {
    name: 'Temperature',
    data: props.weather.temperature,
    type: 'line',
  },
  {
    name: 'Rain',
    data: props.weather.rain,
    type: 'bar',
  },
]
</script>

<template lang="pug">
apexchart(
  width="100%"
  height="300"
  :options="chartOptions"
  :series="series"
)
</template>
