from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling
import os

def dataset_olustur(dosya, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=dosya,
        block_size=block_size,
        overwrite_cache=True
    )

def main():
    dosya_adi = "sozluk_metin.txt"
    model_path = "turkce-gpt2-kripto"  # eğitilecek temel model
    kayit_yolu = "./gpt2-sozluk-egitim"  # eğitilmiş model buraya kaydedilir

    print("🔧 Tokenizer ve model yükleniyor...")
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)

    print("📚 Dataset hazırlanıyor...")
    dataset = dataset_olustur(dosya_adi, tokenizer)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir=kayit_yolu,
        overwrite_output_dir=True,
        num_train_epochs=5,
        per_device_train_batch_size=2,
        save_total_limit=1,
        logging_steps=10,
        report_to=[],
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=data_collator,
    )

    print("🎓 Eğitim başlıyor...")
    trainer.train()

    print("💾 Model kaydediliyor...")
    trainer.save_model(kayit_yolu)
    tokenizer.save_pretrained(kayit_yolu)
    print("✅ Eğitim tamamlandı!")

if __name__ == "__main__":
    main()
