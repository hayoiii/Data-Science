from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import urllib.parse
from urllib.request import Request, urlopen
from time import sleep
import pandas as pd



search = input("검색어를 입력하세요 : " )
 #검색어를 URL에 사용할 수 있도록 urllib.parse.quote 사용
search = urllib.parse.quote(search)
# /와/ 사이에 검색어가 들어가기 때문에 주소 사이에 검색어를 넣어줌
url = 'https://www.instagram.com/explore/tags/'+str(search)+'/' 
#웹드라이버 사용
driver = webdriver.Chrome('chromedriver.exe')

driver.get(url)
#드라이버 실행 후 페이지가 완전히 로드된 후 진행하기 위해서 5초간 sleep 
sleep(5)


SCROLL_PAUSE_TIME = 1.0
reallink = []

while True:
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, "lxml")


    #게시물들의 주소를 가지고 옴
    for link1 in bsObj.find_all(name="div",attrs={"class":"Nnq7C weEfm"}):
        title = link1.select('a')[0] 
        real = title.attrs['href']
        reallink.append(real) 
        title = link1.select('a')[1] 
        real = title.attrs['href']
        reallink.append(real) 
        title = link1.select('a')[2] 
        real = title.attrs['href']
        reallink.append(real) 

    # 페이지의 height를 비교해서 스크롤 하고 height값이 같으면 스크롤을 멈춘다.
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
            
        else:
            last_height = new_height
            continue


csvtext = []

reallinknum = len(reallink)
print("총"+str(reallinknum)+"개의 데이터.")
try:
    # for문에 주소가 저장된 리스트를 넣고 돌림 -> 아이디와 해시태그를 가지고옴
    for i in range(0,reallinknum):
        csvtext.append([])
        req = Request('https://www.instagram.com/p'+reallink[i],headers={'User-Agent': 'Mozilla/5.0'})

        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage,"lxml",from_encoding='utf-8')
        soup1 = soup.find("meta",attrs={"property":"og:description"}) #아이디의 메타태그의 property는 og:description
        
        reallink1 = soup1['content']
        reallink1 = reallink1[reallink1.find("@")+1:reallink1.find(")")]
        reallink1 = reallink1[:20]
        if reallink1 == '':
            reallink1 = 'Null'
        csvtext[i].append(reallink1)
        
        for reallink2 in soup.find_all("meta",attrs={"property":"instapp:hashtags"}): #해시태그의 메타태그이 property는 instapp:hashtags
            reallink2 = reallink2['content']
            csvtext[i].append(reallink2)
 
        # data to CSV 먼저 .txt형식으로 저장 후 .csv형식으로 다시 저장

        #file = pd.read_csv('insta.txt', delimiter ='\t')


        print(str(i+1)+"개의 데이터 받아오는 중.")
        print(csvtext)
        data = pd.DataFrame(csvtext)
        data.to_csv('insta.txt', encoding='utf-8')  
                           
except:
    print("오류발생"+str(i+1)+"개의 데이터를 저장합니다.")   
    
    data = pd.DataFrame(csvtext)
    data.to_csv('insta.txt', encoding='utf-8')  
print("저장성공")   