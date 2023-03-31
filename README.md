# Cat Detection

## 1. Description

- This project shows some mathods which using computer vision detect cats.

- Decrices stregness and weakness in different methods.

- This project generally use pytorch to build different methods.

## 2. FastRCNN

- In this method, Selecting a ResNet50 FastRCNN to detect cat and drawing box in the aimed objection.

- This method does not collection training dataset due to split frontground and background.

- This method does not have good result. Through using IOU result to check box does not get a box including whole object and have some useless information.

- Maybe change vgg16 can get better result.

## 3. CNN

- In this way, Using datasets from kaggle Dog and Cat train self CNN model, get the .path weight and tune better paramters to test test dataset and using single images to detection cat.
  - 1. Modify config
  - 2. Make dataset
  - 3. Train model
  - 4. Test model and tune paramters
  - 5. Check result

- This way has good result (without tune paramters effect) than a way that using pre-train model detect object.

- The way only output a class name without box and object position information. This way generally be impacted on different models. Finally, it generally cost huge tiem for get better effect.

- tune paramters to get better result.

## 4. YOLO

~~~shell
cd yolov5
pip install -r requirements.txt

pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
~~~

~~~shell
├── data
│   ├── Annotations   Doing detection The tag file at the time of the task,  .xml, with the file name corresponding to the image name
│   ├── images  Save .jpg files
│   ├── ImageSets  Stored is the dataset split file for classification and detection，including train.txt, val.txt,trainval.txt,test.txt
│   ├── labels  Stored label infomation.txt，Correspond with the picture one by one


├── ImageSets(train，val，test--8:1:1)
│   ├── train.txt  the pictures used for training
│   ├── val.txt  the pictures used for validation
│   ├── trainval.txt  train and val
│   ├── test.txt  the pictures used for testing

~~~



## 5. Effective Net
