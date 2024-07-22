<template>
    <div id="space">
        <div id="cont"></div>
    </div>
</template>

<script>

import * as THREE from 'three'
import { MapControls } from 'three/examples/jsm/controls/OrbitControls'

export default {
    name: 'space',
    data() {
        return {
            scene: null,
            camera: null,
            renderer: null,
            controls: null,
            iR: null,
        }
    },
    mounted() {
        this.Awake()

        // When user resize window
        window.addEventListener('resize', this.onWindowResize, false);

        this.onWindowResize();
    },
    methods: {
        Awake() {
            let cont = document.getElementById('cont')

            // init scene
            this.scene = new THREE.Scene()
            this.scene.background = new THREE.Color(0x222222)

            // init camera
            this.camera = new THREE.PerspectiveCamera(25, window.innerWidth / window.innerHeight, 1, 100)
            this.camera.position.set(8, 4, 0)

            // init group
            this.iR = new THREE.Group()
            this.iR.name = "Interactive Root"
            this.scene.add(this.iR)

            // init lights
            let light0 = new THREE.AmbientLight(0xfafafa, 0.25);

            let light1 = new THREE.PointLight(0xfafafa, 4);
            light1.position.set(200, 90, 40);

            let light2 = new THREE.PointLight(0xfafafa, 4);
            light2.position.set(200, 90, -40);

            this.scene.add(light0);
            this.scene.add(light1);
            this.scene.add(light2);

            let gridHelper = new THREE.GridHelper(60, 150, new THREE.Color(0x555555), new THREE.Color(0x333333))
            this.scene.add(gridHelper)

            let geometry = new THREE.BoxGeometry(1, 1, 1)
            let material = new THREE.MeshPhongMaterial({ color: 0x00ff00 })
            let mesh = new THREE.Mesh(geometry, material)
            this.scene.add(mesh)

            // Init renderer
            this.renderer = new THREE.WebGLRenderer({ antialias: true });
            this.renderer.setPixelRatio(window.devicePixelRatio);
            this.renderer.setSize(window.innerWidth, window.innerHeight);

            cont.appendChild(this.renderer.domElement)

            // controls
            this.controls = new MapControls(this.camera, this.renderer.domElement);
            this.controls.enableDamping = true;
            this.controls.dampingFactor = 0.25;
            this.controls.screenSpacePanning = false;
            this.controls.maxDistance = 800;

            this.controls.update()

            this.Update()
        },
        onWindowResize() {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
        },
        Update() {
            requestAnimationFrame(this.Update)

            this.renderer.render(this.scene, this.camera)
            this.controls.update()
        }
    }
}
</script>

<style scoped>

</style>
