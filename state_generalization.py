import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

state_url = 'https://ngosindia.org/gujarat/'

state_req = requests.get(state_url)
state_soup = BeautifulSoup(state_req.text, "lxml")

city_links = []

cat_city_links = state_soup.find_all("div", attrs={"class":"npos-postcontent clearfix"})
city_links_par = cat_city_links[0].find("ul")
city_links_sub_par = city_links_par.find_all("li")

for l in city_links_sub_par:
    city_lunk = l.find_next("a")
    city_links.append(city_lunk.get("href"))

print(city_links)
"""
for n in city_links:
    city_req = requests.get(n)
    city_soup = BeautifulSoup(city_req.text, "lxml")

    city_soup.find("ul", attrs={"class":"lcp_paginator"})
    if city_soup is None:
        lim = 1
    else:
        lim = len(city_soup)
"""
