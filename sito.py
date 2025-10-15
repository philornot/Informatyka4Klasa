n = 100000
tab = [0] * n

i = 0
while i < n:
    tab[i] = i
    i += 1

i = 2
while i < n:
    if i == 0:
        continue
    x = i * i
    # print(f'i={i}, x ={x}, n={n}')
    while x < n:
        tab[x] = 0
        x += i

    i += 1

for i in tab:
    if i != 0 and i != 1:
        print(i, end=' ')
