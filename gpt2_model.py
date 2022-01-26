from transformers import pipeline
#print("hello")
text_generate = pipeline("text-generation")
input_txt = str(input(" Enter your text to develop some context:"))
generated_txt = text_generate(input_txt, max_length = 500, do_sample=False)[0]
print(generated_txt['generated_text'])
print(type(generated_txt['generated_text']))


