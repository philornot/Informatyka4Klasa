def czy_pierwsza(liczba):
    pierwsza = False
    i = 2
    while i >= pierwsza ** 0.5:
        if liczba % i == 0:
            return False
        i += 1
    if liczba >= 2:
        return True
    else:
        return False


print(czy_pierwsza(64))
