import cv2
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from PIL import Image




def rgb2gray(matrix):
  return np.dot(matrix[...,:3],[0.2989,0.5870,0.1140])[:][:]



mat = scipy.io.loadmat("data/extra_32x32.mat")



y = np.asarray(mat['y'])
X = np.asarray(mat['X'])

X = np.swapaxes(X, 2, 3)
X = np.swapaxes(X, 1, 2)
img = np.swapaxes(X, 0, 1)





for i in range(img.shape[0]):
  gray = rgb2gray(img[i])
  label = int(y[i])
  if label == 10:
    label = 0
  name = 'custom_data/extra/%s_%s.jpg' %(i,label)
  cv2.imwrite(name,gray)





