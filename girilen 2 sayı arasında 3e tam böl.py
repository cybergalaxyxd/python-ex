a = int(input(("ilk sayıyı giriniz = ")))
b = int(input(("İkinci sayıyı giriniz = ")))
toplam = 0
if a<b:
    for x in range (a,b+1):
        if x % 3==0:
            print(x)
            toplam =toplam + x
else:
    for x in range (b,a+1):
        if x % 3==0:
            print(x)
            toplam = toplam + x
print ("Toplam = " +str(toplam))






