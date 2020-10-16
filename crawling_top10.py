### 후보 연예인 10명의 이름으로 각각 기사 제목 크롤링 

import requests
from bs4 import BeautifulSoup

# BASE_PATH 폴더에 크롤링한 결과를 저장 할 텍스트파일이 생성될 것임 (후보의 수만큼) 
BASE_PATH = '/'
# name_file: 후보 이름이 '\n'으로 구분되어있는 텍스트 파일
name_file = open('top10.txt', 'r')


def crawl(keyword, maxpage):
    count = 0
    page = 1
    maxpage_t = (int(maxpage) - 1) * 10 + 1  # 11= 2페이지 21=3페이지 31=4페이지 ...81=9페이지 , 91=10페이지, 101=11페이지

    # f: output file
    # ex) 유이.txt, 소유.txt, ... 
    f = open(BASE_PATH + star + '.txt', 'w', encoding='utf-8')
    while page <= maxpage_t:
        url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword + "&ds=&de=&docid=&nso=&mynews=1" + "&start=" + str(
            page)
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        articles = soup.select("ul.type01>li")

        for article in articles:
            print(article.select_one("a._sp_each_title").text + "\t" + article.select_one(
                "span._sp_each_source").text)
            f.write(article.select_one("a._sp_each_title").text + "\t" + article.select_one(
                "span._sp_each_source").text + "\n")
            count += 1
        page += 10
    
    f.close()
    return count 


# namelist 만들기
namelist = []
while True:
    line = name_file.readline()
    if line == '':
        break
    name = line.replace('\n', '')
    namelist.append(name)


# 각각의 연예인에 대해서 크롤링 
for star in namelist:
    maxpage = 5       # 네이버 검색의 최대 페이지 수
    result = crawl(star, maxpage)
    print(star + '>>', result, 'completed')


name_file.close()
