import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}


response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

liste = soup.find_all("li", {"class": "column"}, limit=10)

for li in liste:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    price = li.find("div", {"class": "proDetail"}).find(
        "div", {"class": "priceContainer"}).find("span").text.strip()


    print(f"Computer Name: {name.ljust(105)}, Price: {price} and Product Link: {link}")