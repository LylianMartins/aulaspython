#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maisúsculas
# O nome com todas aletras minúsculas
# Quantas letras ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome


frase = str(input('Qual o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(frase.upper()))
print('Seu nome em minúsculas é {}'.format(frase.lower()))
print('O números de letras do seu nome é: {}'.format(len(frase) - frase.count (' ')))
print('Seu primeiro nome tem {} letras'.format(frase.find (' ')))
#ou
#separa = frase.spli()
#print('Seu primeiro nom é {} e ele tem {} letras'.format(separa{0}, len(separa{0})))