from time import sleep
from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Aposentadoria'] = pessoa['Contratação'] - nasc + 35
    pessoa['Salário'] = float(input('Salário: R$'))
    print()
else:
    print()
print('=-' * 40)
for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v}')
    sleep(1)
# - nome tem o valor Juvenal
# - idade tem o valor 28
# - CTPS tem o valor x.
