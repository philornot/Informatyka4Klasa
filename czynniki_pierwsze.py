def czynniki(liczba):
    czynnik = 2
    czynniki = []
    while czynnik * czynnik <= liczba:
        while liczba % czynnik == 0:
            czynniki.append(liczba)
            liczba = liczba // czynnik
        czynnik += 1
    if liczba > 1: # została `liczba` większa od 1 <=> liczba jest liczbą pierwszą
        czynniki.append(liczba)
    return czynniki

print(czynniki(int(input("liczba="))))