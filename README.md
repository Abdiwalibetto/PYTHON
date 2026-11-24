# Books Scraper & Data Cleaning

## Part 1: Scraper

**What it does:** A Python script that visits books.toscrape.com, collects the title and price of each book on all 50 pages, and saves them to `books.csv`.

**How to run it:**
1. Install Python from python.org
2. Install the libraries: `pip install requests beautifulsoup4`
3. Run the script: `python scraper.py`

**Tools used:** Python, requests, BeautifulSoup

## Part 2: Data Cleaning

**What it does:** Loads `books.csv`, converts prices to numbers, and creates:
- `cleaned_books.csv`: the cleaned data
- `summary.txt`: total books, average price, 5 cheapest and 5 most expensive

**How to run it:**
1. Run Part 1 first, so `books.csv` exists
2. Install pandas: `pip install pandas`
3. Run the script: `python clean.py`

**Tools used:** Python, pandas