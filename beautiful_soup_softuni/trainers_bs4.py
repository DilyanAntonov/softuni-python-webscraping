from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json


url = 'https://softuni.bg/trainers'

uClient = uReq(url)

page_html = uClient.read()
page_soup = soup(page_html, 'html.parser')

data = {}

trainers = page_soup.findAll(
    'article', {'class': 'trainers-page-content-trainer-info'})

for trainer in trainers:
    id = trainer.get('data-id')
    popup = page_soup.find('div', {'id': id})

    name = trainer.find(
        'p', {'class': 'trainers-page-content-trainer-name'}).text
    position = trainer.find(
        'p', {'class': 'trainers-page-content-trainer-occupation'}).text
    info = popup.find(
        'p', {'class': 'trainings-page-content-trainer-info-modal-description'}).text

    data[name] = {'position': position, 'info': info}

with open('bs4_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
