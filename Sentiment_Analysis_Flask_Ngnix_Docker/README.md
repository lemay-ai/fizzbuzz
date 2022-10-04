# Sentiment Analysis
    Sentiment analysis is the process of tagging a text according to its sentiment, mostly positive, negative or neutral. 

## Objective

To build an Automated Sentiment Analysis tool to predict the sentiment of the input text along with its confidence score. The tool should allow the users to enter the text in real time through a web API, configured in a way such that it can handle multiple inference requests at the same time. 

## Approach

  1. __Model__:  The model used here for inference is [Bertweet]((https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis?text=I+like+you.+I+love+you)), a [Roberta](https://arxiv.org/abs/1907.11692) model trained on SemEval 2017 corpus containing tweets in english. Thanks to Hugging face community, we can leverage the pipeline functionality for using pre-trained models with minimal code. 
  
  2. __Flask__: We create a minimal web app using flask to render the html files to create an interface for inferencing our model. Users can enter their text and get the result here.

  3. __Nginx and Gunicorn__ : Next we deploy our working model more efficiently using Nginx and Gunicorn. Gunicorn is an application server for our running instance. Meanwhile, Nginx serves as reverse proxy, accepting incoming requests and routing them. In a nutshell it acts as a load balancer to our Web Application.
   
  4. __Docker__ : Our final step is to dockerise the above components so that it works across all environments. Docker provides an isolation environment so that the application can run on anywhere. 

## How get the application up?

1. ```git clone task2-url ```
   
2. ```docker-compose up -d --build scale app = 5```
   This code triggers the docker build. "*--scale app=5*" refers to the number of containers that should be created and run in parallel for accepting mutliple requests from multiple users. We can scale this up according to the need. We can also use other techniques like locust to swarm and monitor how the application responds to multiple user requests.

## Why this model?

   - Bertweet was the first large scale pre-trained model for English tweets trained on a large scale corpus of 850 million english tweet BERTweet produced state-of-the-art performances on 3 downstreamTweetNLPtasks: POS tagging, NER, and text classification (i.e. sentiment analysis & irony detection). It served as a strong foundation for future real world problems like hate speech detection that have been an issue with social media platform like twitter. High accuracy along with the mentioned reasons have motivated me to go ahead with Bertweet for this demonstration. 