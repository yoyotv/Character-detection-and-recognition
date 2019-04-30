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


## Models

https://drive.google.com/open?id=18LOMbMRIF2w6etZaqH3X9DfTnhorMWIs

## Anything else?

* Train more models to play.

* Train the model with AM-softmax so that we could evaluate the angle between faces to identify person.
