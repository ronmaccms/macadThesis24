<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="./web-app/src/assets/img/logo.jpg" alt="Logo" width="150">
  <h3 align="center">Simulation of Wind Flow Around Buildings Using Physics-Informed Neural Networks</h3>
  <p align="center" style="font-weight: bold;">IAAC: AI 2023-24<br>
    <a href="mailto:andres.roncal@students.iaac.net">Report Bug</a>
    ·
    <a href="mailto:andres.roncal@students.iaac.net">Request Feature</a>
  </p>
</div>

<h2>About The Project</h2>

<p>Project developed under the course IAAC: AI 2023-24 in <a href="https://iaac.net/">IAAC</a>.</p>

<h3>Overview</h3>

<p>This research project aims to develop a web application for simulating wind flow around buildings using Physics-Informed Neural Networks (PINNs). By leveraging data from Ladybug Tools, NOAA, and OpenWeatherMap, this project integrates real-time wind data and 3D building models to optimize building designs for enhanced pedestrian comfort and energy efficiency.</p>

<p>The project also integrates <strong>Three.js</strong> for rendering 3D models of buildings and <strong>Geolib</strong> for geographic calculations, which are utilized in the <code>space.vue</code> component.</p>

<h3>Objectives</h3>

<p>The primary objective of this research is to design and implement a web-based platform that utilizes PINNs to simulate wind flow and assess pedestrian comfort in urban environments. The platform will:</p>
<ul>
  <li>Collect and preprocess data from various sources, including historical wind data from NOAA, real-time wind conditions from OpenWeatherMap, and 3D building models from OpenStreetMap.</li>
  <li>Develop and train a PINN model using DeepXDE to simulate wind flow.</li>
  <li>Integrate the trained model into a Vue.js application for real-time user interaction and visualization.</li>
  <li>Provide insights and visualizations to architects and urban planners to enhance urban design and pedestrian comfort.</li>
  <li>Utilize Three.js and Geolib for rendering and geographic calculations respectively, as implemented in the <code>space.vue</code> component.</li>
</ul>

<h3>Significance</h3>

<p>Optimizing urban design for pedestrian comfort and energy efficiency has significant environmental and economic benefits. By reducing reliance on mechanical cooling systems and improving outdoor conditions, this project aims to:</p>
<ul>
  <li>Lower greenhouse gas emissions.</li>
  <li>Enhance the sustainability of urban environments.</li>
  <li>Reduce energy consumption and operational costs.</li>
  <li>Improve the overall quality of life in urban areas.</li>
</ul>

<h3>Methodology</h3>

<p>The development process includes the following stages:</p>
<ol>
  <li><strong>Planning and Data Collection</strong>: Set up the project repository and collect synthetic and real-time wind data.</li>
  <li><strong>PINN Model Development</strong>: Train and develop the PINN model using DeepXDE.</li>
  <li><strong>Backend Development</strong>: Implement the backend using Flask or FastAPI to handle data and integrate the PINN model.</li>
  <li><strong>Frontend Development</strong>: Develop the user interface using Vue.js for user input and visualization.</li>
  <li><strong>System Integration and Testing</strong>: Connect the frontend and backend, conduct thorough testing, and fix bugs.</li>
  <li><strong>Deployment and Documentation</strong>: Deploy the application on a cloud platform and document the project for future use.</li>
</ol>

<h3>Data Sources</h3>
<ul>
  <li><strong>Historical Wind Data</strong>: NOAA historical wind speed and direction data.</li>
  <li><strong>Real-Time Wind Data</strong>: OpenWeatherMap wind conditions.</li>
  <li><strong>3D Building Models</strong>: OpenStreetMap (OSM).</li>
  <li><strong>Synthetic Data</strong>: Ladybug Tools.</li>
</ul>

<h3>Project Scope</h3>

<p>This project focuses on developing a comprehensive platform that integrates geospatial data with advanced simulations. The scope includes:</p>
<ul>
  <li>Implementing a user-friendly web application for simulating wind flow.</li>
  <li>Providing real-time visualization and interaction capabilities.</li>
  <li>Supporting urban planners and architects with actionable insights for better urban design.</li>
</ul>

<h3>space.vue File Overview</h3>

<p>The <code>space.vue</code> component is a key part of the frontend development. It integrates Three.js for rendering 3D models of buildings and provides a user interface for inputting geographic coordinates and simulation parameters. Here’s an overview of its functionality:</p>
<ul>
  <li><strong>Components Used</strong>: <code>AppSidebar</code> for user input and controls.</li>
  <li><strong>Libraries</strong>: Three.js for 3D rendering, <code>geolib</code> for geographic calculations.</li>
  <li><strong>Functions</strong>:</li>
  <ul>
    <li><code>awake()</code>: Initializes the Three.js scene, camera, lights, and renderer.</li>
    <li><code>getGeoJson()</code>: Fetches building data from OpenStreetMap using Overpass API.</li>
    <li><code>loadBuildings()</code>: Processes and renders buildings based on fetched data.</li>
    <li><code>handleUpdateCoordinates()</code>: Updates coordinates and refreshes building data based on user input.</li>
  </ul>
</ul>

<h2>Setup Instructions</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Node.js (version X.X.X)</li>
  <li>npm (version X.X.X)</li>
</ul>

<h3>Clone the Repository</h3>
<pre><code>git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
</code></pre>

<h3>Install Dependencies</h3>
<pre><code>npm install
</code></pre>

<h3>Run the Project</h3>
<pre><code>npm run serve
</code></pre>

<h2>Project Structure</h2>

<ul>
  <li><code>src/</code>: Source files</li>
  <li><code>public/</code>: Public assets</li>
  <li><code>package.json</code>: Project configuration and dependencies</li>
  <li><code>README.md</code>: Project instructions and information</li>
</ul>

<h2>Team & Contacts</h2>

<h3>Student</h3>
<p><strong>Andres Roncal</strong></p>
<a href="https://www.linkedin.com/in/andres-roncal-1b148a132/" target="_blank">
    <img src="./web-app/src/assets/img/andres.png" alt="Andres Roncal" width="100">
</a>

<h3>Thesis Advisor</h3>
<p><strong>David Andres Leon</strong></p>
<a href="https://es.linkedin.com/in/davidandresleon" target="_blank">
    <img src="./web-app/src/assets/img/davidProfilePic.png" alt="David Andres Leon" width="100">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

</body>
</html>
