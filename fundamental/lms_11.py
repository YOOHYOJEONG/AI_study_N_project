# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:53:25 2021

@author: user
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_wine()

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state = 11)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("정답률 : ", accuracy_score(y_test, y_pred))