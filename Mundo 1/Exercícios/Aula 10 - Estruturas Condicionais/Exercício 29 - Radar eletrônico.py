"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""

velocidade = float(input('Qual a velocidade atual do veículo: '))
a = velocidade-80
multa = 7.00*a
if velocidade > 80.0:
    print('ATENÇÃO! VOCÊ ULTRAPASSOU A VELOCIDADE DE 80KM/H PERMITIDA NA VIA')
    print("""Será aplicada uma multa no valor de R$7,00/km rodado acima da velocidade limite.
O valor total da multa é de R${:.2f}""".format(multa))

print('Tenha um bom dia e, dirija com segurança!')
