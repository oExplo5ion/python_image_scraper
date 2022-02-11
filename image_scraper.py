import requests
from bs4 import BeautifulSoup

class ImageScraper():

    def scrap_image(self, url=str):
        html_data = requests.get(url=url).text
        soup = BeautifulSoup(html_data, 'html.parser')
        scrs = []
        for item in soup.find_all('img'):
            scrs.append(item['src'])
        return scrs
