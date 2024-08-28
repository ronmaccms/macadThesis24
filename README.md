<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="./web-app/src/assets/logo.jpg" alt="Logo" width="200">
  <h3 align="center">Urban Wind Flow Modeling with PINNs</h3>
  <p align="center" style="font-weight: bold;">IAAC: AI 2023-24<br>
    <a href="mailto:andres.roncal@students.iaac.net">Report Bug</a>
    ·
    <a href="mailto:andres.roncal@students.iaac.net">Request Feature</a>
  </p>
</div>

<!-- GIF Section -->
<div align="center">
  <img src="./data/images/librariesinstalling.gif" alt="Project-GIF" width="500">
</div>

<h2>About The Project</h2>

<p>Project developed under the course IAAC: AI 2023-24 in <a href="https://iaac.net/">IAAC</a>.</p>

<h3>Overview</h3>

<p>Urban Wind Flow Modeling with PINNs focuses on developing a web-based platform that simulates wind flow in urban environments using real-time data and neural networks. By using data from NOAA, OpenWeatherMap, and OpenStreetMap, the project integrates real-time wind data and 3D building models to visualize pedestrian wind comfort and cfd simulations.</p>

<h3>Objectives</h3>

<p>The projects aim is to create an open-source, web-based platform that leverages Physics-Informed Neural Networks to simulate wind flow in urban environments. Designed to be a collaborative tool, inviting contributions from urban planners, architects, and designers to enhance its functionality and adaptability. The project aims to promote sustainable urban development, reducing energy consumption and improving pedestrian comfort. This initiative not only supports environmental sustainability but also fosters a community-driven approach to urban design innovation.</p>

<ul>
  <li>Collect and preprocess data from various sources, including historical wind data from NOAA, real-time wind conditions from OpenWeatherMap, and 3D building models from OpenStreetMap using the Overpass API.</li>
  <li>Develop and train a PINN model using NVIDIA Modulus and PyTorch to simulate wind flow.</li>
  <li>Integrate the trained model into a Vue.js application for real-time user interaction and visualization.</li>
  <li>Provide insights and visualizations to urban planners and architects to enhance urban design and pedestrian comfort.</li>
  <li>Utilize Three.js and Geolib for rendering and geographic calculations respectively, as implemented in the <code>space.vue</code> component.</li>
</ul>

<h3>Significance</h3>

<p>By reducing reliance on mechanical cooling systems and improving outdoor conditions, this project aims to:</p>
<ul>
  <li>Enhance the sustainability of urban environments.</li>
  <li>Reduce energy consumption and operational costs.</li>
</ul>

<h3>Methodology</h3>

<p>Phases:</p>
<ol>
  <li><strong>Planning</strong>: Set repository and collect data from NOAA, OpenWeatherMap, and OpenStreetMap for model development.</li>
  <li><strong>PINN Model Development</strong>: Utilize PyTorch for initial testing and develop the PINN model using NVIDIA’s Modulus framework.</li>
  <li><strong>Backend Development</strong>: Implement the backend using Flask or FastAPI, creating API endpoints to manage data and run simulations.</li>
  <li><strong>Frontend Development</strong>: Develop the user interface using Vue.js, with Three.js for 3D rendering and Geolib for geographic calculations.</li>
  <li><strong>System Integration and Testing</strong>: Connect the frontend, backend, and PINN model, followed by rigorous testing to ensure accuracy and reliability.</li>
  <li><strong>Deployment and Documentation</strong>: Deploy the application on a cloud platform and document the project for future reference.</li>
</ol>

<h3>Data Sources</h3>
<ul>
<!--   <li><strong>Historical Wind Data</strong>: NOAA historical wind speed and direction data.</li> -->
  <li><strong>Real-Time Wind Data</strong>: OpenWeatherMap wind conditions.</li>
  <li><strong>3D Building Models</strong>: OpenStreetMap (OSM) data using Overpass API.</li>
<!--   <li><strong>Synthetic Data</strong>: Ladybug Tools for additional modeling.</li> -->
</ul>

<h3>Equations and Models</h3>

<p>The challenges include the ongoing integration of the OpenWeatherMap data and Navier-Stokes equations into the neural network model to enhance the precision of simulations.</p>

<!-- GIF Section -->
<div align="center">
  <img src="./data/images/lala2.gif" alt="sim-gif" width="600">
</div>

<h3>Frontend Development</h3>

<p>The frontend is developed using Vue.js, with Three.js handling the 3D rendering and Geolib managing geographic calculations. This interface allows users to input geographical data and run wind flow simulations, providing immediate visual feedback.</p>

<h3>System Integration</h3>

<p>The system integration phase involved connecting the backend, frontend, and PINN model.</p>

<h3>Learning and Development with NVIDIA Modulus Sym</h3>

<p>As part of the development process for this project, I am actively learning how to leverage NVIDIA’s <code>modulus.sym</code> for building PINNs. The training sessions required for developing accurate models often take up to 12 hours, and they are conducted on my GPU using a WSL. This setup allows me to fully utilize the computational power of my NVIDIA GPU while working in a Linux environment.</p>

<div align="center">
    <img src="./data/images/2d-heat-sink-with-fins.png" alt="sink-heat" width="500">
</div>

<p>I am testing several techniques:</p> 
<ul> 
    <li><strong>Physics-Informed Neural Networks (PINNs)</strong>: Learning how to integrate physical laws directly into neural networks for accurate simulation results.
    </li> 
    <li><strong>Inverse PINNs (I-PINNs)</strong>: Tackling inverse problems to optimize and fine-tune model parameters based on observed data.
    </li> 
    <li><strong>Deep Neural Operators (DeepONets)</strong>: Developing skills in mapping functions to functions, for solving complex simulations like fluid dynamics.
    </li> 
    <li><strong>NVIDIA Modulus</strong>: Applying these concepts using NVIDIA’s Modulus framework, specifically in Computational Fluid Dynamics (CFD) and structural analysis.
    </li> 
</ul>

<div align="center">
    <img src="./data/images/Screenshot 2024-08-27 092922.png" alt="sink-heat-2" width="500">
</div>
<br>
<div align="center">
    <img src="./data/images/Screenshot 2024-08-27 093741.png" alt="sink-heat-2" width="400">
</div>


<h3>Example of Implementation</h3>

<p>2D simulation in Section 3: Deep Neural Operator (DeepONet). This simulation integrates key equations such as the Navier-Stokes and Advection-Diffusion equations to model fluid dynamics. By utilizing <code>modulus.sym</code>, I have been able to develop neural networks that predict fluid velocity, pressure, and diffusivity, for simulating wind flow in urban environments.</p>

<h3>Setting Up and Using WSL for CUDA-Enabled GPU Computing</h3>

<p>To fully utilize the NVIDIA GPU on my system, I have set up a WSL environment with Ubuntu 20.04, which allows me to run Linux-based software while taking advantage of CUDA for GPU. Below are the steps to replicate this setup:</p>

<div align="center">
    <img src="./data/images/" alt="gpu" width="500">
</div>

<h3>Step 1: Install WSL and Ubuntu 20.04</h3>
<ol>
  <li><strong>Enable WSL</strong>: Open PowerShell as an Administrator and run:
  </li>
  <li><strong>Install Ubuntu 20.04</strong>: If you need a specific version, such as Ubuntu 20.04
  </li>
  <li><strong>Set Up WSL</strong>: Once Ubuntu is installed, open it from your Start menu and follow the on-screen instructions to complete the setup.</li>
</ol>

<h3>Step 2: Install NVIDIA CUDA Toolkit</h3>

<h3>Step 4: Install NVIDIA Modulus and Other Dependencies</h3>

<h3>Running Your First Simulation</h3>
<p>After setting up your environment, you can run your first PINN simulation by navigating to the project directory and executing the following command:</p>
<pre><code>python3 your_simulation_script.py</code></pre>

<p>This command will start the simulation, utilizing your NVIDIA GPU to accelerate the computations. Depending on the complexity of the model, training can take several hours.</p>

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
<!-- <style>
  pre code {
    padding: 10px;
    margin: 5px 0;
    display: block;
    overflow-x: auto;
  }
</style> -->

</html>
