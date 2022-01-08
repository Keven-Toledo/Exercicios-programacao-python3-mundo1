from math import sin, cos, tan, radians
x = float(input('Digite um ângulo: '))
sen = sin(radians(x))
cos = cos(radians(x))
tan = tan(radians(x))

print('Dado o ângulo de {}º, temos:\n'
      'sen = {:.2f}\n'
      'cos = {:.2f}\n'
      'tan = {:.2f}'.format(x, sen, cos, tan))

