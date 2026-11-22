import csv
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("h3")


with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price"])

    for book in books:
        title = book.find_next("a")["title"]
        price = book.find_next("p", class_="price_color").text
#        print(f"Title: {title}, Price: {price}")
        writer.writerow([title, price])
