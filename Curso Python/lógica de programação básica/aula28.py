# exercício

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

# exercício

nome = input('digite o seu nome: ')
idade = input('digite a sua idade: ')

if nome == '' or idade == '':
    print('Desculpe, você deixou campos vazios.')

else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('seu nome contém espaço')
    if ' ' not in nome:
        print('seu nome não contém espaço')

    print(f'Seu nome tem ', len(nome), 'letras')
    print(f'a primeira letra do seu nome é', nome[0])
    # print(f'a última letra do seu nome é', nome[:-2:-1])
    print(f'a última letra do seu nome é', nome[-1])

    frase = input('digite qualquer frase: ')
