# Operadores in e not in;
# Strings são iteráveis;
# 0 1 2 3 4 
# H a r r y
# -6-5-4-3-2
# in = está entre
# not in = não está entre
nome = 'Harry'
#print(nome[2])
#print(nome[-3])

#print('Har' in nome)
#print('Zer' in nome)
#print(10 * '-')
#print('Har' not in nome)
#print('Zer' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} está em {nome}')
else:
  print(f'{encontrar} não está em {nome}')
