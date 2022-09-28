# LEMAY.AI INTERVIEW QUESTIONS
Hello, human.

Please follow the instructions for each task.

# MODEL DEPLOYMENT DEMONSTRATION
- We used ResNet-50 v1.5 https://huggingface.co/microsoft/resnet-50 pretrained model to get the inference.
- ResNet model pre-trained on ImageNet-1k at resolution 224x224. It was introduced in the paper Deep Residual Learning for Image Recognition by He et al.
- This is a image classification model using resnet-50 backbone.
- The output of this application is the form of string displaying the class/es of detected objects in the image.
- Model is used to classify an image of the COCO 2017 dataset into one of the 1,000 ImageNet classes.

Execution:

- Direct to folder /MDD and open jupyter notebook "image_classification.ipynb".
- Make sure your Linux-64 supports docker, docker-compose, and curl command.
- Check the terminal path from your application(e.g., jupyter notebook, vscode) to make sure your
  working directory is /MDD
- Execute all the cells in "image_classification.ipynb" file one by one. This notebook will create
  docker and containers for nginx and python application and using a CURL request process your image
  and return the name of detected classes.
- I have chosen an image classifier since it is relevant to my current role. Among image classifier,
  ResNet (Residual Network) is a convolutional neural network that democratized the concepts of residual learning and skip connections. This enables to train much deeper models. Also, it is trained on a million images of 1000 categories from the ImageNet database. Supporting 1000 classes increase the chance of getting a closer class detection to the real category of object.

# 3) EXPLORATORY DATA ANALYSIS DEMONSTRATION
- To perform EDA, I have chosen CPPE - 5 (Medical Personal Protective Equipment) dataset (https://huggingface.co/datasets/cppe-5).
- To execute this EDA, please direct into folder /EDA and open/run the "EDA_shahriar_taheri.ipynb" file.
  Each cell contains the info/explanation of the code cell.
- This is an object detection dataset in which 5 different classes are supported (Coverall (0),Face_Shield (1),Gloves (2),Goggles (3) and Mask (4)).
- Since pandemic, datasets regarding medical personal protective equipments become popular.
  Moreover, this dataset uses real world images in which having deeper information on that could bring some real impacts.
