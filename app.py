from transformers import pipeline
classifier = pipeline('sentiment-analysis')

print("Lets check your tweets \n")
state = str(input("Enter any tweet: \t"))

while state:
    print(state, "\t",classifier(state), "\n")
    print("Enter another tweet or leave blank to exit\n\n")
    state = str(input("Enter any tweet: \t"))

print("exiting the program")