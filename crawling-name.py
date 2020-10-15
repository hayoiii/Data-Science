from selenium import webdriver
import time

# 드라이버 경로 지정 (크롬 이용) -> 컴퓨터에 chromedriver 설치해야 함 (구글에 치면 다운 가능)
from selenium.common.exceptions import NoSuchElementException

output_file = open('/Users/hayeong/DataScience/project/namelist_male_actor.txt', 'w')
driver = webdriver.Chrome('/Users/hayeong/chromedriver')
isFinished = False
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
url = f'https://ko.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EB%B0%B0%EC%9A%B0'
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