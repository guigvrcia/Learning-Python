hora_solicitada = input('Digite a hora atual: ') # Solicitando ao usuário que digite a hora atual.
hora_digitada = int(hora_solicitada) # Convertendo a hora digitada para um inteiro.

if hora_digitada >= 0 and hora_digitada <= 11:
  print(f'Bom dia! São {hora_digitada} horas.')
elif hora_digitada >= 12 and hora_digitada <= 17:
  print(f'Boa tarde! São {hora_digitada} horas.')
elif hora_digitada >= 18 and hora_digitada <= 23:
  print(f'Boa noite! São {hora_digitada} horas.')