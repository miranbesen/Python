from pprint import pprint as pp
from itertools import chain, combinations 

"""
    Sırt çantası problemi adı altında olan bu problem bir klasik yöneylem araştırması ve matematiksel olarak "kombinatik optimizaston" 
yöntemi adı altında geçiyor.Kapasitesi belirtilmiş olan bir çantamıza belirtilen kapasiteyi geçmiyecek şekilde eşyaları koyduğumuzu farz ediyoruz.
--> Çanta boyutu dışında başka kısıtlamalar da kullanıcı belirleyebilir.
-->Durumlar değişkendir. En hızlı olanı, en pahalı olanı,vs... Bu gibi kriterlere "Optimizasyon Kriteri" denir.
-->Farklı yöntem olarak belirlenebilen algoritmalar vardır. 
1-) Greedy Algorithms: 
    Aç gözlülük anlamındadır, bulunduğu durumda olan en yüksek veya en düşük şeklinde sıralanmış olan koşula göre direk
ilk indexten kabul edilecek şekilde çantaya koymayı amaçlar. En iyi durum olduğu söylenmez ama kullanılabilir.
 2-)chooseBest:
    Optimal: Çözümün en iyi sonucu vermesi demektir.(Bunu bulmak imkansız denilebilir. Çünkü kıyaslama sayısı arttıkca karmaşıklıkda arttığı için 
bulmak da gitgide zorlaşır.
--> Bütün olası durumlara power set denir. Bunun izlediği algoritma ise:
I-) Bütün durumları üretiriz.
II-) Şartı sağlamayanları çıkart.
III-) Şartı sağlayanları da maksimum olanları geri dönder.

"""

class Item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=v
        self.weight=w

    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self): #print işleminin böyle yapıldığını belirtiyor.
        result= '<'+self.name+', '+str(self.value)+', '+str(self.weight)+ '>'
        return result

def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()



def greedy(items,maxWeight,keyFunction):
    """Assumes Items a list, maxWeight>=0, keyFunction maps elements of Items to numbers"""
    itemsCopy=sorted(items,key=keyFunction,reverse=True) #büyükten küçüğe sıralamayı sağlar. True kısmını False yaparsak küçükten büyüğe sıralar.
    result=[]
    totalValue,totalWeight=0.0,0.0
    for i in range(len(itemsCopy)):
        if (totalWeight+itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalWeight+=itemsCopy[i].getWeight()
            totalValue+=itemsCopy[i].getValue()
    return(result, totalValue)


def buildItems():  #Tablomuzu oluşturduk.
    names=['clock','painting','radio','vase','book','computer']
    values=[175,90,20,50,10,200]
    weights=[10,9,4,2,1,20]
    Items=[]
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items


def testGreedy(items,maxWeight,keyFunction):  #keyFunction:Kriter olarak neye göre sıralıcağımızı belirler.
    taken,val=greedy(items,maxWeight,keyFunction)
    print('Total value of items taken is', val)
    for item in taken:
        print('     ',item)



def testGreedys(maxWeight=20):
    items=buildItems()
    print('Use greedy by value to fill knapsack of size',maxWeight) #maksimum value değerine göre koyuyoruz çantamıza.
    testGreedy(items,maxWeight,value)
    print('\nUse greedy by weight to fill knapsack of size',maxWeight) #minimum ağırlık olanlara göre koyarsak eğer çantamıza.
    testGreedy(items,maxWeight,weightInverse)
    print('\nUse greedy by density to fill knapsack of size',maxWeight) #Yöğunlukları büyük olanları çantaya koyuyor. En yüksek Value değerini bu şekil sağlıyoruz.
    testGreedy(items,maxWeight,density) #density=yoğunluk(Value/getWeight)



def chooseBest(pset,maxWeight, getVal, getWeight): #MaxWeight değerine göre en iyi şekilde value değerini elde etmemizi sağlıyor. 
    bestVal=0.0
    bestSet=None
    for items in pset:
        itemsVal=0.0
        itemsWeight=0.0
        for item in items:
            itemsVal+=getVal(item)
            itemsWeight+=getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal=itemsVal
            bestSet=items
    return (bestSet,bestVal)


def testBest(maxWeight=20):
    items=buildItems()
    pset=genPowerset(items) #karmaşıklık 0(n) iken genPoweset yüzünden 0(n*2^n) oluyor. || pset: Olası bütün durumlar.
    taken,val= chooseBest(pset,maxWeight, Item.getValue,Item.getWeight)
    print('Total value of items taken is',val)
    for item in taken:
        print(item)


def genPowerset(iterable): #olabilecek bütün koşulları kombine etmeye yarıyor.
    "powerset([1,2,3])--> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)" #Bütün olası değerleri kombine eder.
    s=list(iterable)
    return chain.from_iterable(combinations(s,r)for r in range(len(s)+1))



testGreedys()
print("\n--------------------------------\n")
testBest() 