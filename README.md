# 개요
 인터넷에는 사람인, 잡코리아등 많은 구직 사이트가 존재하고 새로운 정보가 어마어마하게 있고 지금 또한 올라오고 있다. 나와 상관 없는 분야, 또는 같은 분야에서 내 관심분야 밖인 공고도 많이 볼 수 있다. 황금같은 시간을 조금이나마 줄이기 위해 나에게 적합한 공고, 내가 원하는 분야만 볼 수 있도록 시작하게 되었다.

# Web Crawling
![Alt text](/img/crawling.png)
 1. 위사진과 같이 requests 와 BeautifulSoup을 import 한다.
 2. requests.get에 다가 크롤링 할 주소를 쓴다.
 3. 위에서 선언한 BeautifulSoup을 가지고 이쁘게 html을 뽑는다.
 4. 가지고온 html을 필요한 부분만 가지고 오기 위해서 soup.find_all을 사용한다.
    find_all안에 넣을 부분은 브라우져에서 F12를 누르고 해당 부분을 오른쪽 마우스->copy->copy selector을 누르면 필요한 부분이 복사된다. 처음에는 어려웠지만 여러번 시행착오를 거치면 쉬워진다. 밑에 참고 사이트를 가면 더욱더 자세히 나와 있다.
# Selenium
![Alt text](/img/selenium.png)
 1. pip install selenium
 2. https://github.com/mozilla/geckodriver/releases 드라이버 다운받기(firefox)
 3. from selenium import webdriver 선언
 4. webdriver.Firefox에 executable_path="다운받은 드라이버경로"(executable_path 없이 한 분들도 있었는데 내 경우는 오류가 발생하였다.)
 5. 다음은 그림과 같이 주석을 보고 따라하면 이해할 수 있다. 밑에 참고 사이트를 가면 더욱더 자세히 나와 있다.
# Facebook Messager
![Alt text](/img/fbMSG.png)
 1. form fbchat import Client 를 선언한다.
 2. Client()에 아이디,패스워드를 입력한다.
 3. searchForUsers()에 받는 사람을 적는다(이메일|아이디)
 4. 보낼 메시지를 적는다.
# Word2Vec
![Alt text](/img/word2vec.png)
 1. from gensim.models.word2vec import Word2Vec 선언한다.
 2. from konlpy.tag import Kkma 선언한다.
 3. kkma.nouns()를 가지고 문장들을 단어별로 나눈다.
 4. Word2Vec()로 단어들을 학습시킨다.
 5. embedding.most_similar()가지고 내가 원하는 단어들과 가장 유사한 단어를 뽑는다.
# 참고
 1. 크롤링 https://beomi.github.io/2017/04/20/HowToMakeWebCrawler-Notice-with-Telegram/
 2. 크롤링 https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
 3. 셀리늄 https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
 4. 페메   http://egloos.zum.com/mcchae/v/11266313
