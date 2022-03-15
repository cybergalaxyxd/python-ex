import random
random
lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = ".;/*-+"
all = lower + upper +number + symbol
lenght = 10
password = "".join(random.sample(all,lenght))
print ("The password you genetared = " , password)
