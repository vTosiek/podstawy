
imie = input("Wprowadź swoje imię:")
print("Twoje imię to " + imie)
while True:
    try:
        wiek = int(input("Wprowadź swój wiek:"))
    except ValueError:
        print("Błąd! Proszę wpisać liczbę!")
        continue
    teraz = 2026
    starosc = (2026 - wiek) + 100
    print(f"{imie} w roku {starosc} będziesz miał 100 lat!")

