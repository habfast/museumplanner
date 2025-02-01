export type Weather = {
  temperature: number[]
  rain: number[]
}

export type Image = {
  date?: string | null
  copyright?: string | null
  imageid: number
  idsid: number
  format: string
  caption?: string | null
  description?: string | null
  technique?: string | null
  renditionnumber: string
  displayorder: number
  baseimageurl: string
  alttext?: string | null
  width: number
  iiifbaseuri: string
  height: number
}

export type Poster = {
  imageurl: string
  caption?: string | null
}

export type ExhibitionRecord = {
  shortdescription?: string | null
  htmldescription?: string | null
  images: Image[]
  begindate: string
  color?: string | null
  description?: string | null
  exhibitionid: number
  title: string
  primaryimageurl?: string | null
  temporalorder: number
  url: string
  textiledescription?: string | null
  enddate?: string | null
  id: number
  lastupdate: string
  poster?: Poster | null
}

export type Info = {
  totalrecordsperquery: number
  totalrecords: number
  pages: number
  page: number
  next: string
  responsetime: string
}

export type ExhibitionList = {
  info: Info
  records: ExhibitionRecord[]
  weather: Weather
}
