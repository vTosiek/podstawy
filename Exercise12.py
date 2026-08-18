a = [5, 10, 15, 20, 25, 30, 69]
ile_razy = int(input("Podaj liczbę liczb w liscie: "))
b = []
for ile in range(ile_razy):
    liczba = int(input("Wprowadź liczbę do listy: "))
    b.append(liczba)
def lista():
    return b[0], b[-1]
c = [lista()]
print(c)
