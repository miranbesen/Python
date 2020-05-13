"""
Decision trees: Bu şekilde böl parçala yöntemi ile sırt çantasına çözüm bulabilirmiyiz diye bakıcaz.


"""

def maxValue(toConsider,avail):

    if toConsider==[] or avail==0: #eğer boş ise diye kontrol yapıyoruz.
        result=(0,())
    elif (toConsider[0].getWeight()>avail): #eğer ağırlığı fazla ise çantadan çıkarıyoruz.
        result=maxValue(toConsider[1:],avail)
    else: #eğer ağırlık çantadan büyük değilse çantaya ekliyoruz
        nextItem=toConsider[0] #çantaya koyulacak eleman
        leftNodeVal,leftNodeTake=maxValue(toConsider[1:],avail-nextItem.getWeight()) #çantaya koyduktan sonra koyulmuş haliyle recursive çağırım yapıyoruz.
        leftNodeVal+=nextItem.getValue() #çantaya koyuyoruz.
        rightNodeVal,rightNodeTake=maxValue(toConsider[1:],avail) #çantaya almadığı durumda kıyaslama yapmak için birde böyle değerlendiriyoruz.
        if (leftNodeVal>rightNodeVal): #Hangisi büyük diye kıyaslama yapıyoruz.
            result=(leftNodeVal,leftNodeTake+(nextItem,)) #tuple eleman toplami yapıyoruz.
        else:
            result=(rightNodeVal,rightNodeTake)

    return result




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

def smallTest():
    name=['a','b','c','d']
    value=[30,7,8,9]
    weight=[5,1,1,2]

    Items=[]
    for i in range(len(value)):
        Items.append(Item(name[i],value[i],weight[i]))
    
    val,taken=maxValue(Items,5)
    for item in taken:
        print(item)
    print("Total value of items taken=",val)

import random

def buildManyItems(numItems,MaxVal,MaxWeight):
    items=[]
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1,MaxVal),
                          random.randint(1,MaxWeight)))

    return items

import pprint 

def bigTest(numItems):
    items=buildManyItems(numItems,10,10)
    val, taken=maxValue(items,20)
    print('Items is taken')
    for item in taken:
        print(item)
    print("Total value of items taken=",val)


def fastMaxVal(toConsider,avail,memo={}):
    
    if ((len(toConsider),avail) in memo):
        result=memo[(len(toConsider),avail)]
    elif toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getWeight()>avail:
        result=fastMaxVal(toConsider[1:],avail,memo)
    else:
        nextItem=toConsider[0]
        leftNodeVal,leftNodeTake=fastMaxVal(toConsider[1:],avail-nextItem.getWeight(),memo) #çantaya koyduktan sonra koyulmuş haliyle recursive çağırım yapıyoruz.
        leftNodeVal+=nextItem.getValue() #çantaya koyuyoruz.
        rightNodeVal,rightNodeTake=fastMaxVal(toConsider[1:],avail,memo)
        if (leftNodeVal>rightNodeVal): #Hangisi büyük diye kıyaslama yapıyoruz.
            result=(leftNodeVal,leftNodeTake+(nextItem,)) #tuple eleman toplami yapıyoruz.
        else:
            result=(rightNodeVal,rightNodeTake)
    
    memo[(len(toConsider),avail)]=result
    return result





items=buildManyItems(10,5,5)
val, taken = fastMaxVal(items,10)
for item in taken:
        print(item)
print("Total value of items taken=",val)


