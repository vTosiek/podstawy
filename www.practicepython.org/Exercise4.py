def x():
    return int(input("Wprowadź liczbę:"))
wpis = x()
lista = range(1, wpis)
dzielniki =[]
for chuj in lista:
    if wpis % chuj == 0:
        dzielniki.append(chuj)
    else:
        continue
print(f"To jest lista dzielników Twojej liczby: {dzielniki}")
