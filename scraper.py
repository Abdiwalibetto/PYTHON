import csv
import requests
from bs4 import BeautifulSoup


with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price"])

    for page in range(1, 51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("h3")

        for book in books:
            title = book.find("a")["title"]
            price = book.find_next("p", class_="price_color").text
            writer.writerow([title, price])
