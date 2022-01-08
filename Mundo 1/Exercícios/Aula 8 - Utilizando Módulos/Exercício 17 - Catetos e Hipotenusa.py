"""CA = float(input('Digite o valor do Cateto Adjacente: '))
CO = float(input('Digite o valor do Cateto Oposto: '))
CC = (CA**2)+(CO**2)
HIP = CC**(1/2)

print('Dados:\n '
      'CA = {}\n '
      'CO = {}\n '
      'Soma dos Catetos = {}\n '
      'Hipotenusa = {:.2f}'.format(CA, CO, CC, HIP))"""

"""from math import sqrt, pow
CA = float(input('Digite o valor do Cateto Adjacente: '))
CO = float(input('Digite o valor do Cateto Oposto: '))
hip = sqrt(pow(CA, 2)+pow(CO, 2))
print('Dados:\n '
      'CA = {}\n '
      'CO = {}\n '
      'Hipotenusa = {:.2f}'.format(CA, CO, hip))"""

from math import hypot

CA = float(input('Digite o valor do Cateto Adjacente: '))
CO = float(input('Digite o valor do Cateto Oposto: '))
HI = hypot(CA, CO)
print('Dados:\n '
      'CA = {}\n '
      'CO = {}\n '
      'Hipotenusa = {:.2f}'.format(CA, CO, HI))
