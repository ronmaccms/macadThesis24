<!-- PROJECT LOGO -->
<div align="center" style="background-color: #f39c12; color: white; padding: 10px; font-size: 20px; font-weight: bold;">
  WIP
</div>
<br />
<div align="center">
    <img src="./web-app/src/assets/img/logo-b.png" alt="Logo" width="200">
  <h3 align="center">Urban Wind Flow Modeling with PINNs</h3>
  <p align="center" style="font-weight: bold;">IAAC: AI 2023-24<br>
    <a href="mailto:andres.roncal@students.iaac.net" target="_blank">Report Bug</a>
    ·
    <a href="mailto:andres.roncal@students.iaac.net" target="_blank">Request Feature</a>
  </p>
  <!-- Add a link to the research paper -->
  <p target="_blank">
    <a href="https://docs.google.com/document/d/1bncJg6RVQCD4ev0K-jJk0_dyS2iHdrlpaUodtdLf9TM/edit" target="_blank">
      View Research Paper
    </a>
  </p>
</div>

<!-- GIF Section -->
<div align="center">
  <img src="./web-app/src/assets/doc/data/images/librariesinstalling.gif" alt="Project-GIF" width="500">
</div>

<h2>About The Project</h2>

<p>Project developed under the course IAAC: AI 2023-24 in <a href="https://iaac.net/">IAAC</a>.</p>

<h3>Overview</h3>

<p>Urban Wind Flow Modeling with PINNs focuses on developing a web-based platform that simulates wind flow in urban environments using real-time data and neural networks. By using data from NOAA, OpenWeatherMap, and OpenStreetMap, the project integrates real-time wind data and 3D building models to visualize pedestrian wind comfort and CFD simulations. The integration of Physics-Informed Neural Networks (PINNs) enables the platform to deliver precise and dynamic wind flow simulations efficiently.</p>

<h3>Objectives</h3>

<p>The project's goal is to create an open-source, web-based platform leveraging PINNs to simulate wind flow in urban environments. Designed as a collaborative tool, it aims to involve urban planners, architects, and designers to enhance its functionality. This project promotes sustainable urban development, reducing energy consumption and improving pedestrian comfort, while also fostering a community-driven approach to urban design innovation.</p>

<ul>
  <li>Collect and preprocess data from sources including NOAA, OpenWeatherMap, and OpenStreetMap using the Overpass API.</li>
  <li>Develop and train a PINN model using NVIDIA Modulus and PyTorch to simulate urban wind flow effectively.</li>
  <li>Integrate the trained model into a Vue.js application for real-time user interaction and visualization.</li>
  <li>Provide actionable insights for urban planners and architects to improve urban design and pedestrian comfort.</li>
  <li>Utilize Three.js and Geolib for rendering and geographic calculations, as implemented in the <code>space.vue</code> component.</li>
</ul>

<h3>Significance</h3>

<p>This project aims to enhance urban sustainability by:</p>
<ul>
  <li>Reducing reliance on mechanical cooling systems and improving natural ventilation in outdoor spaces.</li>
  <li>Promoting energy efficiency and reducing operational costs in urban environments.</li>
  <li>Providing an accessible platform for urban planners and researchers to model wind flow dynamics, informing better city design and layout decisions.</li>
</ul>

<h3>Methodology</h3>

<p>The project's development is divided into several phases:</p>
<ol>
  <li><strong>Setup and Requirements</strong>: Establish the computational environment using WSL for GPU access. Technologies chosen: Vue.js for the frontend, Flask/FastAPI for the backend, and NVIDIA Modulus with PyTorch for model development.</li>
  <li><strong>Planning and Research</strong>: Conduct extensive research on Physics-Informed Neural Networks (PINNs) and fluid dynamics, using tools like DeepXDE, NVIDIA Modulus, and PyTorch.</li>
  <li><strong>Repository and UI</strong>: Set up a structured GitHub repository for code, documentation, and data. Develop the Vue.js frontend for interaction with the wind flow models.</li>
  <li><strong>Model Integration and Testing</strong>: Integrate OpenStreetMap polygons into the training models and define domains/constraints using extracted building footprints.</li>
  <li><strong>Learning and Bootcamps</strong>: Invest over 80 hours in learning multiple techniques (PINNs, DeepONets, I-PINNs) to enhance the model's accuracy.</li>
  <li><strong>System Integration</strong>: Connect the frontend (Vue.js) with the backend (Flask/FastAPI) and integrate the trained PINN models.</li>
  <li><strong>Testing and Future Development</strong>: Iterate and refine the model integration, explore incorporating additional environmental factors, and expand user interactivity.</li>
</ol>

<h3>Data Sources</h3>
<ul>
  <li><strong>Real-Time Wind Data</strong>: OpenWeatherMap provides up-to-date wind conditions.</li>
  <li><strong>3D Building Models</strong>: OpenStreetMap (OSM) data using Overpass API offers detailed geographic information for urban modeling.</li>
</ul>

<h3>Equations and Models</h3>

<p>Key challenges involve integrating OpenWeatherMap data and the Navier-Stokes equations into the neural network model to enhance simulation precision. The use of NVIDIA Modulus and PyTorch allows the development of neural networks capable of predicting fluid velocity, pressure, and diffusivity, which are essential for modeling wind flow in urban environments.</p>

<!-- GIF Section -->
<div align="center">
  <img src="./web-app/src/assets/doc/data/images/lala2.gif" alt="sim-gif" width="600">
</div>

<h3>Frontend Development</h3>

<p>The frontend is built using Vue.js, with Three.js for 3D rendering and Geolib for geographic calculations. This interface enables users to input geographical data, run simulations, and receive visual feedback on urban wind flow dynamics.</p>

<h3>System Integration</h3>

<p>The integration phase connected the Vue.js frontend with the Flask/FastAPI backend and the PINN model. This allows for real-time data processing, user interaction, and dynamic visualization of wind flow.</p>

<h3>Learning and Development with NVIDIA Modulus Sym</h3>

<p>During the project's development, I focused on learning how to leverage NVIDIA’s <code>modulus.sym</code> for building Physics-Informed Neural Networks. Model training sessions, conducted on my NVIDIA GPU using WSL, often take up to 12 hours. This setup efficiently utilizes GPU resources for complex simulations.</p>

<div align="center">
    <img src="./web-app/src/assets/doc/data/images/2d-heat-sink-with-fins.png" alt="sink-heat" width="500">
</div>

<p>The following techniques were explored:</p> 
<ul> 
    <li><strong>Physics-Informed Neural Networks (PINNs)</strong>: Integrating physical laws into neural networks for precise simulation results.</li> 
    <li><strong>Inverse PINNs (I-PINNs)</strong>: Tackling inverse problems to fine-tune model parameters based on observed data.</li> 
    <li><strong>Deep Neural Operators (DeepONets)</strong>: Mapping functions for solving complex simulations like fluid dynamics.</li> 
    <li><strong>NVIDIA Modulus</strong>: Utilizing NVIDIA’s Modulus framework for CFD and structural analysis simulations.</li> 
</ul>

<div align="center">
    <img src="./web-app/src/assets/doc/data/images/Screenshot 2024-08-27 092922.png" alt="sink-heat-2" width="500">
</div>
<br>
<div align="center">
    <img src="./web-app/src/assets/doc/data/images/Screenshot 2024-08-27 093741.png" alt="sink-heat-2" width="400">
</div>

<h3>Example of Implementation</h3>

<p>This project implements a 2D simulation using DeepONets, integrating key equations like the Navier-Stokes and Advection-Diffusion equations to model fluid dynamics. Utilizing <code>modulus.sym</code>, neural networks predict fluid properties such as velocity and pressure in an urban environment.</p>

<h3>Setting Up and Using WSL for CUDA-Enabled GPU Computing</h3>

<p>To fully utilize the NVIDIA GPU on my system, I set up a WSL environment with Ubuntu 20.04, allowing the execution of Linux-based software and CUDA for GPU acceleration.</p>

<div align="center">
    <img src="./web-app/src/assets/doc/data/images/gpu2.png" alt="gpu2" width="500">
</div>

<h3>Current Status and Future Work</h3>

<p>The platform's front and back ends are integrated, allowing for real-time simulations. However, final model integration for pedestrian wind assessment is ongoing. Future work includes enhancing computational efficiency, exploring the addition of environmental factors like temperature and humidity, and expanding the user interface for broader scenario comparisons.</p>

<h2>Team & Contacts</h2>

<h3>Contributor</h3>
<p><strong>Andres Roncal</strong></p>
<a href="https://www.linkedin.com/in/andres-roncal-1b148a132/" target="_blank">
    <img src="./web-app/src/assets/img/andres-pic.jpg" alt="Andres" width="100">
</a>

<h3>Thesis Advisor</h3>
<p><strong>David Andres Leon</strong></p>
<a href="https://es.linkedin.com/in/davidandresleon" target="_blank">
    <img src="./web-app/src/assets/img/davidProfilePic.png" alt="David Andres Leon" width="100">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

</body>
</html>
