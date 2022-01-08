# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ').strip().split())
nome2 = nome.title()
print('Seu nome possui "Silva"? ', "Silva" in nome2)
