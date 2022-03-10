"""
Code by
  __  __      _ _                 _____ _          
 |  \/  | ___| | | _____      __ |  ___(_)_ __ ___ 
 | |\/| |/ _ \ | |/ _ \ \ /\ / / | |_  | | '__/ _ \
 | |  | |  __/ | | (_) \ V  V /  |  _| | | | |  __/
 |_|  |_|\___|_|_|\___/ \_/\_/   |_|   |_|_|  \___|
check out my stuff on https://linktr.ee/Mellowfire
"""
import requests
from bs4 import BeautifulSoup
import random

url = "https://a-z-animals.com/animals/"
global headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
request = requests.get(url, headers=headers)
soup = BeautifulSoup(request.text, "html.parser")
animals = soup.find_all(class_="col-md-4")
print(animals)
global imagess
global links
global names
imagess = []
links = []
names = []


def run():
    imagess.clear()
    links.clear()
    names.clear()
    for _ in range(9):
        randompicks = random.choices(animals)
        for ras in randompicks:
            link = ras.find("a")["href"]
            name = ras.text
            link2 = link + "pictures/"
            request2 = requests.get(link2, headers=headers)
            bs = BeautifulSoup(request2.text, "html.parser")
            images = bs.findAll(class_="full_size_link")
            names.append(name)
            links.append(link)
            imagess.append(images[0].attrs["href"])
            break

    if len(names) != 9 or len(links) != 9 or len(imagess) != 9:
        run()


run()
