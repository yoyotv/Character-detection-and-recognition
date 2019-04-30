import numpy as np 
import pandas
import matplotlib.pyplot as plt
import cv2
import os
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras import backend as K
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
#ignore warning messages 
import warnings
warnings.filterwarnings('ignore') 



dataset = pandas.read_csv("A_Z Handwritten Data.csv").astype("float32")

dataset.rename(columns={'0':'label'},inplace=True)

X=dataset.drop('label',axis = 1)
y = dataset['label']

print X.shape
print len(X.iloc[1])

# splite the data
X_train, X_test, y_train, y_test = train_test_split(X,y)

# scale data
standard_scaler = MinMaxScaler()
standard_scaler.fit(X_train)

X_train = standard_scaler.transform(X_train)
X_test = standard_scaler.transform(X_test)

print("Data after scaler")
#X_shuffle = shuffle(X_train)

print X_train.shape

print X_train[0].shape

print X_test.shape

print X_test[0].shape

print y_train.shape

print y_test.shape






path="/home/dl-linux/Desktop/hw/custom_data/english_train_2/"

for i in range(X_train.shape[0]):
  img = X_train[i].reshape(28,28)*256
  cv2.imwrite(path+str(i)+"_"+str(int(np.asarray(y_train)[i])+10)+".jpg",img)


path="/home/dl-linux/Desktop/hw/custom_data/english_test_2/"

for i in range(X_test.shape[0]):
  img = X_test[i].reshape(28,28)*256
  cv2.imwrite(path+str(i)+"_"+str(int(np.asarray(y_test)[i])+10)+".jpg",img)








