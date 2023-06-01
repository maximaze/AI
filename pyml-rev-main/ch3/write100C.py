# 파일 이름과 데이터
filename = "a.bin"
data = b'hello,world!'

# 쓰기 : 쓰기모드, 바이너리 모드로 오픈
with open(filename, "wb") as f:
    f.write(bytearray(data))

