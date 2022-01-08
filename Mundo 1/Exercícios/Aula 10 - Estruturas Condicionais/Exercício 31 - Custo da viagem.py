"""Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km
e R$0,45 parta viagens mais longas."""

# Condição Composta a minha
viagem = float(input('Qual a distância da sua viagem em km? '))
passagem1 = 0.50 * viagem
passagem2 = 0.45 * viagem

if viagem > 200:
    print("""Sua viagem será de {}Km. 
O valor cobrado para essa viagem será de R${:.2f}""".format(viagem, passagem2))
else:
    print("""Sua viagem será de {}Km. 
O valor cobrado para essa viagem será de R${:.2f}""".format(viagem, passagem1))

# Condição Composta do Professor
'''distancia = float(input('Qual a distância da sua viagem: '))
print('Você está prestes a iniciar uma viagem de {}Km'.format(distancia))
if distancia > 200:
    preço = distancia*0.45
else:
    preço = distancia*0.50
print('O valor da sua viagem será de R${:.2f}'.format(preço))'''

# Condição Composta Simplificada
'''distancia = float(input('Qual a distância da sua viagem: '))
print('Você está prestes a iniciar uma viagem de {}Km'.format(distancia))
preço = distancia*0.45 if distancia > 200 else distancia*0.50
print('O valor da sua viagem será de R${:.2f}'.format(preço))'''
