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


def getDetail(company_url):
    url='URL'
    req=requests.get(url)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    text=soup.find_all("div","job-wrapper recruit_view_reform ")
    text1=re.sub('<script type="text/javascript">.*?</script>', '', str(text), 0, re.I|re.S)
    a=re.sub('<.+?>', '', str(text1), 0, re.I|re.S)
    b=a.replace("\n","").replace("\r","").replace("\t","")#.replace(" ","")
    #print(b)
   # print(url)
    return url, b;

def getSimilarity(detail):
    prediction=[]
    count=0;
    myword=['빅데이터','하둡','딥러닝','개발자','응용','python','c','c++','응용시스템','프로그램','언어','소프트웨어','IOT','사물인터넷']
    kkma=Kkma()
    a=kkma.nouns(detail)
    embedding=Word2Vec([a],min_count=1,size=32,window=4,iter=10,sg=1)
    for i in range (0,len(myword)):
        try:
            prediction.append(embedding.most_similar(positive=myword[i],topn=1))
            count=count+1
        except KeyError:
            pass


    return count
