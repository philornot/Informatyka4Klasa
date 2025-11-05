def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x - 6


def znajdz_mz(a, b, dokladnosc=0.0001):
    if b < a:
        a, b = b, a  # zamieniamy a i b, jeśli b < a
    while b - a > dokladnosc:
        srodek = (a + b) / 2
        if f(srodek) == 0:
            return srodek
        if f(a) * f(srodek) < 0:
            b = srodek
        else:
            a = srodek

    return (a + b) / 2


print(znajdz_mz(10000, -10000))
