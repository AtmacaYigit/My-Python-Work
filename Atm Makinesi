print("--------------------------------------\nATM'YE HOŞ GELDİNİZ\n--------------------------------------")
#Hesap Bilgileri
musteri = {"Kaan": {"sifre": "314159", "bakiye": 1000, "guvenlik": "Londra"},
         "Yiğit": {"sifre": "161803", "bakiye": 500, "guvenlik": "Paris"},
         "Vahdet": {"sifre": "123456", "bakiye": 2000, "guvenlik": "New York"}}
log = []

#ATM İsim Soyisim ve Şifre İsteme
def giris():
    isim = input("İsminizi girin: ")
    sifre = input("Şifrenizi girin: ")
    return isim, sifre

def cekim(isim, tutar):
    if tutar > musteri[isim]["bakiye"]:
        print("Yetersiz bakiye.")
    else:
        musteri[isim]["bakiye"] -= tutar
        print(f"{isim}, hesabınızdan {tutar} TL çektiniz. Yeni bakiyeniz {musteri[isim]['bakiye']} TL.")
        log.append(isim + " " + str(tutar) +"TL çekti.")

def yatirma(isim, tutar):
    musteri[isim]["bakiye"] += tutar
    print(f"{isim}, hesabınıza {tutar} TL yatırdınız. Yeni bakiyeniz {musteri[isim]['bakiye']} TL.")
    log.append(isim + " " + str(tutar) + "TL yatırdı.")

def kayit(isim):
    for i in log:
      if isim in i:
        print(i)

def sifre_degistirme(isim, yeni_sifre):
    musteri[isim]["sifre"] = yeni_sifre
    print(f"{isim}, şifreniz başarıyla değiştirildi.")

def toplam_para(musteri):
    toplam_bakiye = sum([musteri[isim]["bakiye"] for isim in musteri])
    print("Bankanın toplam bakiyesi:", toplam_bakiye)

while True:
    isim, sifre = giris()
    if isim in musteri and musteri[isim]["sifre"] == sifre:
        print(f"Hoşgeldiniz, {isim}! Bakiyeniz {musteri[isim]['bakiye']} TL.")
        while True:
            islem = int(input("""
Yapmak istediğiniz işlemi giriniz:
1. Para Çekme
2. Para Yatırma
3. Yapılan İşlemler
4. Şifre Değiştirme
5. Bankanın Toplam Parası
6. Çıkış Yapma
    """))
            if islem == 1:
                tutar = int(input("Çekmek istediğiniz miktarı girin: "))
                cekim(isim, tutar)
            elif islem == 2:
                tutar = int(input("Yatırmak istediğiniz miktarı girin: "))
                yatirma(isim, tutar)
            elif islem == 3:
                print("Yaptığınız işlemler: ")
                kayit(isim)
            elif islem == 4:
                yeni_sifre = input("Yeni şifrenizi girin: ")
                sifre_degistirme(isim, yeni_sifre)
            elif islem == 5:
              toplam_para(musteri)
            elif islem == 6:
                print("Çıkış yapıldı.")
                break
            else:
                print("Geçersiz işlem.")
    else:
        print("Girmiş olduğunuz isim veya şifre yanlış.")
        sifre_degistir = input("Şifrenizi değiştirmek ister misiniz? Evet ise 'e', hayır ise 'h' yazınız: ")
        if sifre_degistir == "h":
            continue
        elif sifre_degistir == "e":
            guvenlik = input("Güvenlik kelimenizi giriniz: ")
            if guvenlik == musteri[isim]["guvenlik"]:
                yeni_sifre = input("Yeni şifrenizi girin: ")
                sifre_degistirme(isim, yeni_sifre)
            else:
                print("Güvenlik kelimesi yanlış. Şifre değiştirme işlemi başarısız.")
