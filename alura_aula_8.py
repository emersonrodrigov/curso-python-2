from model import *

####  ORIENTÇÃO A OBJETOS E O CONCEITO DE CLASSE  ###

#ORIENTAÇÃO OBJETO PARA RESOLVER O PROBLEMA ABAIXO

perfil1_nome = 'Flávio Almeida'
perfil1_telefone = 'não informado'
perfil1_empresa = 'Caelum'


# VAMOS CRIAR UM DICTIONARY - problema continua !!!!!!!!

perfil = {'nome' : 'Flávio Almeida' , 'telefone' : 'não informado' , 'empresa': 'Caelum'}
print(perfil['nome'])

perfil2 = {'nome' : 'Nico Steppat' , 'telefone' : 'segredo' , 'empresa': 'Caelum'}
print(perfil2['nome'])


# Instaciar uma classe

perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')

perfil1 = Perfil('Flávio Almeida', 'não informado', 'Caelum')
perfil1.imprimir()

perfil2 = Perfil('Nico Steppat', 'segredo', 'Caelum')
perfil2.imprimir()


perfil = Perfil(telefone='não informa2222do',empresa='Caelum',  nome='Fulaninho Ciclano')
perfil.imprimir()

print(type(perfil))

print(perfil.__class__)


outro = perfil2
print(outro.nome)


d = Data('01','02','1987')
d.imprimir()

p = Pessoa('Emerson ', 80, 1.70)
p.imprimir()


