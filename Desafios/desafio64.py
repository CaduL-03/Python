num = 0
cont = 0
soma = 0
num = int(input('Digite um número (999 pra parar): '))
while num != 999:
    soma += num 
    cont += 1
    num = int(input('Digite um número (999 pra parar): '))
print('Você digitou {} números e asoma entre eles foi {}.'.format(cont,soma))
