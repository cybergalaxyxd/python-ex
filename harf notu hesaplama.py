print("""
**************
Harf notu hesaplayıcı
**************

""")


vize1 = int (input("1.vize notunuz = "))
vize2 = int (input("2.vize notunuz = "))
final = int (input("final notunuz = "))

notum = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

if   notum >=90:
    print("AA Notunuz {}".format(notum))
elif notum >=85:
    print("BA Notunuz {}".format(notum))
elif notum >=80:
    print("BB Notunuz {}".format(notum))
elif notum >=75:
    print("CB Notunuz {}".format(notum))
elif notum >=70:
    print("CC Notunuz {}".format(notum))
elif notum >=65:
    print("DC Notunuz {}".format(notum))
elif notum >=60:
    print("DD Notunuz {}".format(notum))
elif notum >=55:
    print("FD Notunuz {}".format(notum))
else:
    print("DD Notunuz {}".format(notum))

