<template>
  <div class="sidebar">
    <h2>Controls</h2>
    <form @submit.prevent="updateCoordinates">
      <div>
        <label for="latitude">Latitude:</label>
        <input type="number" v-model="latitude" step="0.000001" required />
      </div>
      <div>
        <label for="longitude">Longitude:</label>
        <input type="number" v-model="longitude" step="0.000001" required />
      </div>
      <div>
        <label for="radius">Radius:</label>
        <select v-model="radius">
          <option value="500">500</option>
          <option value="1000">1000</option>
        </select>
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
      latitude: 40.709193,
      longitude: -74.010387,
      radius: 1000, // Default radius
    };
  },
  methods: {
    updateCoordinates() {
      this.$emit('update-coordinates', { latitude: this.latitude, longitude: this.longitude, radius: this.radius });
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
