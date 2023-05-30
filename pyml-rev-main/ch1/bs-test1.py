# 라이브러리 읽어 들이기 --- (※1)
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML --- (※2)
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
  <p>11</p>
</body></html>
"""

# HTML 분석하기 --- (※3)
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출하기 --- (※4)
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling    # 줄바꿈(\n)을 추출
p3 = p2.next.sibling

# 요소의 글자 출력하기 --- (※5)
print("h1 = " + h1.string)
print("p  = " + p1.string)
print("p  = " + p2.string)
print("p  = " + p3.string)