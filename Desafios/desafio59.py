n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
ch = 0

while ch != 5:
    print('-='*11)
    print(""" 
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números 
    [ 5 ] Sair do programa""")
    print('-='*11)
    ch = int(input('Escolha sua opção: '))
    print('-='*11)
    if ch == 1:
        s = n1 +n2
        print('A soma de {} + {} é de {}'.format(n1, n2, s))
    elif ch == 2:
        m = n1 * n2
        print('A multiplicação de {} por {} é de {}'.format(n1,n2,m))
    elif ch == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é o {}'.format(n1,n2,n1))
        elif n1 < n2:
            print('O maior número entre {} e {} é {}'.format(n1,n2,n2))
    elif ch == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        
