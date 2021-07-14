# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:14:00 2021

@author: user
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# # 바꿔 볼 수 있는 하이퍼파라미터들
# n_channel_1=30
# n_channel_2=32
# n_dense= 50
# n_train_epoch=15


mnist = keras.datasets.mnist

(x_train, y_train), (x_test,y_test) = mnist.load_data() 
x_train_norm, x_test_norm = x_train / 255.0, x_test / 255.0

# 데이터갯수에 -1을 쓰면 reshape시 자동계산 됨.
x_train_reshaped=x_train_norm.reshape( -1, 28, 28, 1)
x_test_reshaped=x_test_norm.reshape( -1, 28, 28, 1)


model=keras.models.Sequential()
model.add(keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(28,28,1)))
#16 : 얼마나 다양한 이미지의 특징을 살펴 볼 건지(입력 이미지가 다양할 수록 더 많은 특징을 고려해보기)
#input_shape : 입력 이미지의 형태
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(32, (3,3), activation='relu'))
#32 : 얼마나 다양한 이미지의 특징을 살펴 볼 건지
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(32, activation='relu'))
#32 : 분류가 알고리즘을 얼마나 복잡하게 할 것인지(복잡한 문제일수록 해당 수를 늘려보기)
model.add(keras.layers.Dense(10, activation='softmax'))
#10 : 최종 분류기의 class 수. 여기서는 0~9까지 총 10개의 class를 구분하니까 10이 됨.

model.summary()

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

model.fit(x_train_reshaped, y_train, epochs=10)


test_loss, test_accuracy = model.evaluate(x_test_reshaped,y_test, verbose=2)


#evaluate()대신 predict() 사용하면 model이 추론한 확률 분포를 출력할 수 있음.
# model이 추론한 확률값
predicted_result = model.predict(x_test_reshaped)
predicted_labels = np.argmax(predicted_result, axis=1)

# 모델 시험
test_loss, test_accuracy = model.evaluate(x_test_reshaped, y_test, verbose=2)
print("test_loss: {} ".format(test_loss))
print("test_accuracy: {}".format(test_accuracy))