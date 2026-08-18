while True:
    try:
        liczba1 = int(input("Wprowadź pierwszą liczbę:"))
    except ValueError:
        print("Proszę wpisać liczbę!")
        continue
    if liczba1 == 0:
        print("Twoja liczba to zero")
    elif liczba1 % 4 == 0:
        print("Twoja liczba jest podzielna przez 4, 2 oraz 1")
    elif liczba1 % 2 == 1:
        print("Twoja liczba jest nieparzysta")
    else:
        print("Twoja liczba jest parzysta")
        
    try:
        liczba2 = int(input("Wprowadź drugą liczbę:"))
    except ValueError:
        print("Proszę wpisać liczbę!")
        continue
    if liczba2 == 0:
        print("Twoja liczba to zero")
    elif liczba2 % 4 == 0:
        print("Twoja liczba jest podzielna przez 4, 2 oraz 1")
    elif liczba2 % 2 == 1:
        print("Twoja liczba jest nieparzysta")
    else:
        print("Twoja liczba jest parzysta")
        
    if liczba1 % liczba2 == 0:
        print("Twoja pierwsza liczba dzieli się przez drugą bez reszty!")
    else:
        print("Twoje liczby nie dzielą się przez siebie bez reszty...")
        
