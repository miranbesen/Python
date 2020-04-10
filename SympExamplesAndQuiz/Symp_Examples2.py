import sympy as sym 
# as kullanımı bir kütüphaneyi veya bir modülü istediğimiz ad ile kullanmamızı sağlar.
from sympy import Symbol
from sympy import pprint

#------------------------------------------------------------------Formul olusturma-----------------------------------------------------------------------
print("Formul olusturucaz=")
sigma=Symbol('sigma')
x=Symbol('x')
mu=Symbol('mu')

part_1=1/(sym.sqrt(2*sym.pi*sigma**2)) #formulumuzun 1 kismi
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2)) #formul 2 kisim
print()
print("gauss formul 1 kisim:")
pprint(part_1)
print("gauss formul 2 kisim:")
pprint(part_2)
print()
pprint("gauss formulu:")
gauss_function=part_1*part_2
pprint(gauss_function)
print()
print("gauss formulune sigma degeri =3, mu degeri =1 girersek eger yeni formul halimiz:")
values_gauss=gauss_function.subs({sigma:3,mu:1})
pprint(values_gauss)


import sympy.plotting as syp 
## Grafik gösterimi için dahil edilen fonksiyondur.
#syp.plot(gauss_function.subs({mu:10,sigma:30}),(x,-1000,1000),title='gauss distribution') 
#plot fonksiyonu grafik cizimlerinde kolaylık saglayan bir fonksiyondur. 
#ilk parametre fonksiyonun kendisi, ikinci parametre'de artis miktarını verir neye baglıysa formül veya denklem(grafik için kulanıyoruz) 

#----------------------------------------------------------------.evalf fonksiyonu()------------------------------------------------------------
x_values=[]
y_values=[]
print()
print(50*"-")
print("x degerine gore y degeri degisimi:")
print()
for value in range(-5,5):
    y=gauss_function.subs({mu:10,sigma:30,x:value}).evalf() 
#.evalf(): sqrt veya exp gibi fonksiyonların sayısal degerlerini elde etmemizi saglar. 
#Bu sayede x degerine göre y degerinin artis miktarını görebiliriz.
    y_values.append(y)
    x_values.append(value)
    print(value,y)
#------------------------------------------------------------matplotlib.pyplot fonksiyonu------------------------------------------------------------------------

print()
print(50*"*")
print("Grafik hali:")
print()
import matplotlib.pyplot as plt  
#matplotlib:Pythonda veri görsellestirmeye yarayan kütüphanedir.
#.pylot:Çizim icin kullanılan baska bir method da budur. Grafik islemleri icin kullanılır.

plt.plot(x_values,y_values)
#.plot(): Bu method yardımıyla grafik olusturabiliriz.
plt.show() 
#.show(): Çizim gösterimini sağlar.





