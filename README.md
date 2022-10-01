# TASK 1 (module_2)
## FEATURES
 - A GPT model that generates the text based on the topic and number of words input

## 🛠 Tech Stack

**Server:** Python, FastAPI, Uvicorn



## API AND MODEL DEPLOYMENT DEMONSTRATION
 - Clone the repository to your local machine
 - Open the terminal in module_2/server_docker/ directory 
 - Now we need to package the application using the following command: 
```sh
 docker build -t test-lemay .
```

- Finally, we need to start the container using following command: 
```sh
docker run --name test-lemay -p 80:80 test-lemay
```

> Note: Due to the fact that we have only one image to manage, we do not need to create a docker compose file

## API Reference
#### Complete documentation
```http
  GET /docs
```

#### Retrive text based on a topic

```http
  POST /compare
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `topic` | `string` | **Required**. |
| `max_length` | `int` | **Required**. |

 ## Please explain why you have chosen this model as your demonstration?
 It's been a long time since I've been interested in learning more about openAI pre-trained models. Now I have the opportunity to use one of their models. My goal is to extend the API capabilities in order to create a better user interface and fine-tune the model based on my requirements. As part of my teaching, I plan to demonstrate how easy it is to use the pre-trained models to my students. Thanks to Lemay for providing me with the opportunity to read about GPT model


# TASK 2 (module_3)
## STEPS TO START NOTEBOOK
 - Clone the repository to your local machine
 - Open the directory module_3 and create a virtual env using following command
 ```sh
 python3 -m venv /path_to_venv
```
 - Activate the venv environment (for Mac and Linux) as follows:
 ```sh
 source /path_to_venv/bin/activate
```

 - Activate the venv environment (for Windows) as follows:
 ```sh
  \path_to_venv\Scripts\activate.bat
```

 - Using the following commands, install the dependencies:
  ```sh
  pip install -r requirements.txt
```

 - As a final step, launch the notebook or lab as follows:
```sh
  jupyter lab
```
or 

```sh
  jupyter notebook
```

## Please explain why you have chosen this dataset for your demonstration of exploratory data analysis?
For the EDA, I have selected the IMDB review data set. Despite the small size of the dataset, it gives important insights into the data. This evaluation was conducted as a case study of how COVID-19 affects the movie watching experience and ratings. Even though the data were a sample from a larger dataset, they provided some interesting and real insights. Additionally, I explored other datasets and found that most of them dealt with image classification and text analysis. While image classification is an active research area, it does not provide motivation for EDA. Text analysis is similarly straightforward, using techniques such as lemmatization, stemming, tokenization, sentiment analysis, etc. It is my main goal for this assignment to demonstrate my ability to make inferences from the data. 