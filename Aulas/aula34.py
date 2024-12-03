# Reptições (while):

condicao = True

while condicao:
  nome = input('Digite o seu nome: ')
  print(f'Olá, {nome}')

  if nome == 'sair':
    break

print('Fim do programa.')