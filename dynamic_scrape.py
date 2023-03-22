import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

ngo_links = []
ngo_name = []
ngo_add = []
ngo_city = []
ngo_pin = []
ngo_state = []
ngo_mobile = []
ngo_email = []
ngo_web = []
ngo_contactper = []
ngo_purpose = []
ngo_about = []


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

for n in city_links:
    city_req = requests.get(n)
    city_soup = BeautifulSoup(city_req.text, "lxml")

    city_soup.find("ul", attrs={"class":"lcp_paginator"})
    if city_soup is None:
        lim = 1
    else:
        lim = len(city_soup)

    for m in range(1,lim):

        url = n + '?lcp_page0=' + str(m) + '#lcp_instance_0'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")

        #print(soup.prettify())
        links = []
        cat_list = []
        ngo_links = []
        cat_list = soup.find(id = "lcp_instance_0")
        #print(cat_list)

        links = cat_list.find_all("li")
        #print(links)

        for x in links :
            lunk = x.find_next("a")
            ngo_links.append(lunk.get("href"))

        for i in ngo_links:
            print("Scraping -> " + i + "........")
            sub_req = requests.get(i)
            sub_soup = BeautifulSoup(sub_req.text, "lxml")



            #test_url = "https://ngosindia.org/gujarat-ngos/aadhar-ahemedabad/"

            #test_req = requests.get(test_url)
            #test_soup = BeautifulSoup(test_req.text, "lxml")

            ngo_content_par = sub_soup.find_all("div", attrs={"class":"npos-postcontent clearfix"})
            ngo_content = ngo_content_par[1].find("p")

            #for div in ngo_content_par: 
            #   print(div)

            #print(ngo_name)
            #print(ngo_content)
            #print(ngo_content_par[1])

            if ngo_content is None:
                continue

            ngo_name_par = sub_soup.find("h1", "npos-postheader entry-title")
            ngo_name.append(ngo_name_par.string)

            ngo_str = ngo_content.get_text()
            ngo_all = ngo_str.split("\n")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")
            ngo_all.append("This needs fixing T-T")

            add_d = ngo_all[0].removeprefix(" ")
            add_d = add_d.removeprefix("Add.:")
            add_d = add_d.removeprefix("Add : ")
            ngo_add.append(add_d)
            #ngo_add.append(ngo_all[0].removeprefix("Add.:"))
            ngo_city.append(ngo_all[1])

            pin_p = ngo_all[2].removeprefix(" ")

            if "Pin" in pin_p or "pin" in pin_p:
                pin_p = pin_p.removeprefix("Pin:")
                pin_p = pin_p.removeprefix(" ")
                pin_p = pin_p.removeprefix("Pin : ")
                ngo_pin.append(pin_p)
                ngo_state.append(ngo_all[3])
            else:
                ngo_pin.append(ngo_all[3])
                ngo_state.append(pin_p)
            #ngo_pin.append(ngo_all[2].removeprefix("Pin:"))
            #ngo_state.append(ngo_all[3])
            ngo_mobile.append(ngo_all[5].removeprefix("Mobile:") + " " + ngo_all[4].removeprefix("Phone:"))

            mail_m = ngo_all[6].removeprefix("Email:")
            mail_m = mail_m.removeprefix(" ")
            mail_m = mail_m.removeprefix("Email : ")
            ngo_email.append(mail_m)

            web_b = ngo_all[7].removeprefix("Website:")
            web_b = web_b.removeprefix(" ")
            web_b = web_b.removeprefix("Website : ")
            ngo_web.append(web_b)
            ngo_contactper.append(ngo_all[8].removeprefix("Contact Person:"))
            ngo_purpose.append(ngo_all[9].removeprefix("Purpose :"))
            ngo_about.append(ngo_all[10].removeprefix("Aims/Objectives/Mission :"))

data = {
    "Name of NGOs" : ngo_name,
    "Address" : ngo_add,
    "City" : ngo_city,
    "Pin Code" : ngo_pin,
    "State" : ngo_state,
    "Mobile No(s)." : ngo_mobile,
    "Email" : ngo_email,
    "Website" : ngo_web,
    "Name of Contact Person" : ngo_contactper,
    "Purpose" : ngo_purpose,
    "About" : ngo_about
}

datframe = pd.DataFrame(data)
datframe.to_json("D:/pushistov/Scrape-Items/CSVS/datcsvtho7.json", orient="records")




