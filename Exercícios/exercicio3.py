# Variáveis que irão receber os valores do usuário:
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# Confição para verificar qual é o maior valor digitado pelo usuário:

if primeiro_valor > segundo_valor:
  print(
    f'{primeiro_valor=} é maior ou igual '  
    f'ao {segundo_valor=}'
)
else:
  print(
    f'{segundo_valor=} é maior ' 
    f'ou igual ao {primeiro_valor=}'
    )