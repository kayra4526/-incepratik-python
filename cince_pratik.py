# ==============================================================================
# 🚀 BU KODU ÇALIŞTIRMAK İÇİN TERMİNALDE ŞU KOMUTU YAZIN: python3 cince_pratik.py
# ==============================================================================

import random

# A1 (HSK 1) Seviyesi Temel Hece Havuzu
hece_havuzu = {
    # Kişi Zamirleri ve İnsan
    "我": ["wo", "ben"],
    "你": ["ni", "sen"],
    "他": ["ta", "o (erkek)"],
    "她": ["ta", "o (kadın)"],
    "人": ["ren", "insan / kişi"],
    
    # Kendini Tanıtma ve İsim
    "叫": ["jiao", "adlandırılmak / çağrılmak"],
    "名": ["ming", "isim / ad"],
    "字": ["zi", "karakter / yazı"],
    "是": ["shi", "olmak (am/is/are)"],
    
    # Temel Fiiller
    "有": ["you", "sahip olmak / var"],
    "去": ["qu", "gitmek"],
    "来": ["lai", "gelmek"],
    "看": ["kan", "bakmak / görmek / okumak"],
    "吃": ["chi", "yemek yemek"],
    "喝": ["he", "içmek"],
    "学": ["xue", "öğrenmek"],
    
    # Temel Sıfatlar ve Durumlar
    "好": ["hao", "iyi / güzel"],
    "大": ["da", "büyük"],
    "小": ["xiao", "küçük"],
    "多": ["duo", "çok / fazla"],
    "少": ["shao", "az"],
    
    # Zaman ve Sayılar
    "一": ["yi", "bir"],
    "二": ["er", "iki"],
    "三": ["san", "üç"],
    "天": ["tian", "gün / gökyüzü"],
    "月": ["yue", "ay"],
    "日": ["ri", "gün / güneş"],
    
    # Soru ve Olumsuzluk
    "不": ["bu", "değil / hayır (olumsuzluk eki)"],
    "吗": ["ma", "mı/mi (soru eki)"],
    "什": ["shen", "ne (shenme kelimesinin ilk hecesi)"]
}

def hece_pratik_uygulamasi():
    print("="*50)
    print("🇨🇳 ÇİNCE A1 SEVİYESİ HECE PRATİĞİNE HOŞ GELDİN 🇨🇳")
    print("="*50)
    print("Çıkmak ve çalışma özetini görmek için 'q' tuşuna basabilirsin.\n")

    dogru_sayisi = 0
    soru_sayisi = 0
    yanlis_heceler = []

    # Sözlükteki heceleri (Hanzi) bir listeye alıp rastgele karıştırıyoruz
    heceler = list(hece_havuzu.keys())
    random.shuffle(heceler)

    for hanzi in heceler:
        # Seçilen hanzi karakterinin pinyin ve türkçe karşılığını çekiyoruz
        pinyin, turkce = hece_havuzu[hanzi]
        
        print(f"\n👉 Karakter: {hanzi} (Anlamı: {turkce})")
        cevap = input("Pinyin okunuşunu girin: ").strip().lower()

        # Kullanıcı 'q' yazarsa testi bitir
        if cevap == 'q':
            break

        soru_sayisi += 1

        # Cevaptaki ve doğru yanıttaki boşlukları silerek karşılaştırma yapıyoruz
        if cevap.replace(" ", "") == pinyin.replace(" ", ""):
            print("✅ Doğru!")
            dogru_sayisi += 1
        else:
            print(f"❌ Yanlış! Doğrusu: '{pinyin}' olmalıydı.")
            # Bilemediği kelimeyi dosyaya yazmak için sepete ekliyoruz
            yanlis_heceler.append(f"{hanzi} - {pinyin} ({turkce})")

    # --- TEST BİTİMİ VE RAPORLAMA EKRANI ---
    print("\n" + "="*50)
    print("📊 ÇALIŞMA ÖZETİ")
    print(f"Toplam Sorulan: {soru_sayisi}")
    
    if soru_sayisi > 0:
        basari_orani = (dogru_sayisi / soru_sayisi) * 100
        print(f"Doğru Cevap: {dogru_sayisi} (Başarı Oranı: %{basari_orani:.1f})")
        
        if yanlis_heceler:
            print("\n📝 Tekrar edilmesi gereken heceler 'tekrar_edilecekler.txt' dosyasına kaydediliyor...")
            
            # Yanlışları txt dosyasına ekliyoruz ('a' modu ile)
            with open("tekrar_edilecekler.txt", "a", encoding="utf-8") as dosya:
                dosya.write("\n--- Yeni Çalışma Oturumu ---\n")
                for hece in yanlis_heceler:
                    dosya.write(hece + "\n")
                    
            print("Dosya başarıyla güncellendi! Kapatmadan önce txt dosyanı inceleyebilirsin.")
        else:
            print("\n🎉 MÜKEMMEL! Karşına çıkan tüm heceleri doğru bildin.")
    else:
        print("Hiç soru cevaplamadan çıktın. Bir dahaki sefere görüşmek üzere!")

# Programın başlangıç noktası
if __name__ == "__main__":
    hece_pratik_uygulamasi()