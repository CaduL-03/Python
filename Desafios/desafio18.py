import math

ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo {} tem o seno: {:.2f}; \n o cosseno: {:.2f}; \n e tangente {:.2f}'.format(ang, sen, cos, tan))