n = int(input('Digite um número: '))
cont = 0
for x in range(1, 11):
    cont = cont+1
    resul = n*x
    print('{}X{} = {}'.format(n,cont,resul))