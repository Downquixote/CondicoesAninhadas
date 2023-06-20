# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC está em {:.1f}.'.format(imc))
    print('Abaixo do peso!')
elif imc < 25: 
    print('Seu IMC está em {:.1f}.'.format(imc))
    print('Peso ideal!')
elif imc < 30: 
    print('Seu IMC está em {:.1f}.'.format(imc))
    print('Sobrepeso')
elif imc < 40: 
    print('Seu IMC está em {:.1f}.'.format(imc))
    print('Obesidade!')
elif imc > 40:
    print('Seu IMC está em {:.1f}'.format(imc))
    print('Obesidade mórbida!')
else: 
    print('Ops... tente novamente.')