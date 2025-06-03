<template>
  <div id="app">
    <AppHeader />
    <FormOne />
    <FormTwo />
    <FormThree/>
    <FormFour/>
    <FormFive/>
    <AppFooter/>
    
  </div>
</template>

<script>
import AppHeader from './AppHeader.vue' // Обновлено
import FormOne from './FormOne.vue' // Обновлено
import FormTwo from './FormTwo.vue' // Обновлено
import FormThree from './FormThree.vue'
import FormFour from './FormFour.vue'
import FormFive from './FormFive.vue'
import AppFooter from './AppFooter.vue'

export default {
  name: 'HomePage',
  components: {
    AppHeader, // Обновлено
    FormOne, // Обновлено
    FormTwo,
    FormThree, // Обновлено
    FormFour,
    FormFive,
    AppFooter
  }
}
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
</style>