num = cont = soma = 0
while True:
    num = int(input('Digite um número (999 pra parar): '))
    if num == 999:
        break
    soma += num 
    cont += 1
    
print(f'Você digitou {cont} números e a soma entre eles foi de {soma}.')



""" 
cont = 1
while cont <= 10:
    print(cont, '-> ', end="")
    cont += 1
print('Acabou!')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')

nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome} tem {idade} anos e recebe ${salario} reais')
 """

