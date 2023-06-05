import pandas as pd
from sklearn import svm, metrics

# 학습 데이터
tr_input = [
    [2,1,1],
    [3,1,1],
    [4,0,0],
    [5,2,1],
    [6,3,1],
    [7,0,0],
    [8,3,1],
    [9,2,1],
    [5,0,0],
    [4,2,1]
]

# 테스트 데이터
test_data = [
    [2,1],
    [3,1],
    [4,0],
    [5,2],
    [6,3],
    [7,0],
    [8,3],
    [9,2],
    [5,0],
    [4,2]
]


# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
df = pd.DataFrame(tr_input)
data  = df.loc[:,0:1] # 데이터
print("# 데이터")
print('data: ', data)
    
label = df.loc[:,2]   # 레이블
print("# 레이블")
for lb in label:
    print('label: ', lb)
    
# 데이터 학습 --- (※2)
# kernel : "rbf"
clf = svm.SVC(kernel= 'linear')
clf.fit(data, label)

# 예측  --- (※3)
pre = clf.predict(test_data)

print("# 레이블 vs 정답")
for idx, lb in enumerate(label):
    print(f"label:{lb}, pre:{pre[idx]}")

# 정답률 구하기 --- (※4)
ac_score = metrics.accuracy_score(label, pre)
print("정답률 =", ac_score)
