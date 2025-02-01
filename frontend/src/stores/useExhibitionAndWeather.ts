import { getExhibitionAndWeather } from '@/apis/exhibitionAndWeather'
import type {ExhibitionList} from "@/types/exhibitionAndWeather.ts";
import { defineStore } from 'pinia'
import { reactive, ref } from 'vue'

export const useExhibitionAndWeather = defineStore('exhibitionAndWeather', () => {
  const data = ref<ExhibitionList | null>(null)

  const fetchData = async () => {
    const res = await getExhibitionAndWeather()
    data.value = res.data
  }

  return {
    state: ref({ data }),
    actions: reactive({ fetchData }),
  }
})
