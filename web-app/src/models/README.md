<h2>About The Folder</h2>

<p>This folder contains the training code and geometry extraction codes for OSM polygons and trains the PINN Nvidia model.</p>

<h3>Git Commands Cheat Sheet</h3>
<p>Below are some essential Git commands for managing your repository:</p>

<h4>1. Checking for the 10 largest files in your commit</h4>
<pre><code>du -ah . | sort -rh | head -n 10</code></pre>

<h4>2. Removing a file from your Git commit</h4>
<pre><code>git rm --cached "File Path"</code></pre>

<h4>3. Adding a file to .gitignore</h4>
<pre><code>echo "filename" >> .gitignore</code></pre>

<h4>4. Committing and pushing changes</h4>
<pre><code>
git add .gitignore
git commit -m "Add large CUDA file to .gitignore"
git push origin main
</code></pre>

<h4>5. Creating and managing branches</h4>
<ul>
  <li>To create a new branch: <code>git checkout -b new-branch-name</code></li>
  <li>To switch to an existing branch: <code>git checkout branch-name</code></li>
  <li>To delete a branch: <code>git branch -d branch-name</code></li>
  <li>To push a new branch to the remote repository: <code>git push origin new-branch-name</code></li>
</ul>

<h3>CUDA Overview and Setup</h3>
<p>CUDA is a parallel computing platform and application programming interface (API) model created by NVIDIA. It allows software developers to use a CUDA-enabled graphics processing unit (GPU) for general purpose processing – an approach known as GPGPU (General-Purpose computing on Graphics Processing Units).</p>

<h4>Checking NVIDIA GPU Status</h4>
<p>To check your NVIDIA GPU status:</p>
<pre><code>nvidia-smi</code></pre>

<h4>Installing CUDA on Ubuntu 24.04</h4>
<ol>
  <li>Download the CUDA repository package:</li>
  <pre><code>wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-repo-ubuntu2404-12-6-local_12.6.1-560.35.03-1_amd64.deb</code></pre>
  <li>Install the package:</li>
  <pre><code>sudo dpkg -i cuda-repo-ubuntu2404-12-6-local_12.6.1-560.35.03-1_amd64.deb</code></pre>
  <li>Add the GPG key:</li>
  <pre><code>sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/7fa2af80.pub</code></pre>
  <li>Update the package lists and install CUDA:</li>
  <pre><code>sudo apt-get update && sudo apt-get install -y cuda</code></pre>
  <li>Verify the installation:</li>
  <pre><code>nvcc --version</code></pre>
</ol>

<h3>Learning and Development with NVIDIA Modulus Sym</h3>
<p>As part of the development process for this project, I am actively learning how to leverage NVIDIA’s <code>modulus.sym</code> for building PINNs. The training sessions required for developing accurate models often take up to 12 hours, and they are conducted on my GPU using a WSL. This setup allows me to fully utilize the computational power of my NVIDIA GPU while working in a Linux environment.</p>

<!-- IMAGE Section -->
<div align="center">
    <img src="./web-app/src/assets/doc/data/images/Screenshot 2024-08-27 092922.png" alt="Training Image" width="500">
</div>

<h3>Example of Implementation</h3>

<p>2D simulation in Section 3: Deep Neural Operator (DeepONet). This simulation integrates key equations such as the Navier-Stokes and Advection-Diffusion equations to model fluid dynamics. By utilizing <code>modulus.sym</code>, I have been able to develop neural networks that predict fluid velocity, pressure, and diffusivity, for simulating wind flow in urban environments.</p>

<h3>Setting Up and Using WSL for CUDA-Enabled GPU Computing</h3>

<p>To fully utilize the NVIDIA GPU on my system, I have set up a WSL environment with Ubuntu 20.04, which allows me to run Linux-based software while taking advantage of CUDA for GPU computing.</p>

<div align="center">
    <img src="./web-app/src/assets/doc/data/images/gpu2.png" alt="gpu2" width="500">
</div>

<h3>Step 1: Install WSL and Ubuntu 20.04</h3>
<ol>
  <li><strong>Enable WSL</strong>: Open PowerShell as an Administrator and run:
  <pre><code>wsl --install</code></pre></li>
  <li><strong>Install Ubuntu 20.04</strong>: 
  <pre><code>wsl --install -d Ubuntu-20.04</code></pre></li>
  <li><strong>Set Up WSL</strong>: Open Ubuntu from your Start menu and follow the on-screen instructions to complete the setup.</li>
</ol>

<h3>Step 2: Install NVIDIA CUDA Toolkit</h3>

<pre><code>sudo apt-get install -y cuda</code></pre>

<h3>Running Your First Simulation</h3>
<p>After setting up your environment, you can run your first PINN simulation by navigating to the project directory and executing the following command:</p>
<pre><code>python3 your_simulation_script.py</code></pre>

<p>This command will start the simulation, utilizing your NVIDIA GPU to accelerate the computations. Depending on the complexity of the model, training can take several hours.</p>

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