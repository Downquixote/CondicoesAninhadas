# Condição Simples
nome = str(input('Qual seu nome? ')).strip().upper()
if nome == 'Lucas'.upper(): 
    print('Que nome lindo!')
print('Seja muito bem-vindo(a), {}!'.format(nome))

print('='*30)

# Condição Composta
idade = int(input('Qual a sua idade? '))
if idade < 18:
    print('Você ainda não é maior de idade!')
else:
    print('Você é maior de idade!')

print('='*30)

# Condição Aninhada
profi = str(input('Qual a sua formação acadêmica? ')).upper().strip()
if profi == 'Desenvolvedor de Software'.upper():
    print('Olá, Dev. {}!'.format(nome))

elif profi == 'Medicina'.upper():
    print('Olá, Dr(a) {}!'.format(nome))

elif profi == 'Direito'.upper():
    print('Olá, Dr(a) {}!'.format(nome))

elif profi == 'Psicologia'.upper():
    print('Olá, Dr(a) {}!'.format(nome))
    
elif profi == 'Gastronomia'.upper() or profi == 'Confeitaria'.upper():
    print('Olá, Chef {}!'.format(nome))
else: 
    print('Olá, pessoa!')

print('='*30)
