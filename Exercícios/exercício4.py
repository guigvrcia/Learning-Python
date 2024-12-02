"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
      Seu nome é {nome}
      Seu nome invertido é {nome invertido}
      Seu nome contém (ou não) espaços
      Seu nome tem {n} letras
      A primeira letra do seu nome é {letra}
      A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
      Nada foi digitado
"""

# Solicitando ao usuário que forneça seu nome;
nome = input('Digite o seu nome: ')

# Solcitando ao usuário que forneça sua idade;
idade = input('Digite a sua idade: ')

# Verificando se o nome e idade foram digitados;
if nome and idade: # Se ambos foram digitados;
  print(f'Nome: {nome}')
  print(f'Nome invertido: {nome[::-1]}') # Exibindo o nome invertido;

  if ' ' in nome:
    print(f'Seu nome contém espaços.') # Verifica se o nome contém espaços;

  print(f'Seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome é: {nome[0]}')
  print(f'A última letra do seu nome é: {nome[-1]}')
else:
  print(f'Desculpe, você deixou campos vazios.')