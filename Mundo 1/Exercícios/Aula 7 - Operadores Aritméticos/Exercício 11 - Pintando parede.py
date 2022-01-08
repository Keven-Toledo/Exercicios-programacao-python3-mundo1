titulo = 'Pintando uma parede'
print('{:^120}'.format(titulo))

print('O objetivo desse programa é calcular quantos litros de tinta serão necessários para pintar sua parede.')
print('Abaixo informe o comprimento e a altura de sua parede')
b = float(input('Comprimento em metros:'))
h = float(input('Altura em metros:'))
A = b*h
tinta = A/2
print('Sua parede possui uma área de {:.2f}m². Por isso, use {:.2f} litros de tinta'.format(A, tinta))

print('='*120)
