from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

# BMI 데이터를 읽어 들이고 정규화하기 --- (※1)
csv = pd.read_csv("bmi.csv")

# 몸무게와 키 데이터
csv["weight"] /= 100
csv["height"] /= 200
X = csv[["weight", "height"]]  # --- (※1a)

# 레이블 : 정답
bclass = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]}
y = np.empty((20000,3))
for i, v in enumerate(csv["label"]):
    y[i] = bclass[v]
    
# 훈련 전용 데이터와 테스트 전용 데이터로 나누기 --- (※2)
X_train, y_train = X[1:15001], y[1:15001]
X_test,  y_test  = X[15001:20001], y[15001:20001] 

# 모델 구조 정의하기 --- (※3)
model = Sequential()
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))       # 0, x
model.add(Dropout(0.1))             # 오류데이터를 드롭시킴
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))                 # 정답은 3가지 종류
model.add(Activation('softmax'))    # 합이 1이 되도록

# 모델 구축하기 --- (※4)
model.compile(
    loss='categorical_crossentropy',
    optimizer="rmsprop",
    metrics=['accuracy'])

# 데이터 훈련하기 --- (※5)
hist = model.fit(
    X_train, y_train,   # 훈련데이터, 정답
    batch_size=100,     # 100단위로 훈련
    epochs=20,          # 훈련회수
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)

# 테스트 데이터로 평가하기 --- (※6)
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])



#%%

# 예측
print("# 예측")
import random

xrnd = random.randrange(15001,20001)
print("예측용 난수: ", xrnd)

xpre = X[xrnd:xrnd+1]
ypre = y[xrnd:xrnd+1]
print("예측값: ", xpre)
print("정답값: ", ypre)

yhat = model.predict(xpre)
print("예측결과: ",yhat)

# 원본데이터
print("원본데이터")
print(csv.loc[xrnd])




