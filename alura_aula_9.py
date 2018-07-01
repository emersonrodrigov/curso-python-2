# ENCAPSULAMENTO
from model import *


# // criando perfil
perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')

# print(perfil.curtida)
# perfil.curtida+=1;
perfil.curtir()
print('Somando 1 no perfil  %s' % (perfil.obter_curtidas()))

# perfil.curtida = 100;

# print('Adicionando 100 curtida no perfil %s' % (perfil.obter_curtidas()))


# criar o metodo na classe Perfil para somar curtidas
# perfil.curtida = 0

perfil.curtir()
print('Adicionando perfil atraves do metodo curtidas %s' % (perfil.obter_curtidas()))

perfil.curtir()
print('Adicionando perfil atraves do metodo curtidas %s' % (perfil.obter_curtidas()))

perfil.curtir()
print('Adicionando perfil atraves do metodo curtidas %s' % (perfil.obter_curtidas()))

perfil.curtir()
print('Adicionando perfil atraves do metodo curtidas %s' % (perfil.obter_curtidas()))


print(perfil.obter_curtidas())

# na classe perfil a propriedade curtida foi colocada com private
# nao deixando acessar direto

# def __init__(self, nome, telefone, empresa):
#     self.nome = nome
#     self.telefone = telefone
#     self.empresa = empresa
#     # aula 8
#     self.__curtida = 0

#  Adicionando uma nova propriedade na instancia de perfil
perfil.curtidas =1000


perfil.imprimir()