def listownik():
    a = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7,]
    b = []
    for klon in a:
        if klon not in b:
            b.append(klon)
    print(b)
    return b
listownik()

def setnik():
    a = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7,]
    c = list(set(a))
    print(c)
    return c
setnik()
