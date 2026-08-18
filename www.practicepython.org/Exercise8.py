import os

print("=== Zagrajmy w papier, kamień, nożyce! ===")
print("=== Pamiętaj zasady! ===\n")
print("=== Kamień bije nożyce ===")
print("=== Nożyce biją papier ===")
print("=== Papier bije kamień ===\n")

nick1 = input("Wprowadź nazwę pierwszego gracza: ")
nick2 = input("Wprowadź nazwę drugiego gracza: ")

while True:
    Gracz1 = input(f" 1. Kamień \n 2. Nożyce \n 3. Papier\n {nick1} Twój ruch!: ")
    os.system("cls||clear")
    Gracz2 = input(f" 1. Kamień \n 2. Nożyce \n 3. Papier\n {nick2} Twój ruch!: ")
    if Gracz1 == Gracz2:
        print("Mamy remis!")
    elif Gracz1 == "1" and Gracz2 == "2":
        print (f"{nick1} wygrywa! ")
    elif Gracz1 == "1" and Gracz2 == "3":
        print (f"{nick2} wygrywa! ")
    elif Gracz1 == "2" and Gracz2 == "1":
        print (f"{nick2} wygrywa! ")
    elif Gracz1 == "2" and Gracz2 == "3":
        print (f"{nick1} wygrywa! ")
    elif Gracz1 == "3" and Gracz2 == "1":
        print (f"{nick1} wygrywa! ")
    elif Gracz1 == "3" and Gracz2 == "2":
        print (f"{nick2} wygrywa! ")
    elif Gracz1 == "koniec" or Gracz2 == "koniec":
        break
    else:
        print("Nieprawidłowe dane - Zacznijmy raz jeszcze")
