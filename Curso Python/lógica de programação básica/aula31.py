"""
Flag (Bandeira) - marcar um local
None = não valor
is e is not = é ou não é
id = identidade
"""

# v1 = 'a'
# v2 = 'a'
# v3 = 'b'

# print(id(v1))
# print(id(v2))
# print(id(v3))

# condicao = False
# if condicao:
#     print('Faça algo')
# else:
#     print('Não faça algo')


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('não faça algo')

if passou_no_if is None:
    print('não passou no if')

if passou_no_if is not None:
    print('Passou no if')