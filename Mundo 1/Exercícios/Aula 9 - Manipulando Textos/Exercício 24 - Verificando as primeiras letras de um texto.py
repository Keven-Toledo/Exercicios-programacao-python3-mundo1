# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = input('Em qual cidade você mora?')
divido = cidade.title().strip().split()
pp = divido[0]
print('Santo' in pp)
