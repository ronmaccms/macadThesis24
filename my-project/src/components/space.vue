<template>
  <div id="cont"></div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { getDistance, getRhumbLineBearing } from 'geolib';

export default {
  name: 'ThreeJSMap',
  data() {
    return {
      scene: null,
      renderer: null,
      camera: null,
      controls: null,
      MAT_BUILDING: null,
      center: [-3.188822, 55.943686], // Center point
      radius: 1000, // Radius in meters
      iR: null,
      api: "https://gistcdn.githack.com/isjeffcom/a611e99aa888534f67cc2f6273a8d594/raw/9dbb086197c344c860217826c59d8a70d33dcb54/gistfile1.txt",
      accessToken: 'pk.eyJ1Ijoicm9ubWFjY21zIiwiYSI6ImNseXhoNTIwZjF3d3gyanB1a2VrNXUzaDQifQ.yqT0-g27iPtNGDp-4_GbdQ', // Replace with your Mapbox access token
    };
  },
  mounted() {
    this.awake();
    window.addEventListener('resize', this.onWindowResize, false);
    this.onWindowResize();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onWindowResize, false);
  },
  methods: {
    onWindowResize() {
      if (this.scene) {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
      }
    },
    async awake() {
      console.log("scene");
      let cont = document.getElementById("cont");

      // Init scene
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0x222222);

      // Init Camera
      this.camera = new THREE.PerspectiveCamera(25, window.innerWidth / window.innerHeight, 1, 100);
      this.camera.position.set(8, 4, 0);

      // Init group
      this.iR = new THREE.Group();
      this.iR.name = "Interactive Root";
      this.scene.add(this.iR);

      // Init Light
      let light0 = new THREE.AmbientLight(0xffffff, 0.5); // Increased intensity
      let light1 = new THREE.PointLight(0xffffff, 1); // Increased intensity
      light1.position.set(200, 90, 40);
      let light2 = new THREE.PointLight(0xffffff, 1); // Increased intensity
      light2.position.set(-200, 90, -40);
      this.scene.add(light0);
      this.scene.add(light1);
      this.scene.add(light2);

      // Add directional light for better shadows
      let directionalLight = new THREE.DirectionalLight(0xffffff, 1);
      directionalLight.position.set(50, 200, 100);
      directionalLight.castShadow = true;
      this.scene.add(directionalLight);

      let gridHelper = new THREE.GridHelper(60, 160, new THREE.Color(0x555555), new THREE.Color(0x333333));
      this.scene.add(gridHelper);

      // Init renderer
      this.renderer = new THREE.WebGLRenderer({ antialias: true });
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.renderer.setSize(window.innerWidth, window.innerHeight);

      cont.appendChild(this.renderer.domElement);

      this.controls = new OrbitControls(this.camera, this.renderer.domElement);
      this.controls.enableDamping = true;
      this.controls.dampingFactor = 0.25;
      this.controls.screenSpacePanning = false;
      this.controls.maxDistance = 800;

      this.controls.update();

      this.MAT_BUILDING = new THREE.MeshPhongMaterial();

      this.update();
      this.getGeoJson();
      try {
        await this.getTerrain();
      } catch (error) {
        console.error('Error fetching terrain data:', error);
      }
    },
    update() {
      requestAnimationFrame(this.update);
      this.renderer.render(this.scene, this.camera);
      this.controls.update();
    },
    async getGeoJson() {
      const res = await fetch(this.api);
      const data = await res.json();
      this.loadBuildings(data);
    },
    loadBuildings(data) {
      let features = data.features;
      for (let i = 0; i < features.length; i++) {
        let fel = features[i];
        if (!fel['properties']) return;
        if (fel.properties['building']) {
          // Calculate the distance from the center to the building
          let buildingCenter = this.calculateBuildingCenter(fel.geometry.coordinates[0]);
          let distance = getDistance(
            { latitude: buildingCenter[1], longitude: buildingCenter[0] },
            { latitude: this.center[1], longitude: this.center[0] }
          );
          
          // Only add the building if it is within the specified radius
          if (distance <= this.radius) {
            this.addBuilding(fel.geometry.coordinates, fel.properties, fel.properties["building:levels"]);
          }
        }
      }
    },
    calculateBuildingCenter(coordinates) {
      let sumLat = 0;
      let sumLon = 0;
      for (let i = 0; i < coordinates.length; i++) {
        sumLat += coordinates[i][1];
        sumLon += coordinates[i][0];
      }
      return [sumLon / coordinates.length, sumLat / coordinates.length];
    },
    addBuilding(data, info, height = 1) {
      height = height ? height : 1;
      for (let i = 0; i < data.length; i++) {
        let el = data[i];
        let shape = this.genShape(el, this.center);
        let geometry = this.genGeometry(shape, {
          curveSegments: 1,
          depth: 0.05 * height,
          bevelEnabled: false
        });
        geometry.rotateX(Math.PI / 2);
        geometry.rotateZ(Math.PI);
        let mesh = new THREE.Mesh(geometry, this.MAT_BUILDING);
        this.scene.add(mesh);
      }
    },
    genShape(points, center) {
      let shape = new THREE.Shape();
      for (let i = 0; i < points.length; i++) {
        let elp = points[i];
        elp = this.GPSRelativePosition(elp, center);
        if (i === 0) {
          shape.moveTo(elp[0], elp[1]);
        } else {
          shape.lineTo(elp[0], elp[1]);
        }
      }
      return shape;
    },
    genGeometry(shape, settings) {
      let geometry = new THREE.ExtrudeGeometry(shape, settings);
      geometry.computeBoundingBox();
      return geometry;
    },
    GPSRelativePosition(objPosi, centerPosi) {
      let dis = getDistance({ latitude: objPosi[1], longitude: objPosi[0] }, { latitude: centerPosi[1], longitude: centerPosi[0] });
      let bearing = getRhumbLineBearing({ latitude: objPosi[1], longitude: objPosi[0] }, { latitude: centerPosi[1], longitude: centerPosi[0] });
      let x = centerPosi[0] + (dis * Math.cos(bearing * Math.PI / 180));
      let y = centerPosi[1] + (dis * Math.sin(bearing * Math.PI / 180));
      return [-x / 100, y / 100];
    },
    async getTerrain() {
      const tileSize = 512;
      const zoom = 12; // Adjust zoom level as needed
      const { center, accessToken } = this;

      const [lng, lat] = center;
      const [x, y] = this.lngLatToTile(lng, lat, zoom);

      const url = `https://api.mapbox.com/v4/mapbox.terrain-rgb/${zoom}/${x}/${y}@2x.pngraw?access_token=${accessToken}`;

      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const blob = await response.blob();
        const imageBitmap = await createImageBitmap(blob);
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');

        canvas.width = tileSize;
        canvas.height = tileSize;
        context.drawImage(imageBitmap, 0, 0);

        const { data } = context.getImageData(0, 0, tileSize, tileSize);
        const geometry = new THREE.PlaneGeometry(tileSize, tileSize, tileSize - 1, tileSize - 1);

        for (let i = 0; i < geometry.attributes.position.count; i++) {
          const ix = i % tileSize;
          const iy = Math.floor(i / tileSize);
          const index = (iy * tileSize + ix) * 4;
          const [r, g, b] = [data[index], data[index + 1], data[index + 2]];
          const elevation = (r * 256 * 256 + g * 256 + b) * 0.1 - 10000; // Adjust the formula based on Mapbox's Terrain-RGB spec
          geometry.attributes.position.array[i * 3 + 2] = elevation / 100; // Adjust elevation scale as needed
        }

        geometry.computeVertexNormals();

        const material = new THREE.MeshPhongMaterial({ color: 0x888888, wireframe: false });
        const terrain = new THREE.Mesh(geometry, material);
        terrain.rotation.x = -Math.PI / 2;
        this.scene.add(terrain);
      } catch (error) {
        console.error('Error loading terrain data:', error);
      }
    },
    lngLatToTile(lng, lat, zoom) {
      const x = Math.floor((lng + 180) / 360 * Math.pow(2, zoom));
      const y = Math.floor((1 - Math.log(Math.tan(lat * Math.PI / 180) + 1 / Math.cos(lat * Math.PI / 180)) / Math.PI) / 2 * Math.pow(2, zoom));
      return [x, y];
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

#cont {
  position: absolute;
  height: 100%;
  width: 100%;
}
</style>
