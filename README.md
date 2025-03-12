# PubMed Paper Fetcher

## Overview
**PubMed Paper Fetcher** is a command-line tool that allows users to search for research papers on **PubMed** and retrieve key details such as:
- Paper title
- Publication date
- Non-academic authors
- Company affiliations
- Corresponding author email

The results can be displayed in the terminal or saved as a CSV file.

## Project Structure

    paper_fetcher/
    │── src/paper_fetcher/
    │ ├── init.py # Package initializer 
    │ ├── cli.py # CLI script for execution 
    │ ├── paper_fetcher.py # Core logic to fetch papers 
    │── pyproject.toml # Poetry project configuration 
    │── README.md # Project documentation

## Installation & Usage

### 1. Install Dependencies
This project uses **Poetry** for package management. To install dependencies, run:
```bash
poetry install
```

## 2. Running the Script

To fetch papers from PubMed, run:
```bash
poetry run get-papers-list "cancer research"
```
or
```bash
poetry run get-papers-list "machine learning in healthcare" -d -f results.csv
```

-d or --debug enables debug mode.
-f <filename> or --file <filename> saves results to a CSV file.

## 3. Tools and Libraries used
- Python 3.11 - Core language
- Poetry - Dependency management [Poetry Docs](https://python-poetry.org/docs)
- Requests - API calls to PubMed [Docs](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- Regex (re module) - Extracting information from XML

## 4.  LLM Reference
ChatGPT - [Chat](https://chatgpt.com/share/67d1c61a-40ac-8012-9c67-ef2fc90d6e16)




---

MADE BY [Devi Chandu Reddy Motati](https://github.com/chandumotati611)