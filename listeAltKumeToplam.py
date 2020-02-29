def listeAlt(liste=[4,-3,15,-10,5,-8,2]):
    
    max=0

    for i in range(len(liste)):
        sum=0 
        for j in range(i,len(liste)):
             sum=sum+liste[j]
             if max<sum:
                 max=sum
    return max
   

liste=[4,-3,15,-10,5,-8,2]
print(listeAlt(liste))
