print('O programa a seguir calcula o aluguel de um veículo.\n'
      'Informe o tempo em dias que ficou com o carro e os quilometros rodados.')

d = int(input('Quantos dias você ficou com o veículo?'))
km = float(input('Quantos quilometros rodados com o veículo?'))
vd = (d*60)
vkm = (km*0.15)
vt = vd+vkm

print('Você contratou o carro por {} dias e rodou {}km.\n '
      'O valor dos dias foi de R${} e dos km rodados {}km.\n '
      'O valor total a ser pago será de R${}.'.format(d, km, vd, vkm, vt))
