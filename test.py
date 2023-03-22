import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://ngosindia.org/gujarat/amreli-ngos/"

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")

page = soup.find("ul", attrs={"class":"lcp_paginator"})
if page is None :
    print("harhahar")
