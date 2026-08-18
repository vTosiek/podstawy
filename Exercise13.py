def fibo():
    a = [1]
    liczba_fibo = int(input("Ile liczb fibonacciego mam wygenerować?: "))
    for liczba in range(0, liczba_fibo):
        a.append(a[liczba] + a[liczba - 1])
    return a
lista = fibo()
print(lista)
    