<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="./web-app/src/assets/logo.jpg" alt="Logo" width="150">
  <h3 align="center">Urban Wind Flow Modeling with Physics-Informed Neural Networks (PINNs)</h3>
  <p align="center" style="font-weight: bold;">IAAC: AI 2023-24<br>
    <a href="mailto:andres.roncal@students.iaac.net">Report Bug</a>
    ·
    <a href="mailto:andres.roncal@students.iaac.net">Request Feature</a>
  </p>
</div>

<h2>About The Project</h2>

<p>Project developed under the course IAAC: AI 2023-24 in <a href="https://iaac.net/">IAAC</a>.</p>

<h3>Overview</h3>

<p>Urban Wind Flow Modeling with PINNs focuses on developing a web-based platform that simulates wind flow in urban environments using real-time data and advanced neural networks. By leveraging data from NOAA, OpenWeatherMap, and OpenStreetMap, the project integrates real-time wind data and 3D building models to optimize urban design for pedestrian comfort and energy efficiency.</p>

<h3>Objectives</h3>

<p>The primary objective of this research is to create an open-source, web-based platform that leverages Physics-Informed Neural Networks (PINNs) to simulate wind flow in urban environments. This platform is designed to be a collaborative tool, inviting contributions from urban planners, architects, and designers to enhance its functionality and adaptability. By providing real-time insights into wind flow patterns, the project aims to promote sustainable urban development, reducing energy consumption and improving pedestrian comfort. This initiative not only supports environmental sustainability but also fosters a community-driven approach to urban design innovation.</p>

<ul>
  <li>Collect and preprocess data from various sources, including historical wind data from NOAA, real-time wind conditions from OpenWeatherMap, and 3D building models from OpenStreetMap using the Overpass API.</li>
  <li>Develop and train a PINN model using NVIDIA Modulus and PyTorch to simulate wind flow.</li>
  <li>Integrate the trained model into a Vue.js application for real-time user interaction and visualization.</li>
  <li>Provide insights and visualizations to urban planners and architects to enhance urban design and pedestrian comfort.</li>
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

<p>The development process is structured into several phases:</p>
<ol>
  <li><strong>Planning and Data Collection</strong>: Establish the project repository and collect data from NOAA, OpenWeatherMap, and OpenStreetMap for model development.</li>
  <li><strong>PINN Model Development</strong>: Utilize PyTorch for initial testing and develop the PINN model using NVIDIA’s Modulus framework.</li>
  <li><strong>Backend Development</strong>: Implement the backend using Flask or FastAPI, creating API endpoints to manage data and run simulations.</li>
  <li><strong>Frontend Development</strong>: Develop the user interface using Vue.js, with Three.js for 3D rendering and Geolib for geographic calculations.</li>
  <li><strong>System Integration and Testing</strong>: Connect the frontend, backend, and PINN model, followed by rigorous testing to ensure accuracy and reliability.</li>
  <li><strong>Deployment and Documentation</strong>: Deploy the application on a cloud platform and document the project for future reference.</li>
</ol>

<h3>Data Sources</h3>
<ul>
  <li><strong>Historical Wind Data</strong>: NOAA historical wind speed and direction data.</li>
  <li><strong>Real-Time Wind Data</strong>: OpenWeatherMap wind conditions.</li>
  <li><strong>3D Building Models</strong>: OpenStreetMap (OSM) data using Overpass API.</li>
  <li><strong>Synthetic Data</strong>: Ladybug Tools for additional modeling.</li>
</ul>

<h3>Equations and Model Development</h3>

<p>The Navier-Stokes equations are central to the simulation of wind flow in this project, integrating real-time data from OpenWeatherMap to refine the model’s accuracy. Challenges include the ongoing integration of this data into the neural network model to enhance the precision of simulations.</p>

<h3>Frontend Development</h3>

<p>The frontend is developed using Vue.js, with Three.js handling the 3D rendering and Geolib managing geographic calculations. This interface allows users to input geographical data and run wind flow simulations, providing immediate visual feedback.</p>

<h3>System Integration and Testing</h3>

<p>The system integration phase involved connecting the backend, frontend, and PINN model. This phase included thorough testing to ensure the accuracy of the simulations and the reliability of the web platform.</p>

<h3>Conclusion and Future Work</h3>

<p>This open-source project serves as a collaborative tool for urban planners, offering insights into wind flow patterns. Moving forward, the aim is to expand the model’s capabilities, including incorporating additional environmental factors and improving the user interface for broader applications.</p>

<h2>Setup Instructions</h2>

<h3>Clone the Repository</h3>
<pre><code>git clone https://github.com/your-repo-url.git</code></pre>

<h3>Install Dependencies</h3>
<pre><code>npm install</code></pre>

<h3>Run the Project</h3>
<pre><code>npm run serve</code></pre>

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
