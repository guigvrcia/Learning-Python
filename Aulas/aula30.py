"""
Variáveis, constantes e complexidade de código:

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
      < - Contagem de complexidade (ruim)
"""
velocidade = 70 # velocidade atual do carro
local_carro = 100 # local que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima no radar
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = vel_radar1 and carro_passou_radar1

if vel_radar1:
      print('Velocidade do carro passou do radar 1')

if carro_passou_radar1:
      print('Carro passou no radar 1')

if carro_passou_radar1 and  vel_radar1:
      print('Carro multado em radar 1')