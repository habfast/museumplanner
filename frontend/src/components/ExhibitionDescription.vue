<script lang="ts" setup>
import type { ExhibitionRecord } from '@/types/exhibitionAndWeather.ts'

const props = defineProps<{
  exhibition: ExhibitionRecord
}>()
</script>

<template lang="pug">
v-card(variant="elevated" elevation="24" :image="exhibition.primaryimageurl" min-height="200" )
  v-card-title
    a(:href="exhibition.url" target="_blank") {{ exhibition.title }}
  v-card-text
    div(v-if="exhibition.htmldescription" v-html="exhibition.htmldescription")
    div(v-else-if="exhibition.description") {{ exhibition.description }}
    div(v-else) Description missing


</template>

<style scoped>
:deep(.v-card__image) {
  filter: opacity(0.3) blur(10px);
}
.v-card-title {
  text-shadow:
    #fff 0px 0px 5px,
    #fff 0px 0px 15px,
    #fff 0px 0px 25px;
}
</style>
