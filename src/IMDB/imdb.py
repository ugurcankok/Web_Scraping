import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, 'html.parser')

list_li = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li", limit=10)

for li in list_li:
    title = li.find("div", {"class": "ipc-metadata-list-summary-item__tc"}).find(
        "div", {"class": "sc-14dd939d-0"}
    ).find("div", {"class": "ipc-title"}).find("a").text

    year = li.find("div", {"class": "ipc-metadata-list-summary-item__tc"}).find(
        "div", {"class": "sc-14dd939d-0"}
    ).find("div", {"class": "sc-14dd939d-5"}).find("span", {"class": "sc-14dd939d-6"}).text

    rating = li.find("div", {"class": "ipc-metadata-list-summary-item__tc"}).find(
        "div", {"class": "sc-14dd939d-0"}
    ).find("span", {"class": "sc-14dd939d-1"}).find("div", {"class": "sc-951b09b2-0"}).find("span").text

    print(f"Movie Name: {title.ljust(55)}, Movie Year: {year}, and Rating: {rating}")