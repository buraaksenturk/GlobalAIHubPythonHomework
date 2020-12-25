# Kütüphane ve modüllerin dahi edilmesi
import time
import random

# Oyuncunun adı alınıyor
ad = input("Adınız : ")

print(f'''
-----> Adam Asmaca Oyunu <-----
Hoşgeldin {ad}, bugün seninle adam asmaca oynayacağız.
Oyunumuzun amacı sana verilecek listeden programın tuttuğu kelimeyi tahmin etmekdir.
Bu oyunda 5 hakkın bulunmaktadır. Her yanlış harfte bir hak kaybediceksin.
Hadi oyunumuza geçelim!!
''')
time.sleep(0.5)

while True:
    kelimeler = ["python", "c", "java", "c++", "c#", "r", "javascript", "php", "go", "swift", "arduino", "ruby",
                 "assembly", "scala", "matlab", "kotlin", "flutter", "opencv", "selenium", "kivy", "mongodb", "hadoop", "mysql"]
    print(f"""
Kelimelerimiz şunlardır:
{kelimeler}
""")
    # Rastgele bir kelime alma
    randomKelime = random.choice(kelimeler)
    # Kullanıcının tahmin hakkı
    tahminHakki = 5
    # Girilen harflerin tekrar etmemesi için oluşturulan liste
    girilenHarfler = []
    # Seçilen kelimenin harf sayısı
    harfSayısı = len(randomKelime)
    cizgi = list("_" * harfSayısı)
    print('Tahmin edeceğin kelime -> ', ' '.join(cizgi), end='\n')
    # Tahmin döngüsü
    while tahminHakki > 0:
        # Tahmin edilen harfi alma 
        # Lover modülü ile büyük harf dahi girilse küçültüyoruz
        veri = input("Tahmin ettiğiniz harfi giriniz : ").lower()
        # 1 saniye bekletme
        time.sleep(1)
        # Girilen harf daha önceden de girildi mi diye kontrol ediliyor
        if veri in girilenHarfler:
            print("Kontrol ediliyor lütfen bekleyiniz..")
            time.sleep(1)
            print("Bu harfi daha önceden hatırlıyorum. Lütfen başka bir harf tahmin ediniz.")
            continue
        # Girilen harf birden fazla mı diye kontrol ediliyor
        elif len(veri) > 1:
            print("Kontrol ediliyor lütfen bekleyiniz..")
            time.sleep(1)
            print("Lütfen sadece bir harf girin.")
            continue
        # Girilen harf bizim seçilen kelimemizde var mı yok mu kontrol ediliyor
        elif veri not in randomKelime:
            tahminHakki -= 1
            print("Kontrol ediliyor lütfen bekleyiniz..")
            time.sleep(1)
            print(f"""
Tüh bee! Yanlış tahmin yaptın {ad}.
Daha dikkatli olmalısın çünkü {tahminHakki} hakkın kaldı.
            """)
            time.sleep(1)
        # Girilen harf doğru mu diye kontrol eiliyor
        else:
            for i in range(len(randomKelime)):
                if veri == randomKelime[i]:
                    print(f"{ad} mükemmel bir iş çıkardın doğru tahmin.")
                    cizgi[i] = veri
                    girilenHarfler.append(veri)
            print(" ".join(cizgi), end='\n')

            time.sleep(1)
            kelimeninTamami = input("Kelimeyi tahmin etmek istiyor musunuz?(e/h) : ").lower()
            
            # Kelimenin tamamını tahmin etmek isteyip istemediği sorgulanıyor
            if kelimeninTamami == "e":
                kelimeninTahmini = input("Tahmin ettiğiniz kelimeyi yazınız : ").lower()
                time.sleep(1)
                print("Kontrol ediliyor lütfen bekleyiniz..")
                time.sleep(1)
                # Tam tahmini doğru mu diye kontrol ediliyor
                if kelimeninTahmini == randomKelime:
                    print(f"{ad} seni tebrik ediyorum. Bildin hadi bunu kutlayalım.")
                    break
                else:
                    tahminHakki -= 1
                    print(f"{ad} maalesef yanlış tahmin yaptın. {tahminHakki} tahmin hakkın kaldı.")
        
        # Hakkı bitti mi diye kontrol ediliyor
        if tahminHakki == 0:
            time.sleep(1)
            print(f"{ad} tahmin hakkın kalmadı. Kaybettin ve adam asıldı :( Başka bir zaman tekrar görüşmek üzere.")

    # Tekrar oynamak isteyip istemediği kontrol ediliyor
    if not "e" == input(f"{ad} tekrar Oynamak İstermisiniz? (e/h): "):
        print(f"{ad} bizimle beraber oyun oynadığın için teşekkür ederiz. Çıkış yapılıyor...")
        time.sleep(1)
        break
