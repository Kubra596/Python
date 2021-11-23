boy=float(input("Boyunuzu yazınız: "))
kilo=float(input("Kilonuzu yazınız: "))
vki=kilo/(boy*boy)

if vki<18.5:
    print("Zayıfsınız")

elif vki>18.5 and vki<25:
    print("Normalsiniz")

elif vki>25 and vki<30:
    print("Fazla kilolusunuz")

else:
    print("Obezsiniz")
