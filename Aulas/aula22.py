# Operador lógico 'or';
# 'or' uma das condições precisa ser verdadeira;

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if condição
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
  print('Entrar')
else:
  print('Sair')

# Avalição de curto-circuito;
senha = input('Senha: ') or 'Sem senha'
print(senha)

