from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_path = "./gpt2-sozluk-egitim"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

soru = "Airdrop nedir?\n"
input_ids = tokenizer.encode(soru, return_tensors="pt")

output = model.generate(
    input_ids,
    max_length=150,
    num_return_sequences=1,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.8,
    pad_token_id=tokenizer.eos_token_id
)

cevap = tokenizer.decode(output[0], skip_special_tokens=True)
print(cevap)
