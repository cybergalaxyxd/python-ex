print("""
*****************
Vücut Kitle Endeksi Hesaplayıcı


""")

boy = float (input("Boyunuzu giriniz = "))
kilo= float (input("Kilonuzu giriniz = "))

vki = kilo / (boy * boy)

if vki < 18.5:
    print("Zayıf , Vücut kitle endeks = {}".format(vki))
elif 18.5< vki <25:
    print("Normal, Vücut kitle endeks = {}".format(vki))
elif 25 < vki <30:
    print ("Fazla kilolu , Vücut kitle endeks = {}".format(vki))
else:
    print("Obez")






