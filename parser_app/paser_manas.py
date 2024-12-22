import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://kg.kinoafisha.info/bishkek/cinema/8326434'

HEADERS = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

def get_html(url, params=""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all('div', class_="movieList movieList-grid grid swipe outer-mobile inner-mobile":
    manas_list = []
    for item in items:
        title = item.find("div", class_="movieItem_title").get_text(strip=True)
        image = URL + item.find("div", class_="picture_image").find("img").get("src")
        genres = item.find("div", class_="movieItem_genres").get_text(strip=True)
        year = item.find("div", class_="movieItem_year").get_text(strip=True)

        manas_list.append(
            {
                "title": title,
                "image": image,
                "genres": genres,
                "year": year,
            }
        )
    return manas_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        manas_list2 = []
        for page in range(1,2):
            response = get_html("https://www.kinoafisha.info/online/", params={"page": page})
            manas_list2.extend(get_data(response.text))
        return manas_list2
    else:
        raise Exception('Error in parsing')
