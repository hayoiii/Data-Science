from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

##### 지정해야 할 변수들 #####
# 연예인 이름 리스트 파일
output_file = open('/Users/hayeong/DataScience/project/namelist_male_actor.txt', 'w')
# 드라이버 경로 지정 (크롬 이용) -> 컴퓨터에 chromedriver 설치해야 함 (구글에 치면 다운 가능)
driver = webdriver.Chrome('/Users/hayeong/chromedriver')
# 크롤링 할 url: 위키피디아 '분류:대한민국의 남자/여자 배우/가수'
url = f'https://ko.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EB%B0%B0%EC%9A%B0'


# 다음 페이지가 없을 때 True
isFinished = False
# 크롤링한 이름의 개
count = 0


# 다음 페이지 버튼 클릭하기
def click_next_page():
    div = driver.find_element_by_id('mw-pages')
    try:
        if div.find_element_by_link_text('다음 페이지').is_displayed():
            div.find_element_by_link_text('다음 페이지').click()
            time.sleep(1)
            return False
        else:
            return True

    except NoSuchElementException:
        print("ㅡ No more next page ㅡ")
        return True


print("ㅡ 크롤링 시작 ㅡ")
driver.get(url)
driver.maximize_window()

output_file.write('\n')
while not isFinished:
    div = driver.find_element_by_xpath('//*[@id="mw-pages"]/div/div')
    a_list = div.find_elements_by_tag_name('a')

    for i in range(len(a_list)):
        name = a_list[i].get_attribute('title')
        output_file.write(name+'\n')
        count += 1

    print('누적 크롤링 횟수:', count)
    isFinished = click_next_page()


output_file.close()