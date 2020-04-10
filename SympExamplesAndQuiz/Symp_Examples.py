from sympy import Symbol 
x=1
print("normal kullanım:")
print(x+x+1) #bu şekil yazarsak normal cıktı gibi 3 degerini verir.

#-------------------------------------------------------- Symbol kısmı------------------------------------------------------------------------------
print()
print(50*"-")
x=Symbol('x') #Burda x'i sembol olarak kullanmamızı saglar.
print("sembolik kullanimi:")
print(x+x+1) #burda sembol uzerinden işlem yapıyor.

a=Symbol('x') #a'yı sembol x gibi gostertiyoruz.İlla aynı olmak zorunda değil yani Symbol içindeki degerle 
print("a degiskenli hali:")
print(a+a+1) #x+x+1 degeri basar

#-----------------------------------------------------İki bilinmeyenli denklem islemleri--------------------------------------------------------------------------------------------------------
print()
print(50*"-")
print("iki bilinmeyenli denklem kismi:")
x=Symbol('x')
y=Symbol('y')

symbol1=x*y+x*y 
print(symbol1)

print("sadece x'li islem hali:")
symbol2=x*(x+x) #cevap 2x'in karesidir ** kare anlamında
print(symbol2)


symbol3=(x+2)*(x+3)
print(symbol3)

#---------------------------------------------------------------factor ve expand----------------------------------------------------------------------
print()
print(50*"-")
print("factor ve expand kismi")
from sympy import factor,expand 
#factor: genisletilmis bir ifadeyi tekrar birlestirmeye yarayan bir ifadedir.Veya carpanlarına ayırma gibi islevleride vardır. 
#expand: denklemi genişletmeye yarayan bir ifadedir.
expr1=x**2-y**2
factors1=factor(expr1)
print("Normal denklem:",expr1)
print("Carpanlarina ayrilmis hali(factor kullanilmis hali):",factors1)
print()

print("kup acilimi ornegi :")
expr2=x**3+3*x**2*y+3*x*y**2+y**3
print("normal hali:",expr2)
factors2=factor(expr2)
print("genislemis olan denklemin birlesmis hali (factor kullandık):",factors2)

print()

expr3=(x-y)**2
print("denklemin normal hali:",expr3)
print("denklemin genisletilmis hali:",expand(expr3))

#----------------------------------------------------------------pprint--------------------------------------------------------------------------------
print()
print(50*"-")
print("pprint kismindayiz")
print()
from sympy import pprint 
#pprint: Yazicagimiz ifadeyi daha güzel haliyle yazmaya ve normal haline daha çok benzeyen şekilde göstermeye yarar.
print("denklemin normal hali:",expr3)
print("pprint kullanilmis hali:")
pprint(expr3)
print()
print("seri seklinde pprint örnegi:")
series=x
x_value=5
n=5
for i in range(2,n+1):
    series=series+(x**i)/i

pprint(series)
print()
print("serinin deger verilmis hali:")
series_value=series.subs({x:x_value}) 
# .subs fonksiyonu bir ifadeye deger verirken kullanılır.
#.subs diyip({ şeklinde degisken yerine degerler ekleyebiliyoruz.})

print(series_value)
print()



#---------------------------------------------------------------------------.subs Kısmı----------------------------------------------------------------------------------
print()
print(50*"-")
print(".subs kismi")
print("x,y degiskenli ornek:")

print()
expr4=x*x+x*y+x*y+y*y
values1=expr4.subs({x:1,y:2})#.subs diyip({ şeklinde degisken yerine degerler ekleyebiliyoruz.})
factors3=factor(expr4)
print("Denklemimiz:",expr4)
print("Genis olan denklemin birlesmis hali",factors3)
print("x=1,y=2 girilmis hali denkleme deger olarak: ",values1)

print()
print("Not:")
print("x'e veya y degiskenine illa bir deger girmemize gerek yok baska tanımlı sembolleride girip sadece tek degiskene baglı denklemde yazılabilir.")
print()
print("Ornek:")
print("ornegin denklemimiz yine su sekil olsun:",factors3)
values2=factors3.subs({x:y+1})
print("x=y+1 yazarsak eger yeni denklemimiz: ")
pprint(values2)






