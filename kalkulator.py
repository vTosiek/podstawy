import math
while True:
    print ("==== Kalkulator ====")
    print ("==== 1. Dodawanie ====")
    print ("==== 2. Odejmowanie ====")
    print ("==== 3. Mnożenie ====")
    print ("==== 4. Dzielenie ====")
    print ("==== 5. Pierwiastkowanie ====")
    print ("==== 6. Zakończ ====")

    try:
        dzialanie = int(input("Wybierz działanie: "))
    except ValueError:
        print ("Błąd! Musisz wpisać cyfrę od 1 do 6")
        continue
    
    if dzialanie == 6:
        print("Do Zobaczenia!")
        break
    
    try:
        if dzialanie in [1, 2, 3, 4]:                
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
        elif dzialanie == 5:
            a = float(input("Podaj podstawę pierwiastka: "))
        elif dzialanie not in [1, 2, 3, 4, 5, 6]:
            print ("Błąd! Nie ma takiego działania w menu")
        continue
    except ValueError:
        print ("Błąd! Musisz wpisać cyfrę od 1 do 6")
        continue
    match dzialanie:
        case 1:
            wynik = a + b
            if wynik is not None:
                print (f"{a} + {b} = {wynik}")
        case 2:
            wynik = a - b
            if wynik is not None:
                print (f"{a} - {b} = {wynik}")
        case 3:
            wynik = a * b
            if wynik is not None:
                print (f"{a} * {b} = {wynik}")
        case 4:
            if b == 0:
                print("Błąd! Nie można dzielić przez 0")
                wynik = None
            else:
                wynik = a / b
            if wynik is not None:
                print (f"{a} / {b} = {wynik}")
        case 5:
            if a < 0:
                print ("Błąd! Podstawa pierwiastka musi być dodatnia")
                wynik = None
            else:
                wynik = math.sqrt(a)
            if wynik is not None:
                print (f"Pierwiastek z {a} to {wynik}")
        case _:
            print("Nieznane działanie!")
            wynik = None


