import requests
from bs4 import BeautifulSoup
import html


def scrape_books():
    """Scrape book titles and prices from the site."""
    url = "http://books.toscrape.com/"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for book in soup.select('article.product_pod'):
        title = book.select_one('h3 a').get('title')
        price = book.select_one('.price_color').text.strip()
        books.append({'title': title, 'price': price})

    return books


def generate_html_table(books):
    """Return a formatted HTML table for the provided books."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book Prices</title>
        <style>
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
                font-family: Arial, sans-serif;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
        </style>
    </head>
    <body>
        <h2 style="text-align: center;">Book Prices</h2>
        <table>
            <tr>
                <th>Title</th>
                <th>Price</th>
            </tr>
    """

    for book in books:
        html_content += f"""
            <tr>
                <td>{html.escape(book['title'])}</td>
                <td>{html.escape(book['price'])}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    return html_content


def main():
    """Run the scraping process and write the result to an HTML file."""
    books = scrape_books()
    html_table = generate_html_table(books)

    with open('book_prices.html', 'w', encoding='utf-8') as f:
        f.write(html_table)
    print("HTML file 'book_prices.html' has been generated.")


if __name__ == "__main__":
    main()
