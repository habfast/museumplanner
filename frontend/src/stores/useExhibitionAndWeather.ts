import { getExhibitionAndWeather } from '@/apis/exhibitionAndWeather'
import type {ExhibitionList} from "@/types/exhibitionAndWeather.ts";
import {debounce} from "lodash";
import { defineStore } from 'pinia'
import {computed, reactive, ref, watch} from 'vue'

export const useExhibitionAndWeather = defineStore('exhibitionAndWeather', () => {
  const data = ref<ExhibitionList | null>(null)
  const searchText = ref("")
  const page = ref(0)

  const searchParams = computed(() => {
    const res = {} as Record<string, string>
    if (searchText.value) res.q = `title:${searchText.value}`
    if (page.value) res.page = `${page.value + 1}`
    return res
  })

  const fetchData = async () => {
    const res = await getExhibitionAndWeather(searchParams.value)
    if (page.value && data.value) data.value.records = [...data.value.records, ...res.data.records]
    else data.value = res.data
  }

  watch(page, fetchData)
  watch(searchText, debounce(() => {
    page.value = 0
    return fetchData()
  }, 500))

  return {
    state: ref({ data, searchText, page, searchParams }),
    actions: reactive({ fetchData }),
  }
})
