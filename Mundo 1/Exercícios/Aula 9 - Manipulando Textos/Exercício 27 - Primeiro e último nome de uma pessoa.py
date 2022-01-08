"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite seu nome completo: ')).strip().title().split()
nas = str(input('Digite sua data de nascimento: ')).strip()
dia = nas[0:2]
mes = nas[2:4]
ano = nas[4:]
print('Nascimento: {}/{}/{}'.format(dia, mes, ano))
print('Nome: {}'.format(nome[0]))
print('Sobrenome: {}'.format(nome[-1]))
