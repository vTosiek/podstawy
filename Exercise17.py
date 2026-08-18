import requests
from bs4 import BeautifulSoup
def tytuly():
    r = requests.get('https://www.nytimes.com')
    soup = BeautifulSoup(r.text, 'html.parser')
    tagi = soup.find_all("p", class_="indicate-hover")
    for tag in tagi:
        print(tag.text)
tytuly()
