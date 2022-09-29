# Task 2- MODEL DEPLOYMENT DEMONSTRATION
Steps for the Demo
- Clone the repository to your local machine
- Start Docker Desktop or Docker service in your local system
- In the terminal/powershell navigate to the folder /fizzbuzz/Assignment
- Run the command  
```
docker-compose up -d --build --scale ml-app=3
```
 (3 Replicas will be created for load balancing using NGINX)
- Run the command "docker ps" to check if the containers are running
- Connect to "http://localhost:5000" via browser or postman or curl to check if API is running fine. "Machine Learning Inference" response will be received if the API is running.
- Navigate to the folder /fizzbuzz/Assignment/test
- Run the cells of test.ipynb file to send a POST request to the API and receive a prediction

# Please explain why you have chosen this model as your demonstration?
I have chosen this model for demonstration because I am interested in exploring computer vision and Image based machine learning models. I have worked on Image Classification models-RESNET and VGG16 during my academic projects for a computer vision problem. Having worked on data preparation, data cleaning, preprocessing,Model training and tuning , now I wanted to explore how I can create an python API for a trained model that can interact with a real user. I wanted to understand how can we send an Image as a POST request from the frontend/browser and how it will be framed as a message. In the backend as well, I wanted to understand how will we receive the image and  what operations we need to perform in order to process it for the model prediction. In short I wanted to understand how we take a trained Machine Learning model and turn it into a real time application.
