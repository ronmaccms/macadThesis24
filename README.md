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

<h3>Learning and Development with NVIDIA Modulus Sym</h3>

<p>As part of the development process for this project, I am actively learning how to leverage NVIDIA’s <code>modulus.sym</code> for building Physics-Informed Neural Networks (PINNs). The training sessions required for developing accurate models often take up to 12 hours, and they are conducted on my GPU using a WSL (Windows Subsystem for Linux) environment. This setup allows me to fully utilize the computational power of my NVIDIA GPU while working in a Linux environment.</p>

<h3>Bootcamp Participation and Advanced Learning</h3>

<p>To ensure I am well-equipped to handle the complexity of this project, I am participating in the PINNs Tech Bootcamp. This intensive training covers:</p>
<ul>
  <li><strong>Physics-Informed Neural Networks (PINNs)</strong>: Learning to embed physical laws into neural networks for improved simulation accuracy.</li>
  <li><strong>I-PINNs</strong>: Tackling inverse problems using PINNs to fine-tune model parameters.</li>
  <li><strong>DeepONets</strong>: Developing expertise in Deep Operator Networks, which are used for mapping functions to functions, ideal for complex simulations.</li>
  <li><strong>NVIDIA Modulus Sym</strong>: Hands-on practice with this framework, focusing on its application in CFD (Computational Fluid Dynamics) and other applied sciences.</li>
</ul>

<h3>Example of Implementation</h3>

<p>In my journey, one of the practical applications has been developing a 2D simulation in Section 3: Deep Neural Operator (DeepONet). This simulation integrates key equations such as the Navier-Stokes and Advection-Diffusion equations to model fluid dynamics. By utilizing <code>modulus.sym</code>, I have been able to develop neural networks that predict fluid velocity, pressure, and diffusivity, which are critical for simulating wind flow in urban environments.</p>

<h3>Setting Up and Using WSL for CUDA-Enabled GPU Computing</h3>

<p>To fully utilize the NVIDIA GPU on my system, I have set up a WSL environment with Ubuntu 20.04, which allows me to run Linux-based software while taking advantage of CUDA for GPU-accelerated computing. Below are the steps to replicate this setup:</p>

<h3>Step 1: Install WSL and Ubuntu 20.04</h3>
<ol>
  <li><strong>Enable WSL</strong>: Open PowerShell as an Administrator and run:
    <pre><code>wsl --install</code></pre>
    This command installs WSL and the latest version of Ubuntu by default.
  </li>
  <li><strong>Install Ubuntu 20.04</strong>: If you need a specific version, such as Ubuntu 20.04, you can install it by running:
    <pre><code>wsl --install -d Ubuntu-20.04</code></pre>
  </li>
  <li><strong>Set Up WSL</strong>: Once Ubuntu is installed, open it from your Start menu and follow the on-screen instructions to complete the setup.</li>
</ol>

<h3>Step 2: Install NVIDIA CUDA Toolkit</h3>
<ol>
  <li><strong>Update Package Lists</strong>:
    <pre><code>sudo apt-get update
sudo apt-get upgrade</code></pre>
  </li>
  <li><strong>Add NVIDIA Package Repositories</strong>:
    <pre><code>wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600</code></pre>
  </li>
  <li>
    <pre><code>sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu

  <li><pre><code>sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"</code></pre></li>
  <li><strong>Install CUDA Toolkit</strong>:
    <pre><code>sudo apt-get update
sudo apt-get -y install cuda</code></pre>
  </li>
</ol>

<h3>Step 3: Verify CUDA Installation</h3>
<ol>
  <li><strong>Check CUDA Version</strong>:
    <pre><code>nvcc --version</code></pre>
    This command should return the version of CUDA installed.
  </li>
  <li><strong>Test CUDA with a Simple Program</strong>:
    <pre><code>nvidia-smi</code></pre>
    This command provides information about your GPU, including its utilization and the processes using it.
  </li>
</ol>

<h3>Step 4: Install NVIDIA Modulus and Other Dependencies</h3>
<ol>
  <li><strong>Create a New Conda Environment</strong>:
    <pre><code>conda create -n modulus python=3.10</code></pre>
  </li>
  <li><strong>Activate the Environment</strong>:
    <pre><code>conda activate modulus</code></pre>
  </li>
  <li><strong>Install PyTorch with CUDA Support</strong>:
    <pre><code>pip install torch torchvision torchaudio</code></pre>
  </li>
  <li><strong>Install NVIDIA Modulus</strong>:
    <pre><code>pip install nvidia-modulus</code></pre>
  </li>
  <li><strong>Install Additional Dependencies</strong>:
    <pre><code>pip install -r requirements.txt</code></pre>
    Ensure you have a `requirements.txt` file with all necessary Python packages.
  </li>
</ol>

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
</html>
