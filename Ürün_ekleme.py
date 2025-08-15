urunler = []
adet = int(input("Kaç ürün: "))

i = 0

while i < adet:
    name = input("İsim: ")
    price = input("Fiyat: ")
    urunler.append({
    "name" : name,
    "price": price 
    })
    i += 1 

for urun in urunler:
    print(f"ürün adı: {urun["name"]}, Ürün fiyatı {urun["price"]}")