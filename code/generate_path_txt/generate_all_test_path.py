import os
import random
import time


"""
data_path = '/home/dl-linux/Desktop/hw/custom_data/english_test/'

file_names=[]

for all_files in os.walk(data_path):
  file_names=all_files[2]
"""



txt = open("all_test_path.txt","w")
"""
for i in range(len(file_names)):

  number, label_jpg=file_names[i].split("_")
  label, jpg=label_jpg.split(".")
  txt.write(data_path+str(file_names[i]) + ' ' + str(label) +'\n')
"""


data_path = '/home/dl-linux/Desktop/hw/custom_data/test/'

file_names=[]

for all_files in os.walk(data_path):
  file_names=all_files[2]


for i in range(len(file_names)):

  number, label_jpg=file_names[i].split("_")
  label, jpg=label_jpg.split(".")
  txt.write(data_path+str(file_names[i]) + ' ' + str(label) +'\n')

data_path = '/home/dl-linux/Desktop/hw/custom_data/english_test_2/'

file_names=[]

for all_files in os.walk(data_path):
  file_names=all_files[2]


for i in range(len(file_names)):

  number, label_jpg=file_names[i].split("_")
  label, jpg=label_jpg.split(".")
  txt.write(data_path+str(file_names[i]) + ' ' + str(label) +'\n')










txt.close()

