from random import randint

rand=randint(1,100)
sayac=0

while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında bir değer girin: " "0'a basarsanız çıkış yaparsınız!!"))

    if (sayi==0):
        print("Oyun Bitti!")
        break
    elif sayi<rand:
        print("Daha yüksek bir sayı girin.")
        continue
    elif sayi>rand:
        print("Daha küçük bir sayı girin.")
        continue
    else:
        print("Rastgele seçilen sayı {0}".format(rand))
        print("Tahmin sayınız {0}".format(sayac))