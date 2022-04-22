import math
angulo = float(input('Digite um angulo: '))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O angulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O angulo de {:.2f} tem o TANGENTE de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))
