'''Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram de 1 até 500'''

soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
            cont = cont +1 # soma += c
            soma = soma + c # soma += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
print('FIM')




