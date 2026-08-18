print("=== Sprawdzacz do palindromów ===")

while True:
    a = input("Wprowadź słowo, a program sprawdzi czy jest palindromem: ")
    if a == a[::-1]:
        print("Słowo jest palindromem!")
    else:
        print("Słowo nie jest palindromem!")
        
            
    
    