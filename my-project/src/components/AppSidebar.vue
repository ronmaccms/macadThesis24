<!-- src/components/AppSidebar.vue -->
<template>
  <div class="sidebar">
    <h2>Controls</h2>
    <form @submit.prevent="updateCoordinates">
      <div>
        <label for="latitude">Latitude:</label>
        <input type="number" v-model="latitude" step="0.0001" required />
      </div>
      <div>
        <label for="longitude">Longitude:</label>
        <input type="number" v-model="longitude" step="0.0001" required />
      </div>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AppSidebar',
  data() {
    return {
      latitude: 55.9533,
      longitude: -3.1883,
    };
  },
  methods: {
    updateCoordinates() {
      this.$emit('update-coordinates', { latitude: this.latitude, longitude: this.longitude });
    },
  },
};
</script>

<style scoped>
.sidebar {
  background-color: #f4f4f4;
  padding: 10px;
  width: 200px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  overflow-y: auto;
}
form {
  display: flex;
  flex-direction: column;
}
form > div {
  margin-bottom: 10px;
}
button {
  align-self: flex-start;
}
</style>
