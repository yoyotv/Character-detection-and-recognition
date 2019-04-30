import numpy as np
import cv2
import time

#img_name = 'rocc.jpg'
img_name = 'aa.jpg'
the_memory_size_of_a_character=10000
#the smaller the stricter
overlap_threshold = 0.8
wide_crop = False



def convert_to_binary(cropped_img):
  print cropped_img.shape
  _,cropped_img=cv2.threshold(cropped_img,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  for i in range(cropped_img.shape[0]):
    for j in range(cropped_img.shape[1]):
      if cropped_img[i][j] == 255:
        cropped_img[i][j] = 0
      else:
        cropped_img[i][j] =255
  return cropped_img



def other_in_nine_square(img,current_position, current_character):
  i = current_position[0]
  j = current_position[1]
  ori_num  = current_character.shape[0]
  if i+1<360 and j+1<480:
    if img[i-1][j-1] == 255:
      current_character = np.append(current_character,[[i-1,j-1]],axis=0)
      img[i-1][j-1] = 0
    if img[i-1][j] == 255:
      current_character = np.append(current_character,[[i-1,j]],axis=0)
      img[i-1][j] = 0
    if img[i-1][j+1] == 255:
      current_character = np.append(current_character,[[i-1,j+1]],axis=0)
      img[i-1][j+1] = 0
    if img[i][j-1] == 255:
      current_character = np.append(current_character,[[i,j-1]],axis=0)
      img[i][j-1] = 0
    if img[i][j+1] == 255:
      current_character = np.append(current_character,[[i,j+1]],axis=0)
      img[i][j+1] = 0
    if img[i+1][j-1] == 255:
      current_character = np.append(current_character,[[i+1,j-1]],axis=0)
      img[i+1][j-1] = 0
    if img[i+1][j] == 255:
      current_character = np.append(current_character,[[i+1,j]],axis=0)
      img[i+1][j] = 0
    if img[i+1][j+1] == 255:
      current_character = np.append(current_character,[[i+1,j+1]],axis=0)
      img[i+1][j+1] = 0
    if ori_num != current_character.shape[0]:
      return img, current_character, True
    else:
      return img, current_character, False
  else:
    return img, current_character, False
  


def find_the_first_light_position_for_current_character(img):
  for i in range(img.shape[1]):
    for j in range(img.shape[0]):
      if img[j][i] == 255:
        return j, i

def is_in(matrix,array):
  print (matrix.shape[0])
  for i in range(matrix.shape[0]):
    if np.array_equal(array,matrix[i]) is True:
      return True
  return False

def overlap_area(all_img_coordinate,current_coordinate):

  c_i_min,c_j_min = current_coordinate[0]
  c_i_max,c_j_min = current_coordinate[1]
  c_i_min,c_j_max = current_coordinate[2]
  c_i_max,c_j_max = current_coordinate[3]
  c_h = c_i_max - c_i_min
  c_w = c_j_max - c_j_min

  for k in range(0,all_img_coordinate.shape[0],4):
    width = -2
    height = -2
    i_min,j_min = all_img_coordinate[k]
    i_max,j_min = all_img_coordinate[k+1]
    i_min,j_max = all_img_coordinate[k+2]
    i_max,j_max = all_img_coordinate[k+3]
    h = i_max - i_min
    w = j_max - j_min

    if c_j_max > j_max:
      for j in range(c_j_min,c_j_max):
        if j == j_max:
          width = j_max - c_j_min
        elif j == c_j_max-1 and width != j_max - c_j_min:
          width = -1
    else:
      for j in range(j_min,j_max):
        if j == c_j_max:
          width = c_j_max - j_min
          if width > c_w:
            width = c_w
        elif j == j_max-1 and width != c_w and width != c_j_max - j_min:
          width = -1

    if c_i_max > i_max:
      for i in range(c_i_min,c_i_max):
        if i == i_max:
          height = i_max - c_i_min
        elif i == c_i_max-1 and height != i_max - c_i_min:
          height = -1
    else:
      for i in range(i_min,i_max):
        if i == c_i_max:
          height = c_i_max - i_min
          if height > c_h:
            height = c_h
        elif i == i_max-1 and height != c_h and height != c_i_max - i_min:
          height = -1

    if width> 0 and height >0:
      overlap = width*height
    else:
      overlap = 0

    if overlap/float(c_h*c_w) > overlap_threshold:
      return True

  return False

#############################################################################################
#START


ori_RGB_img = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
ori_RGB_img = cv2.resize(ori_RGB_img, (480,360))

#This part is edge detection by cv2#####
img1=cv2.GaussianBlur(ori_RGB_img,(5,5),0)   #                                         
canny=cv2.Canny(img1,200,100)          #
cv2.imwrite('edge.jpg',canny)          #
########################################




img = cv2.imread("edge.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (480,360))
cv2.imshow("HI1",img)
print img.shape

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1, 1))
#increase 1,1 , the edge of charactere will increase
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))


ori_img = cv2.dilate(img,kernel)
img = cv2.dilate(img,kernel)





for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    if img[i][j] > 100:
      img[i][j] = 255
    else :
      img[i][j] = 0


cv2.imshow("HI2",img)
cv2.waitKey(0)
#################################

character_index=0
the_number_of_point_of_all_character = [0]
while np.sum(img) != 0:

  current_character = np.full((1,2),-1)

  current_character[0][0], current_character[0][1] =find_the_first_light_position_for_current_character(img)
  a,b = current_character[0][0], current_character[0][1]

  for i in range(the_memory_size_of_a_character):
    if i < current_character.shape[0]:
      current_position = current_character[i]
      img, current_character, ans = other_in_nine_square(img, current_position, current_character)
    else:
      break

  the_number_of_point_of_current_character = current_character.shape[0]
  the_number_of_point_of_all_character.append(the_number_of_point_of_current_character)


  i_max_index, j_max_index = np.argmax(current_character,axis=0)
  i_min_index, j_min_index = np.argmin(current_character,axis=0)

  i_max, _ = current_character[i_max_index]
  _, j_max = current_character[j_max_index]
  i_min, _ = current_character[i_min_index]
  _, j_min = current_character[j_min_index]
###############################################################

  current_coordinate = np.asarray([[i_min,j_min],[i_max,j_min],[i_min,j_max],[i_max,j_max]])
  
  try :
    all_character
  except NameError:
    if (i_max-i_min)*(j_max-j_min)/float(360*480)<0.5:
      all_character = current_character
      all_img_coordinate = current_coordinate
      if i_min-10>0 and j_min-10>0 and i_max+10<360 and j_max+10<480 and wide_crop == True:
        i_min = i_min-10
        j_min = j_min-10
        i_max = i_max+10
        j_max = j_max+10
        cropped_img = np.asarray(ori_RGB_img[i_min:i_min+(i_max-i_min),j_min:j_min+(j_max-j_min)])
      else:
        #tight crop
        cropped_img = np.asarray(ori_RGB_img[i_min:i_min+(i_max-i_min),j_min:j_min+(j_max-j_min)])

      cv2.imshow("HI3",cropped_img)
      name = "character/%s.jpg" %(character_index)
      cropped_img = convert_to_binary(cropped_img)
      cv2.imwrite(name, cropped_img)
      cv2.imshow("HI4",img)
      cv2.waitKey(0)
      character_index = character_index + 1
  else:
##########################################################
#find the crop rectangle
    if (i_max-i_min)*(j_max-j_min)/float(360*480)<0.5:
      print (i_max-i_min)*(j_max-j_min)/(360*480)
      if overlap_area(all_img_coordinate,current_coordinate) is False :
        all_character = np.append(all_character,current_character,axis=0)
        all_img_coordinate = np.append(all_img_coordinate,current_coordinate,axis=0)

      #wide crop
        if i_min-10>0 and j_min-10>0 and i_max+10<360 and j_max+10<480 and wide_crop == True:
          i_min = i_min-10
          j_min = j_min-10
          i_max = i_max+10
          j_max = j_max+10
          cropped_img = np.asarray(ori_RGB_img[i_min:i_min+(i_max-i_min),j_min:j_min+(j_max-j_min)])
        else:
          #tight crop
          cropped_img = np.asarray(ori_RGB_img[i_min:i_min+(i_max-i_min),j_min:j_min+(j_max-j_min)])

        cv2.imshow("HI3",cropped_img)
        name = "character/%s.jpg" %(character_index)
        cropped_img = convert_to_binary(cropped_img)
        cv2.imwrite(name,  cropped_img)
        cv2.imshow("HI4",img)
        cv2.waitKey(0)
        character_index = character_index + 1
#####################################

cv2.imshow("HI5",img)

for i in range(all_character.shape[0]):
  x, y = all_character[i]
  img[x][y] = 255




cv2.imshow("HI6",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




#
#divide the character




