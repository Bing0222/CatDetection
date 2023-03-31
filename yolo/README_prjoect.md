
DELET data file

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
