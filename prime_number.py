sayi = int(input("Sayıyı girin: "))

if sayi == 1:
    print("1 asal değildir")
elif sayi  %2 == 0:
    print("Sayı asal değil")
elif sayi  %3 == 0:
    print("Sayı asal değil")
elif sayi  %5 == 0:
    print("Sayı asal değil")
elif sayi  %7 == 0:
    print("Sayı asal değil")
else:
    print("Sayı asal")