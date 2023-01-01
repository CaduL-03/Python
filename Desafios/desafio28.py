import random

num = random.randint(0,5)
perg = int(input('Digite um número entre 0 e 5: '))
if perg == num:
    print('Você acertou!')
else:
    print('Você errou! O número da vez foi {}'.format(num))



""" 
nome = str(input('Qual é seu nome ? '))
if nome == 'Carlos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim')
 """

