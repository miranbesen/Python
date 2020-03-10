def buble_sort():

    liste = [12,4,124,5,3,0,-12,24,9,14]

    for i in range(len(liste)):
        for j in range(len(liste)-1):
            print(i,j)
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j]=liste[j+1]
                liste[j+1] = temp

    return liste

print(buble_sort())
