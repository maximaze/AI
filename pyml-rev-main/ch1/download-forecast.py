# 기상철 데이터 수집
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL 인코딩합니다. --- (※1)
values = {
    'stnId': '109' # 서울/경기도
}
params = urllib.parse.urlencode(values)

print("params: ", params)

# 요청 전용 URL을 생성합니다. --- (※2)
# "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
url = API + "?" + params
print("url=", url)

# 다운로드합니다. --- (※3)
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)