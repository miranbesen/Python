import sympy as sym 
from sympy import Symbol
from sympy import pprint 


p=Symbol('p') #başarı olasılığı.
x=Symbol('x') #başarı sayısı denilebilir. 
n=Symbol('n') #deneme sayısı denilebilir.(Olayın kaç defa yapıldığı)

my_f_part1=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x)) #kombinasyon kısmını yapıyoruz burada yani n'in x'li kombinasyonu
print("formul 1.kisim=")
pprint(my_f_part1)
#---------------------
my_f_part2=p**x #başarı olasılığı^başarı sayısı 
print("formul 2.kisim=")
pprint(my_f_part2)
#---------------------
my_f_part3=(1-p)**(n-x)
print("formul 3.kisim=")
pprint(my_f_part3)
#---------------------
my_f=my_f_part1*my_f_part2*my_f_part3
print("formulun birlesmis hali=")
pprint(my_f)



#sym.plot(my_f.subs({n:50,p:0.5}),(x,0,50),ylim=[0,0.10],title='binomial distribution plot for n=50')
#burada ise başarı sayısının olmamasından 50 kez olma ihtimaline kadar bütün olasılık hesabını yapıyor.



x_values=[]
y_values=[]

for value in range(0,50):
    y=my_f.subs({n:50,p:0.5,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)


import matplotlib.pyplot as plt  


plt.plot(x_values,y_values)
plt.show()
