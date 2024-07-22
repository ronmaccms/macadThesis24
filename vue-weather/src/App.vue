<template>
  <div id="app">
    <main>
      <div class="search-box">
        <input type="text" 
               class="search-bar" 
               placeholder="Search..."
               v-model="query"
               @keypress="fetchWeather"
        />
      </div>

      <div class="weather-wrap" v-if="typeof weather.main != 'undefined'">
        <div class="location-box">
          <div class="location"> {{ weather.name }}, {{  weather.sys.country }} </div>
          <div class="date"> {{ dateBuilder() }} </div>
        </div>
        <div class="weather-box">
          <div class="temp"> {{ Math.round(weather.main.temp) }} °C</div>
          <div class="weather"> {{ weather.weather[0].main }} </div>
          <div class="wind">
            <div class="wind-speed">Wind Speed: {{ weather.wind.speed }} m/s</div>
            <div class="wind-direction">Wind Direction: {{ windDirection(weather.wind.deg) }}</div>
          </div>
        </div>
      </div>

      <div id="cesiumContainer" ref="cesiumContainer" class="cesium-container"></div>
    </main>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import * as Cesium from 'cesium/Cesium';
import 'cesium/Widgets/widgets.css';

Cesium.Ion.defaultAccessToken = 'YOUR_CESIUM_ACCESS_TOKEN'; // Replace with your Cesium access token

export default defineComponent({
  name: 'App',
  data () {
    return {
      api_key: '4470f6319555f06d113186032c495792',
      url_base: 'https://api.openweathermap.org/data/2.5/',
      query: '',
      weather: {},
      viewer: null
    }
  },
  methods: {
    fetchWeather (e) {
      if (e.key === "Enter") {
        fetch(`${this.url_base}weather?q=${this.query}&units=metric&appid=${this.api_key}`)
          .then(res => res.json())
          .then(this.setResults);
      }
    },
    setResults (results) {
      this.weather = results;
      if (this.viewer) {
        const longitude = this.weather.coord.lon;
        const latitude = this.weather.coord.lat;
        const height = 1500;

        this.viewer.camera.flyTo({
          destination: Cesium.Cartesian3.fromDegrees(longitude, latitude, height)
        });
      }
    },
    dateBuilder () {
      let d = new Date();
      let months = ["January", "February", "March", "April", "May", "June", "July", 
      "August", "September", "October", "November", "December"];
      let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

      let day = days[d.getDay()];
      let date = d.getDate();
      let month = months[d.getMonth()];
      let year = d.getFullYear();

      return `${day} ${date} ${month} ${year}`;
    },
    windDirection (deg) {
      const directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"];
      const index = Math.round(deg / 22.5) % 16;
      return directions[index];
    },
    initializeCesium() {
      this.viewer = new Cesium.Viewer(this.$refs.cesiumContainer, {
        terrainProvider: Cesium.createWorldTerrain()
      });

      this.viewer.scene.primitives.add(Cesium.createOsmBuildings());
    }
  },
  mounted() {
    this.initializeCesium();
  }
});
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'montserrat', sans-serif;
}

#app {
  background-image: url('./assets/cold-bg.jpg');
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}

main {
  min-height: 100vh;
  padding: 25px;

  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.75));
}

.search-box {
  width: 100vh;
  padding: 25px;
}

.search-box .search-bar {
  display: block;
  width: 100%;
  padding: 15px;

  color: #313131;
  font-size: 20px;
  
  appearance: none;
  border: none;
  outline: none;
  background: none;

  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 0px 16px 0px 16px;
  transition: 0.4s;
}

.search-box .search-bar:focus {
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.75);
  border-radius: 16px 0px 16px 0px;
}

.location-box .location {
  color: #FFF;
  font-size: 32px;
  font-weight: 500;
  text-align: center;
  text-shadow: 1px 3px rgba(0, 0, 0, 0.25);
}

.location-box .date {
  color: #FFF;
  font-size: 20px;
  font-weight: 300;
  text-align: center;
  font-style: italic;
}

.weather-box {
  text-align: center;
}

.weather-box .temp {
  display: inline-block;
  padding: 10px 25px;
  color: #FFF;
  font-size: 102px;
  font-weight: 900;

  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  margin: 30px 0px;

  box-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}

.weather-box .weather {
  color: #FFF;
  font-size: 48px;
  font-weight: 700;
  font-style: italic;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}

.weather-box .wind {
  margin-top: 20px;
}

.weather-box .wind-speed,
.weather-box .wind-direction {
  color: #FFF;
  font-size: 24px;
  font-weight: 500;
  text-shadow: 2px 4px rgba(0, 0, 0, 0.25);
}

.cesium-container {
  width: 100%;
  height: 50vh;
  margin-top: 20px;
}
</style>
