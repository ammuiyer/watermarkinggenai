from transformers import AutoModelForCausalLM
 
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model.to("cuda")
 
generated_ids = model.generate(tokens, max_new_tokens=1000, do_sample=True)

# decode with mistral tokenizer
result = tokenizer.decode(generated_ids[0].tolist())
print(result)


