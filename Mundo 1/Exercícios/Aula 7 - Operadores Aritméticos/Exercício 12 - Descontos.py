titulo = 'Descontos'
print('{:^120}'.format(titulo))

print('Esse programa tem o objetivo de calcular descontos sobre um produto.')
print('Informe o desconto e o valor nas linhas abaixo:')

p = float(input('Valor da mercadoria:'))
d = float(input('Desconto (sem %):'))
dc = (100-d)
df = (dc/100)*p

print('O desconto inserido foi de {:.0f}%. Sendo assim, '
      'o valor do produto final será R${:.2f}'.format(d, df))
print('='*120)
