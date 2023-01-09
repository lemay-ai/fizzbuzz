# This is an application for Automatic Speech Recognition

## To run this application,
[Assumption is that you are running this on a linux machine]
[Docker is running]


1) Clone this repository

2) Run : 
``docker-compose up --build -d --scale app=2
``
3) Goto : ``localhost:9000``

![sample1](https://github.com/projects-g/fizzbuzz/blob/dev/sample1.png)

![sample2](https://github.com/projects-g/fizzbuzz/blob/dev/sample2.png)

You should be able to see the application on this port

[If you are running on a non-linux machine, you may face issues while running nginx.
This is because we are changing the configuration from a default nginx server to redirect
the calls to our application, running on a pre-determined port]

In this case, if you want to directly access the application, after you run the docker-compose build
command from above,

1) Get the image id of the flask application (fizzbuzz_app) by
``docker images``
2) Run
`` docker run -p 5000:5000 <image_id>``

You should see a SWAGGER UI to interact with the application like below :

![swagger](https://github.com/projects-g/fizzbuzz/blob/dev/swagger.png)


You dont need an UI layer here as SWAGGER UI is intuitive and easy to work with.


Click on "Try it out".

Give the filename as ``84-121550-0000.flac``. 

This is a sample file I have uploaded to do inference against. 
Ideally, you give a filename and we fetch it from cloud storage. Keeping an upload option is easy too, but 
cloud storage enables to get a folder name and perform inference on all files simultaneously too. 
Hence I have kept it this way.

You should be able to extract the text from the speech in the audio file.

NOTE: There is no separate notebook to run the inference and SWAGGER UI takes it place.


![sample3](https://github.com/projects-g/fizzbuzz/blob/dev/image3.png)

That's it !

# Reason for choosing ASR

Automatic Speech Recognition is one of my recent interests and I have been trying 
some experimentations of my own in this domain. Hence, I wanted to engineer a bit around it too.
We can add RabbitMQ as a dependent service and put/process files from/to queue to
parallelize further. I am comfortable designing an in-house message queue for this application, as well as
across the organization too, using underlying concurrent datastructures, lock-free, lock-based both.

I also noticed that Lemay.ai has highlighted a ASR (Voice Recognition) project in their portfolio
brochure. Theres that as well. 

# The EDA task's notebook is in the notebooks folder.

