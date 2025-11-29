# in e not in
# string são iteráveis

# nome = 'Luís'

# print(nome[2])

# print('L' in nome) # True
# print('Z' in nome) # False

seu_nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in seu_nome:
    print(f'{encontrar} está em {seu_nome}')

else:
    print(f'{encontrar} não está em {seu_nome}')