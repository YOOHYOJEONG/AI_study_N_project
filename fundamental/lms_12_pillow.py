# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:44:47 2021

@author: user
"""

import numpy as np
from PIL import Image
import os
import pickle
from tqdm import tqdm

data = np.zeros([32, 32, 3], dtype = np.uint8)
#black image
image = Image.fromarray(data, 'RGB')
image

#red image
data[:,:] = [255,0,0]
image = Image.fromarray(data, 'RGB')
image

#white image
data[:,:] = [255,255,255]
image = Image.fromarray(data, 'RGB')
image

#%%
img_path = 'C:/aiffel/lms_practice/pillow_practice.png'
img = Image.open(img_path)

print('width:', img.width)
print('height:', img.height)

new_img_path = 'C:/aiffel/lms_practice/pillow_practice_new.jpg'
img = img.convert('RGB')
img.save(new_img_path)

#image resizing 
resized_img = img.resize((100,200))

#%%
resized_img_path = 'C:/aiffel/lms_practice/pillow_practice_resized.png'
resized_img.save(resized_img_path)

#image crop
crop_img = img.crop((300,100, 600, 4000))

crop_img_path = 'C:/aiffel/lms_practice/pillow_practice_crop.png'
crop_img.save(crop_img_path)

#%%
dir_path = 'C:/aiffel/lms_practice/cifar-100-python'
train_file_path = os.path.join(dir_path, 'train')

with open(train_file_path, 'rb') as f :
    train = pickle.load(f, encoding = 'bytes')

print(type(train))

data1 = train[b'data'][0].shape
print(data1)

img_data = train[b'data'][0].reshape([32,32,3], order = 'F')
img_data = img_data.swapaxes(0,1)
img = Image.fromarray(img_data)

#%%
img_save_path = 'C:/aiffel/lms_practice/cifar-100-python/images'
if not os.path.exists(img_save_path) :
    os.mkdir(img_save_path)
    
with open(train_file_path, 'rb') as f :
    train = pickle.load(f, encoding = 'bytes')
    for i in tqdm(range(len(train[b'filenames']))):
        filename = train[b'filenames'][i].decode()
        data = train[b'data'][i].reshape([32,32,3], order = 'F')
        img = Image.fromarray(data.swapaxes(0,1))
        img.save(os.path.join(img_save_path, filename))
        
