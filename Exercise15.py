def tylny():
    przyklad = input("Wprowadź przykładowy tekst: ")
    wynik = przyklad.split()
    tyl = wynik[::-1]
    polacz = " ".join(tyl)
    print(polacz)
    return polacz
tylny()