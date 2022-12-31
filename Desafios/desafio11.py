largura = float(input('Qual é a largura da parede ? '))
altura = float(input('Qual é a altura da parede ? '))
area = largura * altura
tinta = area  / 2

print('A área da parede com {}m de altura e {}m de largura é {}m2'.format(altura,largura,area))
print('Será necessário {} litros de tinta'.format(tinta))