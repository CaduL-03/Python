i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
n = 0
for c in range(1, 11):
    n += 1
    print(i + p*(n - 1))