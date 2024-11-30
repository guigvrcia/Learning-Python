# Introdução a formatação de strings: f-strings;

# Calculo de IMC;

nome = 'Harry Styles' # Nome do usuário;
altura = 1.83 # Altura do usuário;
peso = 70 # Peso do usuário;
imc = peso / (altura ** 2) # Placeholder para fazer o cálculo de IMC;

# Cálculo do IMC;

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)