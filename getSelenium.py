#-*- coding: utf-8 -*-
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

def getsalary(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    text=soup.select("div.group.group01 > div.graph_info > div.wrap_graph.age > div > div > span")
    for ptext in text:
        salary=ptext.getText()

    return salary

def findsalary(company_name):

    driver = webdriver.Firefox(executable_path="geckodriver_path")  # 파이어폭스 드라이버 생성
    driver.get("URL")  # 접속

    elem = driver.find_element_by_id("search_company_nm") #검색창 클래스
    elem.send_keys(company_name) #검색창에 company_name 검색
    elem.submit()
    # 닫기
    driver.close()
    # 링크접속

    try:     
        driver.find_element_by_link_text(company_name).click() # 링크들어가기
        salary_url=driver.current_url #현재 url 가져오기
        salary=getsalary(salary_url)
    except:
        salary="no info"

    return salary
