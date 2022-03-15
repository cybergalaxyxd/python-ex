toplam = 0
for x in range (1,5+1):
    sayi =int(input("sayı ="))
    toplam = toplam+sayi
    if x == 1:
        mak =sayi
    else:
        if mak<sayi:
            mak=sayi
print ("Maksimum = " + str (mak))
print ("Ortalama = "+ str (float(toplam) /5))




