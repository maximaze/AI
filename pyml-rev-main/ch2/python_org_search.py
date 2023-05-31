# http://www.python.org 사이트에 접속하여
# 검색문자 "pycon" 입력 후 검색 수행

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q") # 검색어 입력 엘리먼트 객체
elem.clear()    # 검색 엘리먼트 객체 클리어
elem.send_keys("pycon")     # 검색어 입력
elem.send_keys(Keys.RETURN) # 엔터키 입력

assert "No results found." not in driver.page_source

# driver.close()    # 브라우저 창 닫기