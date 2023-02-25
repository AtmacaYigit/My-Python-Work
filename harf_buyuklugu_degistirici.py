soru_stringi = "KJklnnklNKLjkNKLnjHJGklNKLbgjkUIOKikLjşllnKnmlK9034853+/*/-"
sonuc = ""

for harf in soru_stringi:
    if harf.isalpha():
        if harf.islower():
            sonuc += harf.upper()
        else:
            sonuc += harf.lower()

print(sonuc)
