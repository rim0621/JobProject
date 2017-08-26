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

def newCheck(last_url,new_url):
    return new_url!=last_url

def iWant(context):

    if(context.find("WEB")==0):
        return False
    elif(context.find("web")==0):
        return False
    elif(context.find("웹")==0):
        return False
    else:
        return True

def connectDB(sql):
   # MySQL Connection 연결
    conn = pymysql.connect(host='localhost', user='root', password='passwd',
                       db='DB_Name', charset='utf8')

    curs = conn.cursor()
    try: #예외처리
        curs.execute(sql)
        conn.commit()
    except pymysql.Error as err:
        conn.rollback()


    conn.close()

def insertDB(company_url_full, company_name, company_title, company_sector,  company_career, company_edu, company_similarity,company_salary,index):
  #삽입  
  sql="INSERT INTO company VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"%("'"+company_url_full+"'", "'"+company_name+"'", "'"+company_title+"'", "'"+company_sector+"'", "'"+company_career+"'", "'"+company_edu+"'","'"+company_similarity+"'","'"+company_salary+"'","'"+index+"'")
    connectDB(sql)

