valores = []
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-='*15)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()



"""
 num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.pop()
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4) # elimina a primeira ocorrência do valor que tu mandou eliminar
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores.append(5)
valores.append(9)
valores.append(4)

valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a[:] # jeito de fazer uma cópia de uma lista ao inves de uma ligação.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
 """

