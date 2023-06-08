# 넘파이 : numpy
# 다차원 배열
# 모든 원소는 동일한 자료형으로 구성

import numpy as np


# 2차원 배열
# list -> ndarray
lst = [[1,3,5,7],
       [2,4,6,8]]

print(lst)

ndx = np.array(lst)

print(type(ndx))
print(ndx)

#%%

print('size:', ndx.size)
print('len(ndx):', len(ndx))
print('len(ndx.data):', len(ndx.data))

#%%
# ndarray -> list
nls = ndx.tolist()
print(type(nls), nls)
print(type(ndx.data.tolist()), ndx.data.tolist())

#%%

