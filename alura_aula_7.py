

##### Expressão regulares

### Objetivo melhorar as buscas utilizando expressoes regulares


import re


resultado = re.match('Py','Python')
print(resultado.group())


resultado = re.match('py','Python')

print(resultado)


##### Agrupando caracteres
# busca por minusculo e maiusculo
resultado = re.match('[pP]y','Python')
print('Pesquisando com P maiusculo %s' %(resultado.group()))

resultado = re.match('[pP]y','python')
print('Pesquisando com p minusculo %s' %(resultado.group()))



### qualquer letra de a - z seguida de y
resultado = re.match('[A-Za-z]y','Python')
print( 'qualquer letra de a - z seguida de y -> %s' % resultado.group())

## qualquer letra de a-z seguida de y percorrendo toda string
resultado = re.findall('([A-Za-z]y)','Python e jython')
print( 'qualquer letra de a - z seguida de y (findall) -> %s' % resultado)

## Findall com a palavra completa no retorno
resultado = re.findall('([A-Za-z]y[A-Za-z]+)','Python ou jython ou Py1Py')
print( 'Retorna a palavra complate que iniciar com letras seguida do y (findall) -> %s' % resultado)

# buscar qualquer caracter seguido de y
#  \w = qualquer caracter
#  \d = identifica apenas numero
#  \s = espaço em branco ou tabulacao
resultado = re.findall('(\wy\w+)','Python ou jython ou Py1Py')
print( 'qualquer caracter seguido de y utilizando \w -> %s' % resultado)

resultado = re.findall('(\wy\w+\d)','Python3 ou jython2 ou Py1Py')
print( 'qualquer caracter seguido de y utilizando \w -> %s' % resultado)

######## RAW STRING = String crua
# Exemplo r'[A-Z]+'

## Buscar todas as palavras que começam com a letra fF
resultados = re.findall(r'[fF]\w+','Nico Flavio Fabiana Romulo')


# imprime tudo que começa com as letras f ou F que tenha pelo menos 6 caracteres
resultados = re.findall(r'[fF]\w{6}','Nico Flavio Fabiana Romulo')
print('imprime tudo que começa com as letras f ou F que tenha pelo menos 6 caracteres %s' %(resultados))

# Buscar no início e fim da string
# ^ = procurar no inicio da string
# $ = procurar no final da string
# . = zero ou mais vezes
# .* = representa qualquer caracter 0 ou mais vezes!

#  descobri se a string começa com #(tralha)
resultado = re.match(r'^#.*', '#comentarios começam com tralha')
print('Começa com s %s'  % resultado.group())

# descobrir se uma string termina com .br

resultado = re.match(r'.*br$','http://alura.com.br')
print(resultado.group())


