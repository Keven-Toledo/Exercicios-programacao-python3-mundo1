"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
sequencia = n1, n2, n3

print('=-'*20)

if n1 > n2 and n1 > n3:
    print('O número {} é o maior da sequência {}'.format(n1, sequencia))
    if n3 > n1:
        print('O número {} é o maior da sequência {}'.format(n3, sequencia))

else:
    passo2 = n2 > n3
    if passo2:
        print('O número {} é o maior da sequência {}'.format(n2, sequencia))
    else:
        print('O número {} é o maior da sequência {}'.format(n3, sequencia))

if n1 < n2 and n1 < n3:
    print('O número {} é o menor da sequência {}'.format(n1, sequencia))
    if n3 < n1:
        print('O número {} é o menor da sequência {}'.format(n3, sequencia))

else:
    passo3 = n2 < n3
    if passo3:
        print('O número {} é o menor da sequência {}'.format(n2, sequencia))
    else:
        print('O  número {} é o menor da sequência {}'.format(n3, sequencia))

print('=-'*20)
