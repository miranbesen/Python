list_1=[1,4,7,84,3,62,23]
my_d=dict()

my_d={1:'bir',2:2,'3':'three'}

for key in my_d.keys():
    print(key,my_d[key])


if -10 not in my_d:
    my_d[-10]=50
    
print(my_d)

def my_h(list_1):
    my_d={}
    for item in list_1:
        if item not in my_d:
            my_d[item]=1
        else:
            my_d[item]=item+1
    return my_d
print(my_h(my_d))

def lookup(d,v): #bir dictioratiy birde value yolluyoruz
    print(d,v)
    for key in d:
        if d[key]==v:
            return key
    else: #for else yapisi farkli sekilde 
            return -1


print(my_d)
lookup(my_d,2)
