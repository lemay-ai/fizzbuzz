# LEMAY.AI INTERVIEW QUESTIONS

Hello, human.

Your goal is to demonstrate your ninja coding skills by writing an ML API demo using Docker, python3, and a bit of magic. Please spend minimal effort on graphics and UI, as this is not a test of your UI coding skills. Just don't stress on frontend stuff. 

# GENERAL KNOWLEDGE

- Please make a video recording of your answers to the questions in the notebook: https://github.com/lemay-ai/fizzbuzz/blob/main/Interview_Questions.ipynb
- Please share the video file with daniel@lemay.ai and matt@lemay.ai

# MODEL DEPLOYMENT
Please fork this repo (you may opt to share a private repo with us to preserve your privacy) and then do the following:
- Create a branch in your forked repo
- Create a container to process inference requests from any pretrained model in the huggingface model hub: https://huggingface.co/models
- Your solution should include server components to support multiple parallel incoming requests (e.g., NGINX/gunicorn)
- Create a notebook to demonstrate requests that POST to the container endpoint and print out the response
- Please explain why you have chosen this model as your demonstration

# EXPLORATORY DATA ANALYSIS
- Perform exploratory data analysis on any dataset in the huggingface datasets hub: https://huggingface.co/datasets
- Include a notebook that contains your analysis within the repository
- Please explain why you have chosen this dataset for your demonstration of exploratory data analysis

- Commit your code
- Create a pull request and you can approve it yourself and merge the branch into trunk
- Document the process for using your updated repo in README.md so that we can try out your demo ourselves
- Share the repo with the github users dcshapiro and elmathioso
