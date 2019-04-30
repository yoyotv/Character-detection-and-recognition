import caffe

import numpy as np
import cv2
from PIL import Image
import time
import math
import os

threshold_acc=0.9

data_path = '/home/dl-linux/Desktop/hw/character'

file_names=[]

dict=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


for all_files in os.walk(data_path):
  file_names=all_files[2]

the_number_of_character = len(file_names)

angle=0


def rotate(img, angle, scale=1.0):
  h = img.shape[0]
  w = img.shape[1]
  center = (w/2,h/2)
  M = cv2.getRotationMatrix2D(center, angle, scale)
  rotated = cv2.warpAffine(img, M, (w,h))
  return rotated
  



model='evaluate/deploy.prototxt'

weights='evaluate/solver_iter_10000.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(0)

net1=caffe.Net(model,weights,caffe.TEST)

ans_all = np.full((5,2),-1.0)
##
#the_number_of_character=1
##
i=0
while i < the_number_of_character:

  img_name = "character/%s.jpg" %str(i)
  img = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
  #img = cv2.imread("evaluate/a.jpg",cv2.IMREAD_GRAYSCALE)

  img = cv2.resize(img,(32,32))
  cv2.imshow("HI",img)

  img = rotate(img,angle)
  cv2.imshow("HI1",img)


  #print img.shape
  cv2.waitKey(0)


  img = np.resize(img,(1,32,32))
  img = np.expand_dims(img,axis=0)

  net1.blobs['data'].reshape(*img.shape)


  net1.blobs['data'].data[0]=img


  determine = net1.forward()


  ans=str(np.argmax(determine['softmax'][0]))
  ans_prob=str(determine['softmax'][0][np.argmax(determine['softmax'][0])])

  i=i+1

  if float(ans_prob)>=threshold_acc or angle == -45:
    ans_all[4][0] = ans
    ans_all[4][1] = float(ans_prob)
    print ans_all
    _, final_ans_index=np.argmax(ans_all,axis=0)
    final_ans = ans_all[final_ans_index][0]
    final_ans_prob = ans_all[final_ans_index][1]
    print "Determine is  : " + str(dict[int(final_ans)])
    print "Probability is : " + str(final_ans_prob)
    ans_all = np.full((5,2),-1.0)


  if determine['softmax'][0][np.argmax(determine['softmax'][0])] < threshold_acc and angle != -45:

    i=i-1
    if angle == 0:
      angle = 22.5
      ans_all[0][0] = ans
      ans_all[0][1] = float(ans_prob)
    elif angle == 22.5:
      angle = 45
      ans_all[1][0] = ans
      ans_all[1][1] = float(ans_prob)
    elif angle == 45:
      angle = -45
      ans_all[2][0] = ans
      ans_all[2][1] = float(ans_prob)
    elif angle == -45:
      angle = -22.5
      ans_all[3][0] = ans
      ans_all[3][1] = float(ans_prob)
  else:
    angle=0


