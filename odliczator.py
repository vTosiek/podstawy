import time
moj_czas = int(input("Wprowadź liczbę sekund:"))
for x in range (moj_czas , 0 , -1):
    sekundy = x % 60
    minuty = int(x / 60) % 60
    godziny = int(x / 3600) 
    print(f"{godziny:02}:{minuty:02}:{sekundy:02}")
    time.sleep(1)
    print("Koniec czasu!")