'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('-='*15)
print('LISTAGEM DE PREÇOS')
print('-='*15)
produtos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.90,
    'Tansferidor', 4.20,
    'Compasso', 9.99,
    'Mochila',120.32,
    'Canetas', 22.30,
    'Livro', 34.90)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<18}', end='')
    else:
        print(f'R$ {produtos[item]:>7.2f}')
print('-='*15)