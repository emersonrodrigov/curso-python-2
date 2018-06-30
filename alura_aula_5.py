import sys
from datetime import datetime
from datetime import date
from biblioteca import *

# Capturando o input de usuário função python 2 raw_input() python 3 input()

ano = input('Digite ano de nascimento ')
print(2015 - int(ano))

nomes = []
def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)

cadastrar(nomes)
cadastrar(nomes)
cadastrar(nomes)
cadastrar(nomes)

print('Nomes adicionados %s' %(nomes))

remover_item_lista(nomes)


print('digite seu ano de nascimento')
ano_como_string = input()

idade = date.today().year - int(ano_como_string)
print('Sua idade é %s' % (idade))


hoje = date.today()
hoje.day
hoje.month
hoje.year



