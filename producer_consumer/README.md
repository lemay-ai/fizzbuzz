Hello HumanV2,

Here are the instructions to starting the application. The app is based on the Flask webframwork which is dockerized for your convience.
First, you can start the consumer API using:

docker-compose build

docker-compose up

This will start the the Flask app, redis, rq worker and MySQl database where the information from incoming requests is stored.
Next, you can start the producer.ipyndb script that is located wihtin producer_consumer folder. This script sends the request to the consumer app. To start the script you can open jupyter notebook or whatever you desire that handles .ipyndb files. If you don't have jupyter notebook you can run the command:

pip install jupyter

and 

jupyter notebook

To open the notebook. I have decided to not dockerize the jupyter notebook because I asssumed that you wanted to see the response within jupyter, or at least that was mine interpretation of the instructions. Once the notebook is open you can press "Run" and 10 requests at the start of each second will be send to the consumer API. You should get a response from the consumer in the notebook that looks like this:

The request was completed, job id: 65d83d82-dedd-42f3-a130-d8838010bdb4

Leave it running and open up http://0.0.0.0:5000/ in your browser. Here you should see the max_msg number that is currently processed and the average time of all the calls for the past 10 seconds from the current moment. Note: If you open this url before sending requests from the producer script, you will get status code 500 from the flask application. Not to fear, this is just ajax request checking for the latest data within the MySQL database. Additionally, if you stop the requests, you will also get the 500 status code from the /calcaulate_result route. This is because the ajax request cannot find any data with time for the past 10 seconds from the current moment. 

