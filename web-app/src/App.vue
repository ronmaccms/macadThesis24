<template>
  <div id="app">
    <AppHeader />
    <Space />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue';
import Space from './components/space.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    Space
  }
};
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>
