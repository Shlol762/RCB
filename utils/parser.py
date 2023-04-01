from bs4 import BeautifulSoup, Tag
import requests
import re
import logging
from typing import List, Union, Tuple
import discord
from dataclasses import dataclass


log = logging.getLogger('__main__')


@dataclass
class Team:
    name: str
    logo: str
    matches_played: Union[int, str]
    wins: Union[int, str]
    losses: Union[int, str]
    tied: Union[int, str]
    no_res: Union[int, str]
    points: Union[int, str]
    net_run_rate: Union[int, str]
    # last_five: List[str]
    next_match: str
    _for: str
    _against: str


@dataclass
class PointsTable:
    year: int
    teams: List[Team]

    def to_str(self) -> Tuple[str, str]:
        head = f"{'Team':^28}{'Matches':^9}{'Win':^5}{'Loss':^6}{'Tie':^5}{'NR':^4}{'Pts':^5}{'NRR':^7} {'Next':^6}\n"
        body = ''

        for team in self.teams:
            line = f"{team.name:<28}{team.matches_played:^9}{team.wins:^5}{team.losses:^6}" \
                   f"{team.tied:^5}{team.no_res:^4}{team.points:^5}{team.net_run_rate:^7} {team.next_match:<7}\n"

            body += line

        return head, body


class IPLT20:

    root_url = 'https://www.espncricinfo.com'
    ipl_url = '/series/indian-premier-league-2023-1345038'

    def __init__(self):
        with requests.get(self.root_url + self.ipl_url) as req:
            soup = BeautifulSoup(req.text, 'lxml')
        self.matches_url = self.root_url + soup.find(href=re.compile(r'/match')).get('href')
        self.stats_url = self.root_url + soup.find(href=re.compile(r'/stats')).get('href')
        self.teams_url = self.root_url + soup.find(href=re.compile(r'/squads')).get('href')
        self.points_url = self.root_url + soup.find(href=re.compile(r'indian-premier-league-2023-1345038'
                                                                    r'/points-table-standings')).get('href')

    def points_table(self, year: int) -> PointsTable:
        self.points_url = self.root_url + self.points_url if 'https' not in self.points_url else self.points_url
        with requests.get(self.points_url) as req:
            soup = BeautifulSoup(req.text, 'lxml')
        team_data: List[Tag] = soup.find_all('tr', class_ = "ds-text-tight-s")
        teams = []

        for team_raw in team_data:
            team_name = team_raw.find('span', class_ = "ds-text-tight-s").text
            stats = [tag.text for tag in team_raw.find_all('td', class_ = re.compile(r'ds-w-0'))]

            teams.append(
                Team(team_name, 0, *stats)
            )

        return PointsTable(year, teams)
