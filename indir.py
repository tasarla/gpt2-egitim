from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "gorkemgoknar/gpt2-small-turkish"
save_dir = r"C:\Users\sinan aydın\Desktop\SİTELER\ai\turkce-gpt2-kripto"

print("Model ve tokenizer indiriliyor...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Model ve tokenizer kaydediliyor...")
tokenizer.save_pretrained(save_dir)
model.save_pretrained(save_dir)

print(f"Model ve tokenizer başarıyla '{save_dir}' klasörüne kaydedildi.")
