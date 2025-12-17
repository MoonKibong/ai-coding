<template>
  <v-app>
    <v-app-bar color="primary" prominent>
      <v-app-bar-title>MediPredict Lite</v-app-bar-title>
    </v-app-bar>

    <v-main>
      <DiseaseRiskAnalysis />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import DiseaseRiskAnalysis from './components/DiseaseRiskAnalysis.vue'
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
