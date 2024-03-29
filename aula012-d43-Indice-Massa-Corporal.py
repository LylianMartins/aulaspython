'''Desenvolva um programa que leia o peso e a altura de uma pessoa, e calcule o seu IMC'''

peso = float(input('Digite o seu peso(kg): '))
alt = float(input('Digite a sua altura(m): '))
imc = peso / (alt ** 2)
if imc <= 18.5:
    print('Seu IMC é de {:.2f}, você está abaixo do Peso ideal.'.format(imc))
elif imc <= 25:
    print ('Seu IMC é de {:.2f}, você está no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f}, você está em sobrepeso.'.format((imc)))
elif imc <= 40:
    print('Seu IMC é de {:.2f}, você está obeso. '.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.2f}, você está em obesidade mórbida.'.format(imc))