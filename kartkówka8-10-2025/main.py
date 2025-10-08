wyr = input("").split()
stos = ['#']
for i in wyr:
    if '0' < i < '9':
        print(i, end=' ')
    elif i in ['+', '-', '*', '/', '^']:
        stos.append(i)
    elif i == ')':
        while stos[-1] not in ['(', '#']:
            print(stos[-1], end=' ')
            stos.pop()

while stos[-1] != '#':
    print(stos[-1], end=' ')
    stos.pop()
# 2 + 2 -> 2 2 +
