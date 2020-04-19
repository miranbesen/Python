#Ad Soyad: Miran Besen ||| Numara:190401080
#GitHub Link: https://github.com/miranbesen/Prog_Lab/tree/master/HW3_Week2_Sym_Klasik_PDF_Graph

"""(Uniform Distribution)
x random olan değişkeniminizin alabileceği değerlerin aralığı(a,b) olsun. Eğer a ile b aralığında olan tüm değerlerin alabileceği
değerler aynı ihtimalle sonuç alıyorsa, bu dağılıma uniform dağılım diyoruz. x'imizin olasılık fonksiyonu da;
x= 1/(b-a) olur.
x değerimizin a ile b dışında herhangi bir değer de olursa eğer 0 değeri alması gerekir.
Örnek olarak; Bir zar atılma durumunu diyebiliriz. Hilesiz bir zar atıldığında ortaya çıkan  sonuçların olasılığı(1,2,3,4,5,6) 
1/6'dır.
Eğer bu dağılımın olasılık yoğunluk fonksiyonunu gösterecek olursak eğer:
          
           /                                         \
          /     1/(b-a)       eğer a<=x<=b,           \
          \                                           /
f(x)=     /                                           \
          \                                           /
          /       0          diğer( x<a veya x>b)     \
         /                                             \
         \                                             /
"""

import sympy as sym
from sympy import Symbol
from sympy import Piecewise #parçalı fonksiyon yazabilmek için çağırdık
import sympy.plotting as syp
import matplotlib.pyplot as plt
b=Symbol('b')
a=Symbol('a')
x = Symbol('x')
formul=1/(b-a)
maks=int(input("maksimum degeri giriniz:")) # b degeri
#input ile 4 degerini girdim maksimuma
min=int(input("minimum degeri giriniz:"))  # a degeri
#input ile 2 degerini girdim minimuma
if(maks<min):
    print("maksimum veya minimum degerleri yanlis girdiniz(otomatik yer degistiriliyor)")
    temp=maks
    maks=min
    min=temp

syp.plot(Piecewise((0,(x<min) | (x>maks)),(formul.subs({a:min,b:maks}),(x>=min) & (x<=maks))),(x,-10,10),title="Uniform Distribution Graph")
#Piecewise fonksiyonunun ilk parametresi koşul, ikinci parametresi şarttır.

#-------------------------------------------matplotlib ile cizilmis kismi----------------------------------------------------------

y_values=[]
x_values=[]
piecewise_function=Piecewise((0,(x<min) | (x>maks)),(formul.subs({a:min,b:maks}),(x>=min) & (x<=maks))).evalf()
#fonksiyonu direk dongude belirtip x degeri girince hata veriyor. Bunun için ayrı tanımladık.

x_values_start=0.
#float sayılar ile grafik daha düzgün oluyor diye floatlar ile grafiği çizdirdik.

while(x_values_start<10.0):
    y=piecewise_function.subs({x:x_values_start})
    y_values.append(y)
    x_values.append(x_values_start)
    #print(x_values_start,y)
    x_values_start+=0.1


#plt.plot(x_values,y_values)