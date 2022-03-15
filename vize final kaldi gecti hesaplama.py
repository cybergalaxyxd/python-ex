vize = int(input("Vize notunu giriniz = "))
odev = int(input("Ödev notunu giriniz = "))
final = int(input("Final notunu giriniz = "))
ortalama = vize*0.2 + odev*0.3 + final*0.5
print("Ortalama = "+str(ortalama))
if ortalama >50:
    print("Gecti")
else:
    print ("Kaldı")




