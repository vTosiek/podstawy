a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = []
for chuj in a:
    if chuj <= 5:
        b.append(chuj)
    else:
        continue
print(b)

print([chuj for chuj in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if chuj <= 5])

c = int(input("Wprowadź maksymalną liczbę z listy:"))
d = []
for dupa in a:
    if dupa <= c:
        d.append(dupa)
    else:
        continue
print(d)
print([cycki for cycki in a if cycki <= c ])
    


