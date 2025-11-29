'''
try/except
'''

numero_str = input('Vou dobrar o numero que digitar: ')

try:
    numero_float = float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um número')