# 손글찌 예측
# https://www.tensorflow.org/datasets/catalog/mnist?hl=ko

from tensorflow.keras.datasets import mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import utils

# MNIST 데이터 읽어 들이기 --- (※1)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 데이터를 float32 자료형으로 변환하고 정규화하기 --- (※2)
X_train = X_train.reshape(60000, 784).astype('float32')
X_test  = X_test.reshape(10000, 784).astype('float')
X_train /= 255
X_test  /= 255

# 레이블 데이터를 0-9까지의 카테고리를 나타내는 배열로 변환하기 --- (※2a)
y_train = utils.to_categorical(y_train, 10)
y_test  = utils.to_categorical(y_test, 10)

# 모델 구조 정의하기 --- (※3)
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))

# 모델 구축하기 --- (※4)
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(), # 최적화 알고리즘(Adaptive Moment Estimation), AdaGrad + RMSprop
    metrics=['accuracy'])

# 데이터 훈련하기 --- (※5)
hist = model.fit(X_train, y_train)

# 테스트 데이터로 평가하기 --- (※6)
score = model.evaluate(X_test, y_test, verbose=1)
print('loss=', score[0])
print('accuracy=', score[1])

#%%
# 예측

import random
import numpy as np
from numpy import argmax

# 검증 데이터의 갯수로 난수를 발생해서 5개 선택
xhat_idx = np.random.choice(X_test.shape[0],5)
print("예측용 인덱스 데이터: ", xhat_idx)

xhat = X_test[xhat_idx] # 5*784
yhat = model.predict(xhat)

print("예측결과 : ", yhat)

for x in range(5):
    print('#True: ', str(argmax(y_test[xhat_idx[x]])), ', predict:', str(yhat[x]))
