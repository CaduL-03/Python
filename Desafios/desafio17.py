from math import sqrt

op = float(input('Cateto oposto: '))
ad = float(input('Cateto adjacente: '))
con = sqrt(op**2 + ad**2)
print('A hipotenusa desse triangulo é: {}'.format(con))