import requests
from bs4 import BeautifulSoup

maxpage = input("최대 출력할 페이지수 입력하시오: ")
search_keyword = input("검색어 입력: ")


# 검색된 네이버뉴스의 기사내용을 크롤링합니다.
page = 1
maxpage_t = (int(maxpage) - 1) * 10 + 1  # 11= 2페이지 21=3페이지 31=4페이지 ...81=9페이지 , 91=10페이지, 101=11페이지

f = open('/Users/iseungjin/news_list.txt', 'w', encoding='utf-8')

f.write(str(int(maxpage)*10))
f.write('\n')

while page <= maxpage_t:
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+search_keyword+"&ds=&de=&docid=&nso=&mynews=1"+ "&start=" + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.select("ul.type01>li")

    for article in articles:
        print(article.select_one("a._sp_each_title").text)
        f.write(
            article.select_one("a._sp_each_title").text + "\n")
    page += 10

f.close()

