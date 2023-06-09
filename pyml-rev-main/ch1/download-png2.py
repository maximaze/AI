import urllib.request 

# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드 --- (※1)
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기 --- (※2)
# savename : 저장할 파일이름
# mode : "w" 쓰기모드, "b" 바이너리(2진포맷)
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다...!")