import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
from tqdm import tqdm
from dataclasses import dataclass, field, astuple
from collections import namedtuple


@dataclass(slots=True)
class Kufar:
    id: str = field(default="")
    title: str = field(default="")
    link: list = field(default_factory=list)
    parameters: dict = field(default_factory=dict)
    images: list = field(default_factory=list)
    price: int = field(default=0)


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

# data = '["cat=16040&pathname=listings","cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MiwicGl0IjoiMjgzNjg1NDEifQ%3D%3D&pathname=listings","cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MywicGl0IjoiMjgzNjg1NDEifQ%3D%3D&pathname=listings","cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6NCwicGl0IjoiMjgzNjg1NDEifQ%3D%3D&pathname=listings","cat=16040&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6NSwicGl0IjoiMjgzNjg1NDEifQ%3D%3D&pathname=listings"]'
#
# response = requests.post(
#     "https://api.kufar.by/seotools/v1/to-friendly", headers=headers, data=data
# )
# data = json.loads(response.text)
# pages = [f"https://www.kufar.by/{el}" for el in data]
# __import__("pprint").pprint(pages)
#
params = {
    "cat": "16040",
    "cursor": "eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=",
    "lang": "ru",
    "size": "43",
}

r = requests.get(
    "https://api.kufar.by/search-api/v2/search/rendered-paginated",
    params=params,
    headers=headers,
)
d = json.loads(r.text)
cursors = [el["token"] for el in d["pagination"]["pages"]]

items = {}
items_ = []

for el in cursors:
    params = {
        "cat": "16040",
        "cursor": el,
        "lang": "ru",
        "size": "43",
    }
    r = requests.get(
        "https://api.kufar.by/search-api/v2/search/rendered-paginated",
        params=params,
        headers=headers,
    )
    d = json.loads(r.text)

    for el in d["ads"]:
        # items[el["ad_id"]] = {
        #     "id": el["ad_id"],
        #     "title": el["subject"],
        #     "link": el["ad_link"],
        #     "parameters": el["ad_parameters"],
        #     "price": el["price_byn"],
        #     "images": [
        #         f"https://rms8.kufar.by/v1/gallery/{i['path']}" for i in el["images"]
        #     ],
        # }
        item = Kufar()

        item.id = el["ad_id"]
        item.title = el["subject"]
        item.link = el["ad_link"]
        item.parameters = el["ad_parameters"]
        item.price = el["price_byn"]
        item.images = [
            f"https://rms8.kufar.by/v1/gallery/{i['path']}" for i in el["images"]
        ]
        items_.append(item)
    # pprint(d)
    pprint(items_)
    print(len(items_))
