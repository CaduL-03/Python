lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        lista[l][c] = (int(input(f'Digite um valor [{l},{c}]: ')))
print('-='*50)
for l in range(0, 3):
    for y in range(0,3):
        print(f'[{lista[l][c]}]',end='')
    print('')