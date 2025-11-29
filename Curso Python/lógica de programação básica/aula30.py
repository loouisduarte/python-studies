"""
CONSTANTE = 'variáveis' que não vão mudar
muitas condições no mesmo if (ruim)
"""

velocidade = 200 # velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

# é comum no python utilizar palavras em letras maiusculas para dizer que aquela constante não muda


# if velocidade > RADAR_1:
#     print(f'seu veículo estava a {velocidade}km/h em um radar de {RADAR_1}')


# if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
#     print('carro multado')

vel_car_pass_radar = velocidade > RADAR_1

carro_sera_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1

if vel_car_pass_radar:
    print('acima da velocidade permitida')

if carro_sera_multado:
    print('multado')