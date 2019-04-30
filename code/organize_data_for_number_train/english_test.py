import cv2
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from PIL import Image
import os
import time





path="/home/dl-linux/Desktop/hw/custom_data/english/"

for all_files in os.walk(path):
    file_names=all_files[2]
    for i in range(len(file_names)/10*3,len(file_names)):
    #for i in range(len(file_names)/10*3):
      img = cv2.imread(path+str(file_names[i]),cv2.IMREAD_GRAYSCALE)
      #print img.shape
      #cv2.imshow("HI",img)
      #cv2.waitKey(0)

      name = '/home/dl-linux/Desktop/hw/custom_data/english_train/%s' %file_names[i]
      #name = '/home/dl-linux/Desktop/hw/custom_data/english_test/%s' %file_names[i]
      cv2.imwrite(name,img)












