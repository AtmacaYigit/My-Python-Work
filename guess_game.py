import random

sayi = random.randint(1,10)
hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahminin: "))
    if tahmin == sayi:
        print(f"Tebrikler, {sayac}. tahminde doğru bildin. Puanınız: {sayac * 20}")
        break
    elif tahmin > sayi:
        print("Daha düşük bir sayı tahmininde bulun.")
    elif tahmin < sayi:
        print("Daha yüksek bir sayı tahmininde bulun.")
    else:
        print("Lütfen sadece 1 ile 100 arasında bir tahminde bulun")
    
    if hak == 0:
        print(f"Kaybettin. Tutulan sayi: {sayi}")




