a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite o último número: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {} e o menor {}.'.format(maior,menor))