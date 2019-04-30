import cv2
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from PIL import Image
import os
import time




for index in range(11,63):
  print index
  label = index-1
  path="/home/dl-linux/Desktop/hw/data/English/Img/GoodImg/Bmp/Sample0%s/" %index

  file_names=[]

  for all_files in os.walk(path):
    file_names=all_files[2]

    for i in range(len(file_names)):
      img = cv2.imread(path+str(file_names[i]),cv2.IMREAD_GRAYSCALE)
      #print img.shape
      #cv2.imshow("HI",img)
      #cv2.waitKey(0)


      name = '/home/dl-linux/Desktop/hw/custom_data/english/%s_%s.jpg' %(i,label)
      cv2.imwrite(name,img)












