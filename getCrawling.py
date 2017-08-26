import numpy as np
import requests
import re
from bs4 import BeautifulSoup
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Kkma
from konlpy.utils import pprint
from selenium import webdriver
import time
import pymysql

def getUrlName(data):
    company_url=[]
    company_name=[]
    for ex in data:
        url_name=ex.find_all("a","str_tit")
        for ex1 in url_name:

            company_url.append(ex1.get("href"))
            company_name.append(ex1.get("title"))

    return company_url, company_name

def getTitleSector(data):
    company_title=[]
    company_sector=[]
    for ex in data:
        title=ex.find_all("a","str_tit")
        sector=ex.find_all("p","job_sector")
        for ex1 in title:
            company_title.append(ex1.get("title"))
        for ex2 in sector:
            company_sector.append(ex2.text)
    return company_title, company_sector

def getCareerEdu(data):
     company_career=[]
     company_edu=[]
     for ex in data:
         career=ex.find_all("p","career")
         edu=ex.find_all("p","education")

         career=re.sub('<p class="career">','',str(career))
         career=re.sub('</p>','',str(career))
         edu=re.sub('<p class="education">','',str(edu))
         edu=re.sub('</p>','',str(edu))

         company_career.append(career)
         company_edu.append(edu)

     return company_career, company_edu
