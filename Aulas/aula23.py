# Operador lógico "not";
# Usado para inverter expressões (valor booleano);
# not True = False
# not False = True

senha = input('Senha: ')

print(not True) # False
print(not False) # True
if not senha:
  print('Você não digitou nada.')