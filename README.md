# Book Scrapping

This project contains a simple Python script that scrapes book titles and
prices from [books.toscrape.com](http://books.toscrape.com/). The script
outputs an `HTML` file showing the collected information in a table.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

You can install dependencies using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the scraper directly:

```bash
python scrape_books.py
```

This will create a file named `book_prices.html` in the project directory.
Open it in a browser to view the scraped data.

