"""Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo."""

# Segmentos
print('Escreva abaixo o comprimento dos segmentos: ')
a = float(input('Comprimento de a: '))
b = float(input('Comprimento de b: '))
c = float(input('Comprimento de c: '))
segmentos = (a, b, c)

# Soma entre segmentos
somaa = (a + b)
somab = (b + c)
somac = (c + a)
soma = somaa, somab, somac

# Condição de Existência
if a < somab and b < somac and c < somaa:
    print('Os segmentos {} PODEM FORMAR um triângulo'.format(segmentos))
else:
    print('Os segmentos {} NÃO PODEM formar um triângulo'.format(segmentos))
