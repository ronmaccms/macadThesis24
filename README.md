# macadThesis24
<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://github.com/ronmaccms/macadThesis24/assets/logos/project-logo.jpg" alt="Logo" width="450">
  <h3 align="center"> Enhancing Architectural Visualization and GIS Feedback </h3>
  <p align="center" style="font-weight: bold;">IAAC: AI 2023-24<br>
    <a href="https://colab.research.google.com/github/ronmaccms/macadThesis24/blob/main/src/notebook.ipynb">View Demo</a>
    ·
    <a href="https://github.com/ronmaccms/macadThesis24/issues">Report Bug</a>
    ·
    <a href="https://github.com/ronmaccms/macadThesis24/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Our goal is to develop a web-based platform that integrates real-time GIS data with advanced simulations to enhance architectural visualization and decision-making processes in the AEC industry. The platform will provide efficient access to site-specific data and visualizations, facilitating informed decision-making during architectural discussions.</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#intro">Intro</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#team">Team</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
![Project image](assets/img/project-img.png)

Project developed under the course IAAC: AI 2023-24 in [IAAC](https://iaac.net/).

__Project Breakdown__

__Data Collection:__ Gather data on topography, real-time environmental conditions, and GIS data.  
__Model Training:__ Use the collected data to train the AI model.  
__Implementation:__ Deploy the trained model to enhance architectural visualization and provide real-time GIS feedback.

__Data Collection Plan__

__We will focus on collecting data for multiple locations, starting with Manhattan. The project is divided into several data sets, each assigned to a team member.__

Topographical Data:

__Task:__ Develop a web scraping script to collect historical topography data.  
__Implementation:__ Use the provided GitHub script skeleton to scrape relevant websites and databases.  
__Outcome:__ Clean, structured dataset for topographical data.

Real-Time Environmental Data:

__Task:__ Extend the data collection process to include real-time environmental conditions such as weather and vegetation cover.  
__Implementation:__ Adapt the initial script for each new data source.  
__Outcome:__ Clean datasets for real-time environmental data.

GIS Data:

__Task:__ Gather GIS data from reliable sources.  
__Implementation:__ Identify and extract data from government databases and open-source platforms.  
__Outcome:__ Clean dataset for GIS data.

__Workflow__

__Model Selection:__ Identifying the most appropriate AI model for the task requires extensive experimentation and validation. Different algorithms might perform variably based on the nature of the data.

__Model Training:__ Training a robust model requires substantial computational resources, especially when dealing with large datasets and complex algorithms.

__Handling Imbalanced Data:__ Environmental data might be imbalanced, with some conditions (e.g., extreme weather events) being rare. This can affect the model’s ability to generalize.

__Scalability:__ Ensuring that the tool can scale to handle multiple locations and large datasets without compromising performance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [Vue.js](https://vuejs.org/)
* [Python3](https://www.python.org/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Google Maps API](https://developers.google.com/maps)
* [LiDAR](https://www.lidar.com/)
* [MeshGraphNet](https://arxiv.org/pdf/2010.03409.pdf)
* [QGIS](https://qgis.org/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Colab](https://colab.research.google.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Challenges
While working on the project the following challenges were encountered:

__Web Scraping and Data Preparation:__

- Use Python and libraries like BeautifulSoup, Scrapy, and Pandas.
- Clean and structure the data using Python scripts.
- Store the data in a format suitable for AI training (e.g., CSV, JSON).

__Model Training:__

- Use the collected datasets to train an AI model.
- Evaluate different algorithms (e.g., regression models, neural networks) to determine the best fit.
- Validate the model using cross-validation techniques.

__Model Deployment:__

- Integrate the trained model into the platform.
- Develop a user-friendly interface for stakeholders to interact with the platform.
- Provide detailed reports and visualizations of the data and analyses.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Future Work
Description coming soon...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Team & Contacts
<br />
<h1>Andres Roncal</h1>
<div style="width:100%;" width=100%>
    <div>
        <a href="https://www.linkedin.com/in/andres-roncal-1b148a132/" target="_blank">
            <img src="src\img\andres.png" style="filter: grayscale(100%);" alt="Andres Roncal" height=200px style="filter: grayscale(100%);">
        </a>
    </div>
  <h3>Thesis Advisor</h3>
  <h1>David Andres Leon</h1>
  <br />
    <div style="display:flex; flex-direction: row; flex-wrap; justify-content:space-around;">
        <a href="https://es.linkedin.com/in/davidandresleon" target="_blank">
          <img src="src\img\davidProfilePic.png" style="filter: grayscale(100%);" alt="David Andres Leon" height=200px>
        </a>
    </div>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
