def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

""" def contador(i,f,p):
     #Docstring = manual que vai ser exibido ao importar-lo.
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

help(contador) 

def somar(a=0,b=0,c=0): #Parâmetros opcionais
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)

def teste():
    x = 8 # escopo local, só funciona dentro da função.
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste x vale {x}')

n = 2 #escopo global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')

def funcao():
    n1 = 4 # ao criar uma nova variavel com nome ja utlizado dentro de um escopo local, ele o faz localmente, sendo só chamado dentro.
    print(f'N1 dentro vale {n1}')

n1 = 2
print(f'N1 global vale {n1}')
funcao()

def teste(b):
    global a # ao utilizar global, eu especifico que quero usar a variavel global e substituo o A que está no escopo local.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

def somar(a=0,b=0,c=0): #função com retorno
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par.')
else:
    print('É ímpar.')
"""