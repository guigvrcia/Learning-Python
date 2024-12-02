# Operador lógico "and";
# "and" todas as condições precisam ser verdadeiras;
# Todas as condições precisam ser verdadeiras para que o bloco de código seja executado;

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if condição
if entrada == 'E' and senha_digitada == senha_permitida:
  print('Entrar')
else:
  print('Sair')

# Avalição de curto-circuito;
print(True and False and True)
print(True and 0 and False)
