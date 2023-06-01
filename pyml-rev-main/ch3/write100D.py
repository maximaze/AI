# 파일 이름과 데이터
filename = "a.bin"

# 문자열(UTF-8)을 바이트로 변환
data = 'Hi!안녕?'.encode('utf-8')

print('encode(utf-8):', data)
print('decode(utf-8):', data.decode())
print('decode(utf-8):', data.decode('utf-8'))

# 쓰기 : 쓰기모드, 바이너리 모드로 오픈
with open(filename, "wb") as f:
    f.write(bytearray(data))

