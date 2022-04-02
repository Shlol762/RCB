from bs4 import BeautifulSoup
import requests
import re


class IPLT20:

    root_url = 'https://www.iplt20.com'

    def __init__(self):
        with requests.get(self.root_url) as req:
            soup = BeautifulSoup(req.text, 'lxml')
            self.matches_url = soup.find(href=re.compile(r'matches/schedule/men')).get('href')
        with requests.get(self.root_url) as req:
            soup = BeautifulSoup(req.text, 'lxml')
            self.stats_url = soup.find(href=re.compile(r'stats/2022')).get('href')

IPLT20()
