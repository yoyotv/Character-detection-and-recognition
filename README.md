# Character-detection-and-recognition
Simple way to detect the character or numbers and recognize them.


## Approach 

This repository is focus on recognizing the deformation characters and numbers.

  Firsy of all, we apply the simplest strategy to detect the characters and numbers, which is the edge detection. By doing so, we are able to find where is the ROI (Region of interest). Also we have to use some algorithm to filter some interference. e.g., opencv cv2.dilate.
  After we obtain the characters and numbers, we feed them into classification network. In this repository, we utilize ResNet20. Then we are able to see the results!
  
Here is the flow chart.

   <img src="https://raw.githubusercontent.com/yoyotv/Character-detection-and-recognition/master/figures/cha.jpg" >
  
## GET started

You have to install

1. [Opencv](https://opencv.org/)  for read image and detect face, I use 2.4.9

2.  [Caffe](https://github.com/BVLC/caffe) for classify.

## Installation

1. Clone the repository
  ```Shell
  # Make sure to clone with --recursive
  git clone https://github.com/yoyotv/Raspberry-implementation.git
  ```
2. Replace the original caffe/tools/extract_feature.cpp with the new extract_feature.cpp file

3. Add the face_id fold under caffe/models

4. Place fold "Face_identification_Raspberry_pi" under Desktop

5. Finished!

## Tricks

1. Detect : Assume that the different word is not connected, we can acquire the word by connect every bright pixel which is next to one another. E.g., if the bright pixels A is not in the 9 square area of bright pixel B, then we could say that these two pixels are not belong to the same characater or number

2. Classify : Because there will be some character is deformation, it is hard for classifier to predict the right answer. e.g., number "3" is  nearly the same as character "w" in -90 degree. In order to resolve this scenario, the classifier will keep rotate the image from -90 degree to 90 degree if the probability of prediction is lower than 90%. This process will keep excuting until one of the prediction is higher than 90% or none of the prediction is higher than 90%, if the result is none of the prediction is higher than 90%, the system will choose the highest one as the final prediction.

## Switch the extraction model 

1. Place the caffemodel under caffe/models/face_id/

2. Change the command in "run.sh"
```
e.g.  change
./build/tools/extract_features.bin /home/pi/caffe/models/face_id/caffe_mobilenet_without_mirror_train_iter_220000.caffemodel /home/pi/caffe/models/face_id/val.prototxt pool6 /home/pi/caffe/models/face_id/features 1 txt
```
```
into
 ./build/tools/extract_features.bin /home/pi/caffe/models/face_id/name_of_model.caffemodel /home/pi/caffe/models/face_id/val.prototxt pool6 /home/pi/caffe/models/face_id/features 1 txt
```

* If you change the model, remember the dimension of feature might be changed. In this repository, the model is mobilenet_v1 with alpha=0.25, so the dimension will be 256.

* Open evaluate.cpp and modify the variable "feature_dim" and variable "model" at line 14,15, respectively.

* The name of variable "model" in evaluate.cpp refer to the folder name in folder database, if the dimension has changed because of the caffemodel, the database will also be changed. How to add new data into database or generate database will be mentioned in "Add new data into database"

## Add new data into database

1. If you wanna add new data into database, just enable the system and let system take a photo and copy the pool6.txt which is the feature file under caffe/models/face_id/features to Face_identification_Raspberry_pi/database/your_model_name/

## Example for Switch the extraction model and Add new data into database

1. I wanna change the model to [Resnet_50](https://github.com/KaimingHe/deep-residual-networks/blob/master/prototxt/ResNet-50-deploy.prototxt) and store the feature of somenoe which extracted from Resnet_50 as the database.

2. Changed the command of line 14 in run.sh to 
```./build/tools/extract_features.bin /home/pi/caffe/models/face_id/caffe_Resnet_50.caffemodel /home/pi/caffe/models/face_id/val.prototxt pool6 /home/pi/caffe/models/face_id/features 1 txt```
 
3. Place the Resnet_50.caffemodel under caffe/models/face_id/

4. Open evaluate.cpp and modify the const variable "feature_dim" and "model" to 2048 and "Resnet_50", respectively.

5. Place caffe/models/face_id/features/pool6.txt under Face_identification_Raspberry_pi/database/Resnet_50/.

6. Add name into data_list.txt.

7. Modify the val.prototxt.

## Demo

* The performance of model "mobilenet_0.25" is not good, it is trained by [CASIA-webface](https://arxiv.org/pdf/1411.7923.pdf). The top-1 accurancy is only 72%. In the demo video, the L2 distance between different database face is closed. 

* The L2 distance will be more significant if change the model to e.g. Resnet.
  
* The performance of Mobilenet_0.25_1 is so poor that use other networks will be a better choice.   
  
* I want the model as small as possible, but is seems difficult to reach the balance between performance and model size.

* In order to run as fast as possible, [MTCNN](https://arxiv.org/ftp/arxiv/papers/1604/1604.02878.pdf) is not applied, this might be the reason why causing the performance bad.

* https://youtu.be/b5_Cw5E8aCk

## Models

https://drive.google.com/open?id=18LOMbMRIF2w6etZaqH3X9DfTnhorMWIs

## Anything else?

* Train more models to play.

* Train the model with AM-softmax so that we could evaluate the angle between faces to identify person.
