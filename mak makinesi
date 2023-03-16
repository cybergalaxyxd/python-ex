print("********************\nPARAMAKINOGLAN'A HOŞGELDİNİZ\n********************")

print("""
İşlemler:

1. Para Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye  = 35000

while True:
    işlem = input("NE YAPMAK İSTERSİN MAK:")

    if (işlem == "q"):
        print("YİNE BEKLERİZ MAK....")
        break
    elif (işlem == "1"):
        print("BAKİYEN {} TL MAK".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("YATIR MAK İSTEDİGİN TUTAR MAK:"))

        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("ÇEKMEK İSTEDİĞİN TUTAR MAK:"))
        if (bakiye - miktar < 0 ):
            print("BU KADAR PARAN YOK MAKIN OGLU")
            print("BAKİYEN {} TL MAK".format(bakiye))
            continue
        bakiye -= miktar

    else:
        print("MAKINOGLU 3 TANE ŞEY VAR KÖR OCC.")
