# Character-detection-and-recognition
Simple way to detect the character or numbers and recognize them.

## Why

The general way to detect and classify is to merge them int one process, e.g. RCNN, YOLO. But we need to find the dataset, which has the position label information. We have like MS-COCO, but it is for for the charecter and number! So I am thinking I could first develop a system can recognize the word in a restricted area. The restricted area can afford the deformation characters or  numbers.

## Approach 

This repository is focus on detecting and recognizing the deformation characters and numbers.

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
  ```
  git clone https://github.com/yoyotv/Character-detection-and-recognition.git
  ```

2. Finished!

## Tricks

1. Detect : Assume that the different word is not connected, we can acquire the word by connect every bright pixel which is next to one another. E.g., if the bright pixels A is not in the 9 square area of bright pixel B, then we could say that these two pixels are not belong to the same characater or number

2. Classify : Because there will be some character is deformation, it is hard for classifier to predict the right answer. e.g., number "3" is  nearly the same as character "w" in -90 degree. In order to resolve this scenario, the classifier will keep rotate the image from -90 degree to 90 degree if the probability of prediction is lower than 90%. This process will keep excuting until one of the prediction is higher than 90% or none of the prediction is higher than 90%, if the result is none of the prediction is higher than 90%, the system will choose the highest one as the final prediction.

## Switch the classifier model 

1. Place the caffemodel and deploy file under evaluate/

2. Change the code in evaluate/go.py line 38 and 40.

## Training data

Number part
1. [MNIST](http://yann.lecun.com/exdb/mnist/)

Charactee part
1. [A-Z Handwritten Alphabets in .csv format](https://www.kaggle.com/sachinpatel21/az-handwritten-alphabets-in-csv-format)

2. [The Chars74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/)

## Demo

1. That's choose aa.jpg as our demo picture. Set the code in detect.py line 6.

2. Run ``` sh test.sh```

3. You should see 

<img src="https://raw.githubusercontent.com/yoyotv/Character-detection-and-recognition/master/figures/edge.jpg" >

4. Keep press "Enter" to enable system.

5. As you press "Enter", you should see the character keep rotating.

6. The final determine should look like this
<img src="https://raw.githubusercontent.com/yoyotv/Character-detection-and-recognition/master/figures/result.JPG" >

7. As you can see, the answer of the first character is "H", but because of the similarity between rotated "I" and rotated "H", so the classifier went wrong.

## Models

https://drive.google.com/open?id=1BybZGI1q-F8BbTDDZ4Pu6OgASW4e3Fn9

## Labeling

1. Number 0-9 related to label 0-9.

2. Character A,B,...Z related to label 10~35.

2. Character a,b,...z related to label 36~61.

## To do 

We could detect the restricted area by some dataset like

1. [MSRA-TD500](http://www.iapr-tc11.org/mediawiki/index.php?title=MSRA_Text_Detection_500_Database_(MSRA-TD500))

2. [KAIST Scene Text Database](http://www.iapr-tc11.org/mediawiki/index.php?title=KAIST_Scene_Text_Database)

3. [Natural Environment OCR Dataset](http://www.iapr-tc11.org/mediawiki/index.php?title=NEOCR:_Natural_Environment_OCR_Dataset)

Use the position label to obtain the restricted area and feed it into our system, then compare the result with faster RCNN.

By doing so, we could increase the number of our dataset in classification.
