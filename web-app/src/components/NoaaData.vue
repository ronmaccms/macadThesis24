<template>
    <div class="noaa-weather">
      <h2>NOAA Weather Data</h2>
      <div v-if="loading">Loading data...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else>
        <pre>{{ weatherData }}</pre>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NoaaWeather',
    data() {
      return {
        weatherData: null,
        loading: true,
        error: null,
      };
    },
    async mounted() {
      try {
        const response = await fetch('https://api.weather.gov/');
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        this.weatherData = data;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  
  <style scoped>
  .noaa-weather {
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  </style>
  