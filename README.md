# Web Scraper for News Headlines

## Objective

Scrape the top headlines from a news website using Python and save them to a `.txt` file.

---

## Tools & Libraries

- **Python**
- [`requests`](https://pypi.org/project/requests/) – for making HTTP requests
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) – for parsing and extracting data from HTML

---

## Installation

1. Clone this repository or download the files.
2. Install required Python modules:

```bash
pip install requests beautifulsoup4
```

---
### How to Run

```bash
python news_scraper.py
```
It will:

- Fetch the HTML from the news site (https://www.bbc.com/news by default)
- Parse the headlines (e.g., from <h2> tags)
- Save them to headlines.txt
