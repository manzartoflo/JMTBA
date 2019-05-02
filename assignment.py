#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:49:50 2019

@author: manzar
"""
import requests
from bs4 import BeautifulSoup

url = "http://www.jmtba.or.jp/english/members-directory/list-of-members/"

header = "Company name, Telephone, Email, Website\n"
file = open("assignment.csv", "w")
file.write(header)

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
divs = soup.findAll("table", {"class": "listoftables"})
for div in divs:
    find = div.findAll("tr")
    for element in find[1:]:
        rqst = requests.get(element.a.attrs['href'])
        #print(element.a.attrs['href'])
        soup_inside = BeautifulSoup(rqst.text, "lxml")
        name = soup_inside.findAll("h1")
        print(name[0].text)
        block = soup_inside.findAll("tr")
        telephone = block[1].td.text
        #website = block[-2].td.text
        print(telephone)
        #print(website)
        for ex in block:
            if('http' in ex.td.text):
                website = ex.td.text
                break
            else:
                website = 'NaN'
        print(website)
        for ex in block:
            if('@' in ex.td.text):
                email = ex.td.text
                break
            else:
                email = 'NaN'
        print(email)
        file.write(name[0].text.replace(",", "").replace("\n", "") + ", " + telephone.replace("\n", "") + ", " + email.replace("\n", "") + ", " + website.replace("\n", "") + "\n " )
file.close()
file = open("assignment.csv", "a")
url = "http://www.jmtba.or.jp/english/gurundfos/"
rqst = requests.get(url)
#print(element.a.attrs['href'])
soup_inside = BeautifulSoup(rqst.text, "lxml")
name = soup_inside.findAll("h1")
print(name[0].text)
block = soup_inside.findAll("tr")
telephone = block[1].td.text
#website = block[-2].td.text
print(telephone)
#print(website)
for ex in block:
    if('http' in ex.td.text):
        website = ex.td.text
        break
    else:
        website = 'NaN'
print(website)
for ex in block:
    if('@' in ex.td.text):
        email = ex.td.text
        break
    else:
        email = 'NaN'
print(email)
file.write(name[0].text.replace(",", "").replace("\n", "") + ", " + telephone.replace("\n", "") + ", " + email.replace("\n", "").replace(',', '.') + ", " + website.replace("\n", "") + "\n " )
file.close()
    
import pandas 
file = pandas.read_csv('assignment.csv')

