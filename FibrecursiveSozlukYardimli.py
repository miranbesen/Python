#Sözlük yardimi alarak Fib bulma

known = {0:0,1:1}

def fiboRec(n):
    """
    if n<2:
        return n
    else:
        return fiboRec(n-1)+fiboRec(n-2)
    """

    if n in known:
        return known[n]
    else:
        result = fiboRec(n-1) + fiboRec(n-2)
        known[n] = result
        return result

print(fiboRec(7))
