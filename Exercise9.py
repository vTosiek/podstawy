import random
print("=== Gra w zgadywanie cyfr ===")
wyjscie = False
while wyjscie == False:
    zgadnieto = False
    liczba = random.randint(1, 9)
    proby = 1
    while zgadnieto == False:
        strzal = input("Spróbuj zgadnąć cyfrę od 1 do 9: ")
        print(liczba)
        if strzal == "exit":
            zgadnieto = True
            wyjscie = True
        elif liczba == int(strzal):
            print(f"Trafiłeś w {proby} próbach!")
            zgadnieto = True
        elif liczba < int(strzal):
            print("Za dużo!")
            proby += 1  
        else:
            print("Za mało!") 
            proby += 1        
        
        
    
    

