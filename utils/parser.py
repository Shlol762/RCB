from bs4 import BeautifulSoup
import requests


class IPLT20:

    root_url = 'https://www.iplt20.com'

    def __init__(self):
        with requests.get(self.root_url) as req:
            soup = BeautifulSoup(req.text, 'lxml')
            print(soup.prettify())


IPLT20()
