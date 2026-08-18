import random
def cow():
    print("Witam w grze krowy i byki!")
    losowiak = random.randint(1000, 9999)
    proby = 0
    while True:
        liczba = int(input("Wprowadź 4 cyfrową liczbę!"))
        if liczba < 1000:
            print("To nie jest 4 cyfrowa liczba, Spróbuj jeszcze raz!")
            continue
        elif liczba > 9999:
            print("To nie jest 4 cyfrowa liczba, Spróbuj jeszcze raz!")
            continue
        else:
            a = [int(x) for x in str(abs(liczba))]
            b = [int(x) for x in str(abs(losowiak))]
            krowa = 0
            byk = 0
            for cyfra1, cyfra2 in zip(a, b):
                if cyfra1 == cyfra2:
                    krowa += 1
                elif cyfra1 in b:
                    byk += 1
            proby += 1
        print (f"krowy:{krowa}")
        print (f"byki:{byk}")
        if krowa == 4:
            print(f"Gratulacje! Odgadłeś liczbę {losowiak} w {proby} próbach!")
            break

cow()

