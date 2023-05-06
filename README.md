<a name="readme-top"></a>

<h1 align="center">Tech News Scraper 💻</h1>

<details>
  <summary>Summary</summary><br />
  <ol>
    <li><a href="#about-the-project">About the Project</a></li>
    <li><a href="#technologies">Technologies</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#how-to-xecute-the-project">How to Execute the Project</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About the Project

Tech News is a Python-based data scraping project that uses Beautiful Soup to perform web scraping on Trybe's blog and fetch technology news and articles, storing them in a non-sequential MongoDB database.

<br/>

## Technologies
<details>
  <summary><strong>✨ Show Tecnologies</strong></summary><br />

- PYTHON 3
- MONGODB
- PYMONGO
- PYTEST
- BEAUTIFUL SOUP
- FLAKE
</details>
<br/>

## Features

<ul>
  <li>Collect news and articles from Trybe's blog using web scraping and store them in a MongoDB database</li>
  <li>Search news by title</li>
  <li>Search news by date</li>
  <li>Browse news by category</li>
  <li>List the top 5 categories with the most news</li>
</ul>

<br/>

## How to Execute the Project

To run the project locally, follow the steps below.

1. Check that your machine has the minimum configuration for the project to run;

- Python 3;
- Docker;
- Docker-compose version equal to or greater than `1.29.2`.

2. Clone the repository;

```
git clone https://github.com/RuhamLeal/tech_news_scraper.git
```

3. Navigate to the root of the project;

```
cd ./tech_news_scraper
```

4. Create and activate the virtual environment.

```
python3 -m venv .venv

source .venv/bin/activate
```

5. Install dependencies in the virtual environment.

```
dpython3 -m pip install -r dev-requirements.txt
```

6. If you don't have MongoDB installed locally, launch it via Docker.
```
docker-compose up -d mongodb
```

7.Run the following command to access the menu.
```
tech-news-analyzer
```

<br/>

## Contact

Ruham Leal    
Email: ruhamxlpro@hotmail.com    
[![Linkedin][linkedin-badge]][linkedin-url]

<p align="right"><a href="#readme-top">Voltar ao topo</a></p>

<!-- MARKDOWN LINKS & IMAGES -->

[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/ruham-leal/
