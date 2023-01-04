galera = []
dados = []
c = 0
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    cont = ' '
    c += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('-='*15)
print(f'Ao todo você cadastrou {c} pessoas.')
print(f'O maior peso foi de {mai}Kg. ', end='')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}Kg. ', end='')
for p in galera:
    if p[1] == men:
        print(f'{p[0]} ', end='')



""" teste = []
teste.append('Carlos')
teste.append(19)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])
print(galera) 

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nosme: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
"""

