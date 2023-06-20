# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais.
# - iSÓCELES: dois lados iguais.
# - ESCALENO: todos os lados diferentes
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('As medidas informadas PODEM formar um triângulo!')
    if a == b and b == c:
        print('As medidas formam um Triângulo EQUILÁTERO!')
    elif a == b and b != c or a != b and b == c or a == c and b != a:
        print('As medidas formam um Triângulo ISÓCELES!')
    elif a != b and b != c:
        print('As medidas formam um triângulo ESCALENO!')
else:
    print('As medidas informadas NÃO PODEM formar um triângulo!')
