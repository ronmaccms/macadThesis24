<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, "Courier New", monospace;
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Urban Wind Flow Modeling with PINNs</h1>
    <p>This folder contains the training code and geometry extraction codes for OSM polygons and trains the PINN Nvidia model.</p>

    <h2>Git Commands</h2>
    <p>Below are some essential Git commands for managing your repository:</p>

    <h3>1. Checking for the 10 largest files in your commit</h3>
    <pre><code>du -ah . | sort -rh | head -n 10</code></pre>

    <h3>2. Removing a file from your Git commit</h3>
    <pre><code>git rm --cached "File Path"</code></pre>

    <h3>3. Adding a file to .gitignore</h3>
    <pre><code>echo "filename" >> .gitignore</code></pre>

    <h3>4. Committing and pushing changes</h3>
    <pre><code>
git add .gitignore
git commit -m "Add large CUDA file to .gitignore"
git push origin main
    </code></pre>

    <h3>5. Creating and managing branches</h3>
    <ul>
        <li>To create a new branch: <code>git checkout -b new-branch-name</code></li>
        <li>To switch to an existing branch: <code>git checkout branch-name</code></li>
        <li>To delete a branch: <code>git branch -d branch-name</code></li>
        <li>To push a new branch to the remote repository: <code>git push origin new-branch-name</code></li>
    </ul>

    <h2>Checking NVIDIA GPU Status</h2>
    <p>To check the status of your NVIDIA GPU, use the following command:</p>
    <pre><code>nvidia-smi</code></pre>
    <p>This command provides information on the GPU's usage and driver version.</p>

    <h2>Installing CUDA on Ubuntu 24.04</h2>
    <p>To install CUDA on Ubuntu 24.04, follow these steps:</p>
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

    <h2>Additional Resources</h2>
    <p>For more detailed information, refer to the official NVIDIA CUDA documentation and Git documentation.</p>
</body>
</html>
