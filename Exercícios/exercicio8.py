# Iterando strings com while:

nome = 'Harry Styles' # Iteráveis

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < tamanho_nome:
  letra = nome[indice]
  novo_nome += letra
  indice += 1
  
print(novo_nome)