time = []
carreira = {}
partida = []

while  True:
    carreira['nome'] = str(input('Nome do Jogador: '))
    c = int(input(f'Quantas partidas {carreira["nome"]} jogou? '))
    partida.clear()
    for n in range(0,c):
        partida.append(int(input(f'Quantos gols na partida {n}? ')))
    carreira['gols'] = partida[:]
    carreira['total'] = sum(partida)
    time.append(carreira.copy())
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('cod ', end='')
for i in carreira.keys():
    print(f'{i:>10}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 pra parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com códio {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')