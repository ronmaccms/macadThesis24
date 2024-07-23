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

    <div class="weather-data" v-if="typeof weather.main !== 'undefined'">
      <div class="location"> {{ weather.name }}, {{ weather.sys.country }} </div>
      <div class="temp"> {{ Math.round(weather.main.temp) }} °C</div>
      <div class="weather"> {{ weather.weather[0].main }} </div>
      <div class="wind">
        <div class="wind-speed">Wind Speed: {{ weather.wind.speed }} m/s</div>
        <div class="wind-direction">Wind Direction: {{ windDirection(weather.wind.deg) }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppSidebar',
  props: {
    weather: Object,
  },
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
    windDirection(deg) {
      const directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"];
      const index = Math.round(deg / 22.5) % 16;
      return directions[index];
    }
  }
};
</script>
