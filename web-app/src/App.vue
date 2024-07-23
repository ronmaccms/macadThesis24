<template>
  <div id="app">
    <Space />
  </div>
</template>

<script>
import Space from './components/space.vue';

export default {
  name: 'App',
  components: {
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
