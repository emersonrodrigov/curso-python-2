# -*- coding: UTF-8 -*-
class Perfil():
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
      print("Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa))


class Data(object):
    'classe imprime data'
    def __init__(self, dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print('%s/%s/%s' %(self.dia,self.mes,self.ano))


class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimir(self):
        imc = self.peso / (self.altura **2)
        print ('O IMC de %s é: %s ' %(self.nome, imc))

