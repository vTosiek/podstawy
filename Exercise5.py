import numpy as np
los1 = np.random.randint(1, 20, 15)
los2 = np.random.randint(1, 20, 15)
print(los1)
print(los2)

los3 = np.intersect1d(los1, los2)
print("Część wspólna:",los3)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for liczba in a:
    if liczba in b:
        c.append(liczba)
print(c)