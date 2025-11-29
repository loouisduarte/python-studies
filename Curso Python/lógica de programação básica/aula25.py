"""
interpolação de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""

nome = 'Luís'
preco = 1000.9580329

variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('o hexadecimal de %d é %04x' % (15, 15)) 