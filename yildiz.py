def ucgen_yildiz(satir):
    for i in range(1,satir+1):
        print(i*"*")
ucgen_yildiz(5)


def yildiz_ucgen_ciz():
    yukseklik=5
    for i in range(1,yukseklik):
        print(" "*(yukseklik-i),"*"*(i*2-1))
yildiz_ucgen_ciz()

for i in range(11,0,-2):
    print("{:20}".format(i*"*"))

for i in range(1,10,2):
    for j in range(0,6):
        print("{:^12}".format(i*"*"),end='')
    print()


