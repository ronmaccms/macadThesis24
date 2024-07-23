<template>
  <div id="space">
    <AppSidebar @update-coordinates="handleUpdateCoordinates" />
    <div id="cont"></div>
  </div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { getDistance, getRhumbLineBearing } from 'geolib';
import AppSidebar from './AppSidebar.vue';

export default {
  name: 'SpaceMap',
  components: {
    AppSidebar,
  },
  data() {
    return {
      scene: null,
      renderer: null,
      camera: null,
      controls: null,
      MAT_BUILDING: null,
      latitude: 40.709193,
      longitude: -74.010387,
      radius: 1000,
      iR: null,
      nodes: {},
      ways: {},
      buildingMeshes: [],
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
    awake() {
      let cont = document.getElementById("cont");

      // Init scene
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0x222222);

      // Init Camera
      this.camera = new THREE.PerspectiveCamera(25, window.innerWidth / window.innerHeight, 1, 100);
      this.camera.position.set(8, 20, 25);

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
      this.addFlatTerrain();
    },
    update() {
      requestAnimationFrame(this.update);
      this.renderer.render(this.scene, this.camera);
      this.controls.update();
    },
    async getGeoJson() {
      const query = `
        [out:json];
        (
          node["building"](around:${this.radius},${this.latitude},${this.longitude});
          way["building"](around:${this.radius},${this.latitude},${this.longitude});
          relation["building"](around:${this.radius},${this.latitude},${this.longitude});
        );
        out body;
        >;
        out skel qt;
      `;
      const url = 'https://overpass-api.de/api/interpreter?data=' + encodeURIComponent(query);

      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        const data = await response.json();
        // console.log('GeoJSON data:', data);
        this.storeElements(data.elements);
        this.clearBuildings(); // Clear previous buildings
        this.loadBuildings(data);
      } catch (error) {
        console.error('Fetch error: ', error);
      }
    },
    storeElements(elements) {
      elements.forEach(el => {
        if (el.type === 'node') {
          this.nodes[el.id] = el;
        } else if (el.type === 'way') {
          this.ways[el.id] = el;
        }
      });
    },
    clearBuildings() {
      this.buildingMeshes.forEach(mesh => {
        this.scene.remove(mesh);
        mesh.geometry.dispose();
        mesh.material.dispose();
      });
      this.buildingMeshes = [];
    },
    loadBuildings(data) {
      let features = data.elements;
      // console.log('Number of features:', features.length);
      for (let i = 0; i < features.length; i++) {
        let fel = features[i];
        if (!fel.tags) continue;
        if (fel.tags['building']) {
          // Calculate the distance from the center to the building
          let buildingCenter;
          if (fel.type === 'node') {
            buildingCenter = [fel.lon, fel.lat];
          } else if (fel.type === 'way') {
            buildingCenter = this.calculateBuildingCenter(fel.nodes);
          } else if (fel.type === 'relation') {
            let nodes = this.extractNodesFromRelation(fel.members);
            buildingCenter = this.calculateBuildingCenter(nodes);
          }
          if (!buildingCenter) {
            console.error('Building center not found for element:', fel);
            continue;
          }
          let distance = getDistance(
            { latitude: buildingCenter[1], longitude: buildingCenter[0] },
            { latitude: this.latitude, longitude: this.longitude }
          );
          // console.log('Building center:', buildingCenter, 'Distance:', distance);
          // Only add the building if it is within the specified radius
          if (distance <= this.radius) {
            if (fel.type === 'relation') {
              this.addBuilding(this.extractNodesFromRelation(fel.members), fel.tags, fel.tags["building:levels"]);
            } else {
              this.addBuilding(fel.nodes, fel.tags, fel.tags["building:levels"]);
            }
          }
        }
      }
    },
    extractNodesFromRelation(members) {
      let nodes = [];
      members.forEach(member => {
        if (member.type === 'node') {
          nodes.push(member.ref);
        } else if (member.type === 'way' && this.ways[member.ref]) {
          nodes = nodes.concat(this.ways[member.ref].nodes);
        }
      });
      return nodes;
    },
    calculateBuildingCenter(nodes) {
      let validNodes = nodes.map(id => this.nodes[id]).filter(node => node && node.lat && node.lon);
      if (validNodes.length === 0) {
        return null;
      }
      let sumLat = 0;
      let sumLon = 0;
      for (let i = 0; i < validNodes.length; i++) {
        let node = validNodes[i];
        sumLat += node.lat;
        sumLon += node.lon;
      }
      return [sumLon / validNodes.length, sumLat / validNodes.length];
    },
    findNodeById(id) {
      return this.nodes[id] || null;
    },
    addBuilding(data, info, height = 1) {
      if (!data || data.length === 0) {
        console.error('Invalid building data:', data);
        return;
      }
      height = height ? height : 1;
      let points = data.map(id => this.nodes[id]).filter(node => node && node.lat && node.lon);
      if (points.length === 0) {
        console.error('No valid points for building');
        return;
      }
      let shape = this.genShape(points, [this.longitude, this.latitude]);
      let geometry = this.genGeometry(shape, {
        curveSegments: 1,
        depth: 0.05 * height,
        bevelEnabled: false
      });
      geometry.rotateX(Math.PI / 2);
      geometry.rotateZ(Math.PI);
      let mesh = new THREE.Mesh(geometry, this.MAT_BUILDING);
      this.scene.add(mesh);
      this.buildingMeshes.push(mesh); // Track the building mesh
      // console.log('Building added:', mesh);
    },
    genShape(points, center) {
      let shape = new THREE.Shape();
      for (let i = 0; i < points.length; i++) {
        let point = points[i];
        let elp = [point.lon, point.lat];
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
    addFlatTerrain() {
      const geometry = new THREE.PlaneGeometry(200, 200); // Increase the plane size
      const material = new THREE.MeshBasicMaterial({ color: 0x228B22, side: THREE.DoubleSide });
      const plane = new THREE.Mesh(geometry, material);
      plane.rotation.x = -Math.PI / 2;
      this.scene.add(plane);
    },
    handleUpdateCoordinates({ latitude, longitude, radius }) {
      if (latitude && longitude && radius) {
        this.latitude = parseFloat(latitude);
        this.longitude = parseFloat(longitude);
        this.radius = parseInt(radius);
        this.getGeoJson(); // Refresh the buildings based on the new coordinates and radius
      } else {
        console.error('Invalid coordinates or radius received');
      }
    }
  }
};
</script>

<style>
#space {
  display: flex;
  height: 100%;
}

#cont {
  position: relative;
  height: 100%;
  width: calc(100% - 200px); 
  margin-left: 200px;
}
</style>
