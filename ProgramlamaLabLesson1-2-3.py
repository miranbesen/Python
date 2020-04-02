import random

print(random.random())

s=random.randint(1,100) #random.randint(min,max)
print(s)

def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

print(get_n_random_numbers())

#--------------------------------------------histogram with two methods(iki yöntemli histogram)-------------------------------------------------
#for a list [0,-4,8,-1,0,-3,6,3,0,1]
#get the histogram, with array of tuples format
histogram_1=[(-4,1),(-3,1),(-1,1),(0,3),(1,1),(3,1),(6,1),(8,1)] #tuple seklinde 
print(type(histogram_1)) #şu anda liste şeklinde 

my_list=[-7,-1,-3,9,0,-9,-2,4,-1,8]

# my_list=sorted(my_list) böyle yazarsak eğer sıralamıs oluruz listeyi

print(sorted(my_list))

def my_frequency_with_dict(list):
    frequency_dict={} #dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]+=1
        else:
            frequency_dict[item]=1

    return frequency_dict


print(my_frequency_with_dict(my_list))

def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]): #burada listedeki eleman eğer frekans listemizde var ise değer kısmına bir tane daha ekliyor.
                frequency_list[j][1]+=1
                s=True
        if(s==False): #eleman önceden eklenip eklenmediğini kontrol ediyor.
           frequency_list.append([list_1[i],1])

    return frequency_list

my_list2=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4] 

result_1=my_frequency_with_dict(my_list2)
result_2=my_frequency_with_list_of_tuples(my_list2)

print("sozluk seklinde histogram:")
print(result_1)
print("tuple(demet) seklinde histogram:")
print(result_2)

#------------------------------------------------------mode of a list with histogram-------------------------------------------------------------

#mode: en cok tekrar eden eleman 
print(30*"-","mode kismi",30*"-")
print("")
print("mode'nin histogramla yapilmis hali:")

my_list_1=get_n_random_numbers(10)
my_hist_d=my_frequency_with_dict(my_list_1)

print(my_hist_d)

#my_hist_l=my_frequency_with_list_of_tuples(my_list_1)

#print(my_hist_l)


#frequency_max=-1
#mode=-1

#for key in my_hist_d.keys():
#    if my_hist_d[key]>frequency_max:
#        mode=key
#        frequency_max=my_hist_d[key]

#print(mode,frequency_max) #burada denemesi yapılıyor simdi bunu fonksiyona yerleştiricez.


def my_mode_with_dict(my_hist_d): #histograma göre maksimum mode bulmaya yarar.
    frequency_max=-1  #frekansı maksimum olanı bulmaya yarar yani bir nevi value karşılığı en yüksek olan demek.
    mode=-1 #frekansi maksimum olan keyin atamasını yapıyoruz buna.
    for key in my_hist_d.keys():
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key

    return mode,frequency_max


print(my_mode_with_dict(my_hist_d))


#------------------------------------------mode of a list with histogram (a list of tuples)------------------------------------------------------ 

#burda da tupleye(demete) göre en yüksek tekrar eden sayının frekansını buluyor(mode)

print("demet ile yapicaz simdi de mode'yi:")
my_list_2=get_n_random_numbers(10)
my_hist_list=my_frequency_with_list_of_tuples(my_list_2)

print(my_hist_list)


#frequency_max=-1
#mode=-1

#for item,frequency in my_hist_list:
#    if frequency>frequency_max:
#        frequency_max=frequency
#        mode=item

#print(mode,frequency_max)

def my_frequency_with_list_of_tuples(my_hist_list):
    frequency_max=-1
    mode=-1

    for item,frequency in my_hist_list:
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item

    return mode,frequency_max

print(my_frequency_with_list_of_tuples(my_hist_list))

#------------------------------linear search on list-------------------------------------------------------------------------------------------

#bu kısımda ise aramak istedigimiz degerin hangi indexde olduğunu beraberinde veren fonksiyonu yazıcaz.

print("")
print("linear search on list kismindayiz:")

def my_search(my_list,item_search):
    found=(-1,-1) #iki tane degisken var biri hangi elemanın olduğunu diğeri de kaçıncı indexte olduğunu bulmamızı sağlar.
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)
            #break koyarsak eğer değerin ilkini bulduktan sonra çıkar, break yoksa son bulduğu indis numarasi ile çıkar

    return found

print(my_list)

found=my_search(my_list,4)
print("{}.sayisi listenin {}.indisinde".format(found[0],found[1]))

#print(my_search(my_list,4))

#-------------------------------------------------------------------mean of list-----------------------------------------------------------------
print("")
print("mean kismindayiz(ortalama bulma):")

def my_mean(my_list):
    s,t=0,0 #s=eleman sayisi ,t=eleman sayilari toplami

    for item in my_list:
        s=s+1
        t=t+item

    mean_=t/s

    return mean_

print(my_list)
print(my_mean(my_list))


#---------------------------------------------------------------sort the list--------------------------------------------------------------------
print("")
print("sort the list kismindayiz(siralama)")
print("")
print("listenin normal hali:")
print(my_list)

def my_bubble_sort(my_list):
    n=len(my_list)

    for i in range(n-1,-1,-1): #listenin en sonuncu elemanindan bir bir azalarak  devam eder. 
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp


    return my_list



print("listenin siralanmis hali:")
print(my_bubble_sort(my_list))



#---------------------------------------------------binary search on a sorted list---------------------------------------------------------------

#aramanın en hızlı yolu bu olduğu için genellikle bu tercih ediliyor. Linear searchla aynı işlevde
print("binary search on a sorted list kismindayiz(arama islemi):")
print(30*"-","binary search on a sorted list",30*"-")
print("")
#print(my_list)

def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1
    denemesay=0
    while high>=low:
        mid=(high+low)//2
        denemesay+=1
        if (item_search==my_list[mid]):
            #print("deneme sayisi:",denemesay)
            return my_list[mid],mid
        elif (my_list[mid]>item_search):
            high=mid-1
        else:
            low=mid+1
    
    return found

my_list_3=[-5,-4,2,5,6,9,11,13,18,21,23]
#my_list_3=[-5,-4,2,5,6,9,11,13,18,21,23] eğer böyle bir liste olsaydı deneme sayimiz=4 oluyordu (-4 ü aradıgımızı farz ederek)
print(my_list_3)
print(my_binary_search(my_list_3,-4))
#print("aradigimiz sayi ve bulundugu yer=",my_binary_search(my_list,4))


#------------------------------------------------------median of a list------------------------------------------------------------------------

#siralanmis bir listede ortadaki eleman demek medyan değeri


print("median of a list kismindayiz(ortadaki deger):")

print(30*"-","median of a list",30*"-")
print("")


size=input("dizi boyutunu giriniz:")
size=int(size) #convert to str to int

my_list_5=get_n_random_numbers(size,-10,10)

#print("liste:",my_list_5)

def my_median(my_list_5):
    my_list_6=my_bubble_sort(my_list_5)

    print(my_list_6)

    n=len(my_list_6)

    if (n%2==1):
        middle=int(n/2)
        median=my_list_6[middle]
        

    else:
        middle_1=my_list_6[int(n/2)]
        middle_2=my_list_6[int(n/2)+1]
        median=((middle_1+middle_2)/2)
    
    return median


print("medyan degeri:",my_median(my_list_5))






        