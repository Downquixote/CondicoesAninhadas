# A configuração Nacional de Notação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 ANOS: MIRIM
# - Até 14 ANOS: INFANTIL
# - Até 19 ANOS: JUNIOR 
# - Até 20 ANOS: SÊNIOR
# - Acima: MASTER 

from datetime import date

idade = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year - idade

if ano <= 9:
    print('Atleta: MIRIM!')
elif ano <= 14:
    print('Atleta: INFANTIL!')
elif ano <= 19:
    print('Atleta: JUNIOR!')
elif ano <= 20: 
    print('Atleta: SÊNIOR!')
else:
    print('Atleta: MASTER!')