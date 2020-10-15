from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

name_list_women_singer = open('/Users/iseungjin/namelist_women_singer.txt', 'w')
url = ["https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pageuntil=%EB%82%98%ED%9D%AC%EA%B2%BD#mw-pages",
       "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pagefrom=%EB%82%98%ED%9D%AC%EA%B2%BD#mw-pages",
       "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pagefrom=%EB%B3%B4%EC%95%84#mw-pages",
       "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pagefrom=%EC%97%AC%EB%A6%B0+%281994%EB%85%84%29#mw-pages",
       "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pagefrom=%EC%9D%B4%EC%A7%84+%281980%EB%85%84%29#mw-pages",
       "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pagefrom=%EC%B2%9C%EC%9E%AC%EC%9D%B8#mw-pages"]

htmlgg = urlopen("https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pageuntil=%EB%82%98%ED%9D%AC%EA%B2%BD#mw-pages")
s = BeautifulSoup(htmlgg, "html.parser")
t = s.select('.mw-category-group a')
#print(t)

for line in url:
    html = urlopen(line)
# html = urlopen("https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EA%B0%80%EC%88%98&pageuntil=%EB%82%98%ED%9D%AC%EA%B2%BD#mw-pages")
    bsObject = BeautifulSoup(html, "html.parser")

    list = []

    test = bsObject.select('.mw-category-group a')

    for name in test:
        name_text = name.text
        # 괄호 없애기
        if '(' in name_text:
            start = name_text.find('(')
            name_text = name_text[:start]
            name_text.strip()
        else:
            list.append(name_text)
            continue

        list.append(name_text)

    print(list)

    name_list_women_singer.write(str(list))


