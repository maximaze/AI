# 라이브러리 읽어 들이기 --- (※1)
import urllib.request

# URL과 저장 경로 지정하기
# 공유기능이 켜져있어야 다운로드가 정상작동됨
url = "http://p4.wallpaperbetter.com/wallpaper/424/968/982/windows-10-night-sky-wallpaper-preview.jpg"
savename = "test.png"

# 다운로드 --- (※2)
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")