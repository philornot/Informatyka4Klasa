n = 100
tab = [0] * n

i = 0
while i < n:
    tab[i] = i
    i += 1

i = 2
while i < n:
    if i == 0:
        continue
    x = i * i  # czy tu powinno być * 2? bo tak też działą
    # print(f'i={i}, x ={x}, n={n}')
    while x < n:
        tab[x] = 0
        x += i

    i += 1

for i in tab:
    if i != 0 and i != 1:
        print(i, end=' ')
