import pandas as pd
from sklearn import svm, metrics

# 학습 데이터
tr_input = [
    [0, 0, 0],
    [2, 1, 1],
    [3, 1, 1],
    [4, 0, 0],
    [5, 2, 1],
    [6, 3 ,1],
    [7, 0, 0],
    [8, 3, 1],
    [9, 2, 1],
    [5, 0, 0],
    [4, 2, 1],
    [0, 1, 0],
    [0, 9, 0]
]

# 테스트 데이터
test_data = [
    [2, 0],
    [3, 0],
    [0, 0],
    [5, 0],
    [6, 0],
    [0, 0],
    [8, 0],
    [9, 0],
    [0, 0],
    [4, 0],
    [2,1],
    [3,2],
    [0,3],
    [5,4],
    [6,5],
    [0,6],
    [8,7],
    [9,8],
    [0,9],
    [4,10]
]
    
# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
df = pd.DataFrame(tr_input)
data  = df.loc[:,0:1] # 데이터
print("데이터")
print('data: ', data)

label = df.loc[:,2]   # 레이블
print("레이블")
for lb in label:
    print('label: ',label)
    
# 데이터 학습 --- (※2)
# kernel : "rbf"
clf = svm.SVC(kernel= 'linear')
clf.fit(data, label)

# 서포트 백터 확인
print("서포트 확인")
print(clf.support_vectors_)

# 예측 --- (#3)
print("예측(predict)")
for test in test_data:
    pre = clf.predict([test]) # 하나씩 예측
    print("test: ", test, 'pre: ',pre)
    



