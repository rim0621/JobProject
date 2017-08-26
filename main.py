#-*- coding: utf-8 -*-
import numpy as np
import requests
import re
from bs4 import BeautifulSoup
import time
import pymysql
import getCrawling
import getSelenium
import withDB
import fbMSG
import getParser
#----------------------------------------------------------



last_url=None
index=9;
while(1):
    start_time = time.time()
    print(index)
    req = requests.get('URL')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find_all("div", "common_recruilt_list")

    for ptext in text:

        company_url_name=ptext.find_all("td","company_nm") # url(get("href")) & name(get("title"))
        company_title_sector=ptext.find_all("td","notification_info") #2 -> job_tit, job_sector
        company_career_edu=ptext.find_all("td","recruit_condition") #3 -> career(숫자면 패스)경력무관 , education

        company_url,company_name = getCrawling.getUrlName(company_url_name)
        company_title, company_sector = getCrawling.getTitleSector(company_title_sector)
        company_career, company_edu = getCrawling.getCareerEdu(company_career_edu)

        #print(newCheck(last_url,company_url[0]),company_career[0], iWant(company_title[0]))
        if(withDB.newCheck(last_url,company_url[0]) and (company_career[0]=="[경력무관]" or company_career[0]=="[신입]" or company_career[0]=="[신입 · 경력]" ) and withDB.iWant(company_title[0])): #중복아님, 경력아님, 웹아님
            last_url=company_url[0]
            company_url_full, company_detail =getParser.getDetail(company_url[0])
            company_similarity=getParser.getSimilarity(company_detail)
            company_salary = getSelenium.findsalary(company_name[0])
            withDB.insertDB(company_url_full, company_name[0], company_title[0], company_sector[0],  company_career[0], company_edu[0], str(company_similarity),str(company_salary),str(index))
            fbMSG.sendMSG(company_url_full)
            print("good work")
            index = index + 1;
        else:
            print("no work")
            continue



    end_time = time.time()
    #print ("time=",(end_time - start_time),"초")
    time.sleep(300) #2분정도마다 첵크


    #   print(company_url_full, " ", company_name[0], " ", company_title[0], " ", company_sector[0], " ", company_career[0]," ", company_edu[0], " ", str(company_similarity))
 #   print(last_url)



