# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:15:19 2021

@author: user
"""

import os
import pickle
import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt
#%matplotlib inline
from tqdm import tqdm
from PIL import Image

img_path = 'C:/aiffel/lms_practice/data/cv_practice.png'
img = cv.imread(img_path)

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([100,100,100])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img,img, mask= mask)

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv.cvtColor(mask, cv.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv.cvtColor(res, cv.COLOR_BGR2RGB))
plt.show()

#%%
file_path = 'C:/aiffel/lms_practice/data/cifar-100-python/images'
train_file_path = os.path.join(file_path, 'train')
img_path = os.path.join(file_path, 'cifar-images')

def draw_color_histogram_from_image(file_name):
    img_full_path = os.path.join(file_path, file_name)
    # 이미지 열기
    img = Image.open(img_full_path)
    cv_image = cv.imread(img_full_path)

    # Image와 Histogram 그려보기
    f=plt.figure(figsize=(10,3))
    im1 = f.add_subplot(1,2,1)
    im1.imshow(img)
    im1.set_title("Image")

    im2 = f.add_subplot(1,2,2)
    color = ('b','g','r')
    for i,col in enumerate(color):
        # image에서 i번째 채널의 히스토그램을 뽑아서(0:blue, 1:green, 2:red)
        histr = cv.calcHist([cv_image],[i],None,[256],[0,256])   
        im2.plot(histr,color = col)   # 그래프를 그릴 때 채널 색상과 맞춰서 그립니다.
    im2.set_title("Histogram")
    
draw_color_histogram_from_image('adriatic_s_001807.png')
