def sito_eratostenesa(N):
    SITO = [False] * (N + 1)

    for i in range(2, N + 1):
        SITO[i] = True

    # Główny algorytm sita
    i = 2
    while i * i <= N:
        if SITO[i] == True:
            j = i * i
            while j <= N:
                SITO[j] = False
                j = j + i
        i += 1

    return SITO


def czy_liczby_znajdujace_sie_w_tablicy_tab_o_wielkosci_n_sa_liczbami_pierwszymi(tab):
    n = len(tab)  # n to długość tablicy
    for liczba in range(n):  # dla każdej liczby od 0 do n
        if tab[liczba] is True:  # jeśli w tablicy na indeksie liczba jest True,
            print(f'Liczba {liczba} jest liczbą pierwszą.')  # to znaczy, że ta liczba jest pierwsza.
        elif tab[liczba] is False:  # a jeżeli w tablicy na indeksie liczba jest False,
            print(f'Liczba {liczba} NIE jest liczbą pierwszą.')  # to znaczy, że to nie jest liczba pierwsza.


jakas_tablica = sito_eratostenesa(100)
czy_liczby_znajdujace_sie_w_tablicy_tab_o_wielkosci_n_sa_liczbami_pierwszymi(jakas_tablica)
