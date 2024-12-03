primeiro_nome = input('Digite o seu primeiro nome: ') # Solicita ao usuário que digite seu primeiro nome.
menor_que_4  = len(primeiro_nome) <= 4 # Verifica se o nome digitado possui menos de 4 caracteres.
entre_5_e_6 = len(primeiro_nome) > 4 and len(primeiro_nome) < 7 # Verifica se o nome possui entre 5 e 6 caracteres.

if menor_que_4: # Verifica se o nome digitado possui menos de 4 caracteres.
  print('Seu nome é curto.')
elif entre_5_e_6: # Verifica se o nome possui entre 5 e 6 caracteres.
  print('Seu nome é normal.')
else:
  print('Seu nome é muito grande.') # Somente se o nome possuir mais de 6 caracteres.