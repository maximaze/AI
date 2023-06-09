# 손글찌 예측
# https://www.tensorflow.org/datasets/catalog/mnist?hl=ko

from tensorflow.keras.datasets import mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import utils

# https://codetorial.net/matplotlib/subplot.html
# https://matplotlib.org
import matplotlib.pyplot as plt

# MNIST 데이터 읽어 들이기 --- (※1)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#%%
# 이미지 데이터 출력

for x in range(10):
    fig = plt.figure()
    ax = fig.add_subplot(1,3,1)
    ax.imshow(X_train[x])





