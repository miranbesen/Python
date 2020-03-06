
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        t=1
        for i in range(b):
             t=t*a
             
        return t



taban=int(input("sayi tabanini giriniz:"))
us=int(input("üssü giriniz:"))

print(power(taban,us))
