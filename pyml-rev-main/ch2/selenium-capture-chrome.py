from selenium.webdriver import Chrome, ChromeOptions

url = "http://www.naver.com/"

# Firefox를 헤드리스 모드로 설정하는 옵션 --- (※1)
options = ChromeOptions()
# options.add_argument('-headless') # 브라우저를 화면에 띄우지 않고 캡쳐
options.add_argument('start-maximized')

# PhantomJS 드라이버 추출하기 --- (※2)
browser = Chrome(options=options)

# URL 읽어 들이기 --- (※3)
browser.get(url)

# 화면을 캡처해서 저장하기 --- (※4)
browser.save_screenshot("Chrome.png")

# 브라우저 종료하기 --- (※5)
browser.quit()
