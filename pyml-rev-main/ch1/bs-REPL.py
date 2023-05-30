from bs4 import BeautifulSoup

soup = BeautifulSoup(
    "<p><a href='a.html'>test</a></p>",
    "html.parser"
    )

# 분석이 제대로 됐는지 확인
print('prettify:',soup.prettify())

a = soup.p.a

print('type(a): ',type(a.attrs))

print('href 속성을 가지고 있는가?','href' in a.attrs)

print(a['href'])


