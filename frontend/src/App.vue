

<script setup>
import TheHeader from './layouts/TheHeaders.vue'
import TheView from './layouts/TheView.vue'
</script>

<template>
    <TheHeader></TheHeader>
    <TheView></TheView>
    <router-view></router-view>
</template>

<style>
li {
  list-style-type: none; /* 마커를 없앱니다. */
  /* 추가적인 스타일링을 원하면 여기에 추가합니다. */
}
</style>