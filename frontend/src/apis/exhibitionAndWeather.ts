import type {ExhibitionList} from "@/types/exhibitionAndWeather.ts";
import http from '@/utils/http'

const BASE_URL = '/api/exhibitions'

export const getExhibitionAndWeather = () => http.get<ExhibitionList>(BASE_URL)
