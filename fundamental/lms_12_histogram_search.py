# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:53:51 2021

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


def get_histogram(image) : 
    histogram = []
    
    for i in range(3) :
        channel_histogram  = cv.calcHist(images = [image], channels = [i]
                                         ,mask = None, histSize = [4], 
                                         ranges = [0,256])
        histogram.append(channel_histogram)
        
    histogram = np.concatenate(histogram)
    histogram = cv.normalize(histogram, histogram)
    
    return histogram


def build_histogram_db() :
    histogram_db = {}
    
    path = images_dir_path
    file_list = os.listdir(images_dir_path)
    
    for file_name in tqdm(file_list) :
        file_path = os.path.join(images_dir_path, file_name)
        image = cv.imread(file_path)
        histogram = get_histogram(image)
        
        histogram_db[file_name] = histogram
        
    return histogram_db


def get_target_histogram() :
    filename = input("파일 명 : ")
    if filename not in histogram_db :
        print("없는 파일입니다.")
        
        return None
        
    return histogram_db[filename]


def search(histogram_db, target_histogram, top_k=5) :
    results = {}
    
    for file_name, histogram in tqdm(histogram_db.items()):
        distance = cv.compareHist(H1 = target_histogram,
                                  H2 = histogram,
                                  method = cv.HISTCMP_CHISQR)
        results[file_name] = distance
        
    results = dict(sorted(results.items(), 
                         key = lambda item : item[1])[:top_k])
    
    return results


def show_result(result) :
    f = plt.figure(figsize = (10,3))
    for idx, filename in enumerate(result.keys()):
        img_path = os.path.join(images_dir_path, filename)
        im = f.add_subplot(1, len(result), idx +1)
        img = Image.open(img_path)
        im.imshow(img)

dir_path = 'C:/aiffel/lms_practice/cifar-100-python'
train_file_path = os.path.join(dir_path, 'train')

with open(train_file_path, 'rb') as f :
    train = pickle.load(f, encoding = 'bytes')

images_dir_path = 'C:/aiffel/lms_practice/cifar-100-python/images'

# #get_histogram test
# filename = train[b'filenames'][0].decode()
# file_path = os.path.join(images_dir_path, filename)
# image = cv.imread(file_path)
# histogram = get_histogram(image)
# histogram

# #build_histogram_db test
histogram_db = build_histogram_db()
# print(histogram_db['adriatic_s_001807.png'])

target_histogram = get_target_histogram()
#print(target_histogram)

result = search(histogram_db, target_histogram)
#print(result)

show_result(result)

