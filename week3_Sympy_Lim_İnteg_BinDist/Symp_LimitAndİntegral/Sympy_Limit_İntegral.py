from sympy import Symbol,Limit,pprint

#----------------------------------------------------------------Limit yardımıyla türev alma---------------------------------------------------

t=Symbol('t')
print("denklemimiz=")
St=5*t**2+2*t+8 #türev alınacak olan denklem
pprint(St)

t1=Symbol('t1')
delta_t=Symbol('delta_t')
#(S(t1+delta(t))-S(t1))/delta(t)'ifademizin delta(t)-->0 ' a giderken ki limiti türev alma ile aynı anlamdadır.

St1=St.subs({t:t1}) #b kısmı 
St1_delta=St.subs({t:t1+delta_t}) #a kısmı
print()
print("Türev alinmis hali=")
pprint(Limit((St1_delta-St1)/delta_t,delta_t,0).doit()) #burada delta(t)'ye c dersek eğer formül uyarlamış hali a-b/c gibi düşünebiliriz.

#-----------------------------------------------------------İntegral kısmı--------------------------------------------------------------------------

print(50*"-")
print()
print("Olasılık dagilimina göre integral kismi:")
from sympy import Symbol,exp,sqrt,pi,Integral

x=Symbol('x')

p= exp(-(x-10)**2/2)/sqrt(2*pi)
#Normal dagilim icin olasılık formulumuz 
print("Formulumuz:")
pprint(p)


print()
print("formulumuzde x'in 11 ve 12 arası degerliklerin olma olasigi=")
print(Integral(p,(x,11,12)).doit().evalf())
#11 ile 12 arası olasılık degerini bize veriyor


import sympy as sym 
sym.plot(p.subs({pi:3}),(x,0,20),ylim=[0,0.40],title='probality density function')
#olasilik dagilim grafigimiz.