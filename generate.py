import transformers
import torch
import os
from huggingface_hub import login

os.environ['HF_HOME'] = '/work/pi_adamoneill_umass_edu/watermarkinggenai/.cache'

# login(token = os.getenv("USER_ACCESS_TOKEN"))


model_id = "meta-llama/Meta-Llama-3-70B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    token=os.getenv("USER_ACCESS_TOKEN"), trust_remote_code=True)



terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]


print(outputs[0]["generated_text"][-1])


def generate_plain(prompt):
    messages = [
    {"role": "user", "content": prompt}]

    outputs = pipeline(
    messages,
    max_new_tokens=20,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
    pad_token_id=pipeline.tokenizer.eos_token_id)



