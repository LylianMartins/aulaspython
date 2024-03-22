#Crie um programa que leia o nome da pessoa e diga se ela tem "SILVA"


name = str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in name.upper()))