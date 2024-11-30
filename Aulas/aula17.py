# Controle do fluxo do interpretador em condicionais;

condicao = False
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1: # Se a condição for verdadeira, o código abaixo será executado
    print('Este é o código para condição 1')
elif condicao2:
   print('Este é o código para condição 2')
elif condicao3:
   print('Este é o código para condição 3')
elif condicao4:
   print('Este é o código para condição 4') 
else: # Se a condição for falsa, o código abaixo será executado
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
  print('Outro if')

print('Fora do if')