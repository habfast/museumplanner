<script lang="ts" setup>
import type {ExhibitionRecord} from "@/types/exhibitionAndWeather.ts";

const props = defineProps<{
  exhibition: ExhibitionRecord
}>()
</script>

<template lang="pug">
v-card(variant="elevated" elevation="24")
  v-card-title
    a(:href="exhibition.url" target="_blank") {{ exhibition.title }}
  v-card-text
    div(v-if="exhibition.htmldescription" v-html="exhibition.htmldescription")
    div(v-else-if="exhibition.description") {{ exhibition.description }}
    div(v-else) Description missing


</template>
