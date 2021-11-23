vize=input("Vize notunuzu yazınız: ")
final=input("Final notunuzu yazınız: ")
basari_notu=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama: {0}".format(basari_notu))

if (basari_notu<50):
    print("Kaldınız ")
else:
    print("Geçtiniz")