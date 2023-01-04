valores = []
par = []
impar = []

while True:
    n = (int(input('Digite um numero: ')))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
     impar.append(n)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if cont == 'N':
        break

print('-='*15)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')