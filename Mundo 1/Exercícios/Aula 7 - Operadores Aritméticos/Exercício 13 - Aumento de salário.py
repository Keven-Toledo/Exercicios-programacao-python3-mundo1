titulo = 'Aumento de salário'
print('{:^120}'.format(titulo))

print('Esse programa tem a finalidade de calcular o aumento de salário.')
s = float(input('Qual é seu salário?'))
au = int(input('Qual o aumento (sem a %)?'))
au1 = (au+100)
auf = (au1/100)*s

print('Seu aumento foi de {}%. Portanto, seu salário passa de R${} para R${:.2f}.'.format(au, s, auf))
