"""
1-)min_heapify:Bu fonksiyonumuzda elimizdeki diziyi ağaç şeklinde düşünürsek eğer parentlerin childlardan küçük olması gerekiyor.
Eğer değil ise bu diziyi o şekilde ayarlama yapıyor. 
2-)build_min_heap: Bu fonksiyonumuzda ise diziyi kıyaslamaya yapmaya başlıcağımız en büyük child olmayan index numarasından başlayarak(en yüksek index numaralı parent) 
bir eksilerek childları arasında kıyaslama yapmak için min_heapify fonksiyonuna i değerini yollar
3-)heapsort: Elimizde olan diziyi küçükten büyüğe sıralamaya yarar. Bunuda şöyle bir yol  izler:
 1- ilk başta diziyi min_heap haline getirir. 
 2-Sonra bu diziyi ağaç şeklinde düşünecek olursak eğer kök kısmı en küçük eleman olur. Bu eleman ile en sonki child' ı yer 
 değiştirme yapıyoruz.
 3- Yerdeğiştirmeden sonra yeni açtığımız diziye en sonki child'ı eski diziden çıkartıp yeni dizimize ekliyoruz. 
 4- Sonra min_heap  fonksiyonuyla tekrar dizimizi min_heap haline getiriyoruz.
  Bu sekilde yeni olusan dizimiz küçükten büyüğe bir şekilde sıralanmış oluyor.
4-)insertItemToHeap: Minheap halinde olan dizimize eleman eklemeye yarıyor. Bunuda 
1-Eleman ekledikten sonra o elemanı tutan bir değişken atanır.
2-Parent'i bulunur 
3-Eğer parent küçük ise tuttuğumuz değişkenden yer değiştirme işlemi yapılır.
4-Sonra tuttuğumuz değişken eğer index numarası küçüldü ise(yani yer değiştirme yapıldıysa) yeni parent berlirlenir.
5- köke kadar kıyaslama yapılır ve minHeap hali bozulmamıs bir şekilde eleman eklenmiş olur.
5-)removeItemFrom: Minheapimizin kökünü cikartip yeniden minheap yapısının bozulmamasını saglıyor. Bunuda;
1-Önce kök ile en son ki elemanimizin yerini degistiriyoruz ve sonuncu elemanimizi cikartiyoruz
2-Elimizdeki ağacta kökümüz en sonki eleman oluyor. Bunu childlariyla kıyaslama yapıyoruz.
3-Kiyaslamaya göre uygun şekilde yeniden yer değiştirmeler yaparak ağacımızı minHeap bicimini aldırıyoruz.


"""


my_array_1=[8,10,3,4,7,15,1,2,16]

def min_heapify(array,i):
    left=2*i+1 
    right=2*i+2
    length=len(array)-1
    smallest=i

    if left<=length and array[i]>array[left]: #sol child'ın dizinin uzunlugundan büyük olmaması şartı & parentin sol childtan büyük olma şartı.
        smallest=left
    if right<=length and array[smallest]>array[right]: #sag child'ın dizinin uzunlugundan büyük olmaması şartı & smallest'in sag childtan büyük olma şartı.
        smallest=right
    if smallest!=i: #smallest üzerinde değişiklik yapma şartı
        array[i],array[smallest]=array[smallest],array[i]
        min_heapify(array,smallest) # yer değişikliğinden sonra bir sonraki childlar ile kıyaslama yapar.

def build_min_heap(array):
    for i in reversed(range(len(array)//2)): #reverse: tersten azalarak gider.
        min_heapify(array,i)


def heapsort(array):
    array=array.copy() #bu sekilde diziyi kopyalamasak dizide değişiklik yapınca eskisinde de değişiklik yapmış olurduk.
    build_min_heap(array) #dizimizi min_heap haline getirdik.
    sorted_array=[] 
    for _ in range(len(array)): #_ :Kullanmadığı değişkene '_' bu ismi atıyor.
        array[0],array[-1]=array[-1],array[0] # kök ile son child' ı yer değiştirir.
        sorted_array.append(array.pop()) #yeni dizimize diğer dizinin cikardığımız son child'ı ekleriz.
        min_heapify(array,0) #sonra tekrar min_heapify haline getiririz.
    return sorted_array

def insertItemToHeap(myheap_1,item):
           
     myheap_1.append(item)
     current=len(myheap_1)-1
     parent=(current-1)//2
     while (parent>=0 and myheap_1[current]<myheap_1[parent]): #yani item'i tutan current < parent ise (bir nevi bubleup gibi düşünebiliriz.)
         myheap_1[current],myheap_1[parent]=myheap_1[parent],myheap_1[current] #swap işlemi yapıldı.
         current=parent
         parent=(current-1)//2
     
#Dizimizin sonuncu elemanini cikarmaya yariyor.
#def removeItemFrom(myheap_1): 
#    uzunluk=len(myheap_1)
#    if (uzunluk>0):
#       myheap_1.pop()
#    else:
#        print("heap'te cikarilacak eleman bulunmamaktadir.") 

def removeItemFrom(myheap_1):
   uzunluk=len(myheap_1)-1
   index=0 #kökü tutuyor.
   left=2*index+1 #ilk başta kökün solu 
   right=2*index+2 #ilk başta kökün sagı
   if(uzunluk>=0):
       myheap_1[-1],myheap_1[0]=myheap_1[0],myheap_1[-1] #kök ile sonuncu elemanı yer değiştirdik
       myheap_1.pop() #kökü yani en küçük elemanı cikarttik.
       while((uzunluk>left and left<myheap_1[index]) or (uzunluk>right and right<myheap_1[index])): # indeximiz yani ilk durum için kökümüz sol veya sağdan büyük ise
           if(right<left): #sol child, sag child'dan büyük koşula girer.
               myheap_1[index],myheap_1[right]=myheap_1[right],myheap_1[index] #sag child'ı parent konumuna getiriyoruz, parenti de sağ tarafa getiriyoruz.
               index=2*index+2 #sag tarafa geçtiği için iki ile çarpıp topluyoruz..
           else:
                myheap_1[index],myheap_1[left]=myheap_1[left],myheap_1[index] 
                index=2*index+1
           left=2*index+1
           right=2*index+2
   else:
        print("heap'te cikarilacak eleman bulunmamaktadir.")
        return ''


my_array_1=[8,10,3,4,7,15,1,2,16]

print("dizinin normal hali:")
print(my_array_1)
build_min_heap(my_array_1)
print("min heap yapilmis hali:")
print(my_array_1)

my_array_2=heapsort(my_array_1)
print("heapsort yaptiktan sonra:")
print(my_array_2)

print("insert islemleri:")
insertItemToHeap(my_array_1,13)
insertItemToHeap(my_array_1,6)
print(my_array_1)

print("remove islemi(son eleman cikiyor):")
removeItemFrom(my_array_1)
print(my_array_1)






