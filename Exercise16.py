import random
import string
print("=== Generator haseł ===")
def generator():
    a =[]
    male = string.ascii_lowercase
    duze = string.ascii_uppercase
    cyfry = string.digits
    znaki = string.punctuation
    while True:
        try:
            dlugosc = int(input("Wprowadź liczbę znaków w twoim haśle: "))
            break
        except ValueError:
            print("To nie jest liczba! Wprowadź poprawną liczbę!")
    for liczba in range (dlugosc):
        los = random.randint(1, 4)
        if los == 1:
            a.append(random.choice(male))
        elif los == 2:
            a.append(random.choice(duze))
        elif los == 3:
            a.append(random.choice(cyfry))
        else:
            a.append(random.choice(znaki))
    polaczone = "".join(a)
    print(f"Oto twoje nowe hasło: \n{polaczone}")
    return polaczone
generator()
    
        
        
        