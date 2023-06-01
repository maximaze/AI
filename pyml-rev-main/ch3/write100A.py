# 파일 이름과 데이터
filename = "a.bin"
data = [97,98,99,100] # a, b, c, d

# 쓰기 : 쓰기모드, 바이너리 모드로 오픈
with open(filename, "wb") as f:
    f.write(bytearray(data))

