from transformers import pipeline

pipe = pipeline(task="text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
outputs = pipe("the secret to baking a really good cake is ")
print(outputs)
