# INTRODUÇÃO  FUNCOES
# len
# Criando funcao

from biblioteca import *

convite = 'Flavio Henrique Almeira'

parte1 = convite[0:4]
parte2 = convite[11:15]



posicao_final = len(convite)
posicao_inicial = posicao_final - 4

parte1 = convite[0:4]
parte2 = convite[posicao_inicial:posicao_final]

print ('parte 1 %s e parte 2 %s' % (parte1,parte2))

print('Obter tamanho da string len() %s' % len(convite))


## CHAMANDO FUNÇÃO EM OUTRO ARQUIVO
gera_nome_convite('Emerson Rodrigo Vital da Silva')
envia_convite(gera_nome_convite('Emerson Rodrigo Vital da Silva'))

gera_nome_convite('Flavio Almeida')
envia_convite(gera_nome_convite('Flavio Almeida'))

gera_nome_convite('Romulo Henrique')
envia_convite(gera_nome_convite('Romulo Henrique') )


## CHAMANDO FUNCAO QUE PROCESSA TUDO DO CONVITE
processa_convite('Emerson Rodrigo Vital da Silva')
processa_convite('Flavio Almeida')
processa_convite('Romulo Henrique')



