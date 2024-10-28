from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import torch


from huggingface_hub import login
login(token=os.getenv("USER_ACCESS_TOKEN"))

os.environ['HF_HOME'] = '/data/shared_models/'
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'


model_id = "mistralai/Mixtral-8x22B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id, token=os.getenv("USER_ACCESS_TOKEN"), device_map="auto", 
    torch_dtype=torch.bfloat16, trust_remote_code=True)

text = "Hello my name is"
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
