lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um valor [{l},{c}]: '))
print('-='*50)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{lista[l][c]}]',end='')
        if lista[l][c] % 2 == 0:
            spar += lista[l][c]
    print('')
print('-='*30)
print(f'A soma dos valores pares: {spar}')
for l in range(0,3):
    scol += lista[l][2]
print(f'A soma dos valores da terceira coluna: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = lista[1][c]
    elif lista[1][c] > mai:
        mai = lista[1][c]
print(f'O maior valor da segunda linha: {mai}')