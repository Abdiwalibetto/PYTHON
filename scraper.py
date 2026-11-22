import csv
import requests
from bs4 import BeautifulSoup

with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price"])

    for book in books:
        title = book.find("a")["title"]
        price = book.find_next("p", class_="price_color").text
#        print(f"Title: {title}, Price: {price}")
        writer.writerow([title, price])
