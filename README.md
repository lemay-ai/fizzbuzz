# LEMAY.AI INTERVIEW QUESTIONS
Hello, human.

Your goal is to demonstrate your coding skills by creating a video recording of your answers to some general knowledge questions, writing an ML API demo using Docker, python3, and a bit of magic, and showing us your exploratory data analysis skills. Please spend minimal effort on graphics and UI, as this is not a test of your UI coding skills. Just don't stress on frontend stuff.

# 1) GENERAL KNOWLEDGE VIDEO DEMONSTRATION AND TECHNICAL WRITING SAMPLE
- Please provide a writing sample. The sample can be from your past work (off-the-shelf), or you can create a new technical writing sample. The writing sample should be on a technical subject, written in English,  and should be at least one page in length.
- Please make a video recording of your answers to the questions in the notebook: https://github.com/lemay-ai/fizzbuzz/blob/main/Interview_Questions.ipynb
- Please send the video file and writing sample to daniel@lemay.ai and matt@lemay.ai
- After you submit the video, proceed to steps 2 and 3, below.

# 2) MODEL DEPLOYMENT DEMONSTRATION
Please fork this repo (you may opt to share a private repo with us to preserve your privacy) and then do the following:
- Create a branch in your forked repo
- Create a container to process inference requests from any pretrained model in the huggingface model hub: https://huggingface.co/models
- Your solution should include server components to support multiple parallel incoming requests (e.g., NGINX/gunicorn)
- Create a notebook to demonstrate requests that POST to the container endpoint and print out the response
- Please explain why you have chosen this model as your demonstration

Solution:
1. Model / container / web server /web server application selection:
    - As the purpose of this task was to demonstrate model deployment so to focus more in it ,I have selected a model that I have worked in my previous projects. Image classsification model from microsoft i.e (ResNet-50 v1.5 https://huggingface.co/microsoft/resnet-50) which is pretrained on ImageNEt-1k dataset and can classify 1000 classes. 
    - Used Starlette and unicorn for developing the ASGI based web application.
    - Used Nginx as the web server that can recieve the request form the internet and forward it to the unicorn acting as a reverse proxy.
    - The application was containerised using docker container.
2. How to execute / demo:
    - Make sure you have git and docker installed in your local system 
    - First clone the repository in you local machine using git
    - Open terminal and change the directory to fizbuzz/task_2 and type the following docker commmand
    ```
    docker-compose up 
    ```
    - Once the docker build is done you can connect to the application on this url " http://localhost:5000" 
    - To connect it through a browser then go to above url. There will be two options i.e to select the image from your local machine and upload option to get the classification result.
    - User can also do post request (containing image file object) at this url  " http://localhost:5000/predict"
        - To test the above post request user can navigate to folder /fizzbuzz/task_2/web_app/api_testing and open jupyter notebook "test.ipynb" and execute the cells.
    


# 3) EXPLORATORY DATA ANALYSIS DEMONSTRATION
- Perform exploratory data analysis on any dataset in the huggingface datasets hub: https://huggingface.co/datasets
- Include a notebook that contains your analysis within the repository
- Please explain why you have chosen this dataset for your demonstration of exploratory data analysis

- Commit your code
- Create a pull request and you can approve it yourself and merge the branch into trunk
- Document the process for using your updated repo in README.md so that we can try out your demo ourselves
- Share the repo with the github users dcshapiro and elmathioso
