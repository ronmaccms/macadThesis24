<h2>About The Folder</h2>

<h3>Learning and Development with NVIDIA Modulus Sym</h3>
<p>As part of the development process for this project, I am actively learning how to leverage NVIDIA’s <code>modulus.sym</code> for building PINNs. The training sessions required for developing accurate models often take up to 12 hours, and they are conducted on my GPU using a WSL. This setup allows me to fully utilize the computational power of my NVIDIA GPU while working in a Linux environment.</p>

<p>The 2D simulation in Section 3: Deep Neural Operator (DeepONet) demonstrates the power of integrating key equations such as the Navier-Stokes and Advection-Diffusion equations to model fluid dynamics. By utilizing <code>modulus.sym</code>, I have been able to develop neural networks that predict fluid velocity, pressure, and diffusivity, simulating wind flow in urban environments.</p>

<p>PINNs represent an innovative approach in computational modeling by embedding partial differential equations (PDEs) directly into the neural network’s training process. This ensures that the model adheres to established physical laws, such as the Navier-Stokes equations, leading to highly accurate simulations of complex systems like urban wind flow.</p>

<div align="center">
    <img src="https://github.com/ronmaccms/macadThesis24/blob/main/web-app/src/assets/doc/data/images/navier-stokes.png" alt="Navier-Stokes Equations" width="500">
</div>

<p>In this project, the Navier-Stokes equations are used to model how air flows through urban landscapes, predicting phenomena like wind acceleration around corners and vortex formation behind buildings.</p>

<h4>Boundary and Initial Conditions</h4>
<p>The PINNs are configured with boundary conditions derived from real-time data. These conditions control the entry, exit, and flow of wind through the simulated urban landscape.</p>

<p>Integrating data from NOAA, OpenWeatherMap, and OpenStreetMap into the PINN model allows for the dynamic adaptation of simulations to real-time environmental conditions. This ensures that the model remains responsive and accurate, providing valuable insights for urban planners.</p>

<div align="center">
    <img src="https://github.com/ronmaccms/macadThesis24/blob/main/web-app/src/assets/doc/data/images/2d-heat-sink-with-fins.png" alt="Wind Simulation" width="600">
</div>

<h3>Git and WSL Cheat Sheet</h3>

<h4>Essential Git Commands</h4>
<p>Below are some essential Git commands for managing your repository:</p>

<ul>
  <li><strong>Checking for the 10 largest files in your commit:</strong>
  <pre><code>du -ah . | sort -rh | head -n 10</code></pre></li>

  <li><strong>Removing a file from your Git commit:</strong>
  <pre><code>git rm --cached "File Path"</code></pre></li>

  <li><strong>Adding a file to .gitignore:</strong>
  <pre><code>echo "filename" >> .gitignore</code></pre></li>

  <li><strong>Committing and pushing changes:</strong>
  <pre><code>git add .gitignore
git commit -m "Add large CUDA file to .gitignore"
git push origin main</code></pre></li>

  <li><strong>Creating and managing branches:</strong>
  <ul>
    <li>To create a new branch:
    <pre><code>git checkout -b new-branch-name</code></pre></li>
    <li>To switch to an existing branch:
    <pre><code>git checkout branch-name</code></pre></li>
    <li>To delete a branch:
    <pre><code>git branch -d branch-name</code></pre></li>
    <li>To push a new branch to the remote repository:
    <pre><code>git push origin new-branch-name</code></pre></li>
  </ul>
  </li>
</ul>

<h4>Checking NVIDIA GPU Status</h4>
<p>To check if your system has an NVIDIA GPU and ensure that it’s correctly configured for CUDA:</p>

<ul>
  <li>Run the following command in your terminal:
  <pre><code>nvidia-smi</code></pre></li>
  <li>If you see your GPU details listed, your system is set up correctly.</li>
</ul>

<h4>Installing CUDA on Ubuntu 20.04</h4>
<p>If you need to install CUDA, follow these steps:</p>

<ul>
  <li><strong>Install CUDA Toolkit:</strong>
  <pre><code>sudo apt-get install -y cuda</code></pre></li>
  <li><strong>Verify CUDA installation:</strong>
  <pre><code>nvcc --version</code></pre></li>
</ul>

<h4>Setting Up WSL</h4>
<p>To set up WSL with Ubuntu 20.04 on your system:</p>

<ol>
  <li><strong>Enable WSL:</strong> Open PowerShell as an Administrator and run:
  <pre><code>wsl --install</code></pre></li>
  <li><strong>Install Ubuntu 20.04:</strong> 
  <pre><code>wsl --install -d Ubuntu-20.04</code></pre></li>
  <li><strong>Set Up WSL:</strong> Open Ubuntu from your Start menu and follow the on-screen instructions to complete the setup.</li>
</ol>

<h3>Running Your First Simulation</h3>
<p>After setting up your environment, you can run your first PINN simulation by navigating to the project directory and executing the following command:</p>
<pre><code>python3 your_simulation_script.py</code></pre>

<p>This command will start the simulation, utilizing your NVIDIA GPU to accelerate the computations. Depending on the complexity of the model, training can take several hours.</p>

<h3>Contributor</h3>
<p><strong>Andres</strong></p>
    <img src="./web-app/src/assets/img/andres-pic.jpg" alt="Andres" width="100">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>