import requests
from bs4 import BeautifulSoup

def veri_cek_ve_kaydet(url, dosya_adi):
    print("🔍 Veri çekiliyor...")
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    sozluk_items = soup.find_all("dl", class_="hg-item")
    if not sozluk_items:
        print("❌ Sözlük verileri bulunamadı.")
        return False

    with open(dosya_adi, "w", encoding="utf-8") as f:
        for item in sozluk_items:
            baslik = item.find("dt", class_="hg-item-title")
            aciklama = item.find("dd", class_="hg-item-description")
            if baslik and aciklama:
                soru = f"{baslik.text.strip()} nedir?"
                cevap = aciklama.text.strip()
                f.write(f"{soru}\n{cevap}\n\n")

    print(f"✅ Veri '{dosya_adi}' dosyasına başarıyla kaydedildi.")
    return True

def main():
    url = "https://www.coinkolik.com/kripto-sozluk/"
    veri_dosyasi = "sozluk_metin.txt"
    veri_cek_ve_kaydet(url, veri_dosyasi)

if __name__ == "__main__":
    main()
