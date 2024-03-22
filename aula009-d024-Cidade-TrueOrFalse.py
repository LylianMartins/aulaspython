#Crie um programa que leia o nome de uma cidade e diga se começa ou não com o nome Santo

city = str(input('Digite o nome de uma cidade: ')).strip()
print(city[:5].upper() == 'SANTO')