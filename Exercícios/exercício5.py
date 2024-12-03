numero_solicitado_str = input('Digite um número inteiro: ') # Solicitando ao usuário que digite um número inteiro:
verificaInteiro = numero_solicitado_str.isdigit() # Verifica se o número digitado é um inteiro.

# Verificando se o número digitado é par ou impar:
try:
  numero_digitado = int(numero_solicitado_str) # Convertando o número digitado para um inteiro.
  verifica_par_impar = numero_digitado % 2 == 0 # Verifica se o número digitado é par.

  if verifica_par_impar: # Verifica par ou impar.
    print(f'O número {numero_digitado} é par.')
  else:
    print(f'O número {numero_digitado} é impar.')
except:
    if not verificaInteiro: # Verifica se o número digitado pelo usuário é inteiro.
      print(f'O número digitado {numero_solicitado_str} não é um inteiro.')