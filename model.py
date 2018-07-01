# -*- coding: UTF-8 -*-
class Perfil(object): # new style declaracao da classe
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        # aula 8
        self.__curtida = 0

        # aula 9 - heranca
        # self.__tipo = tipo



    def imprimir(self):
      print("Nome : %s, Telefone: %s, Empresa %s, Curtidas %s" % (self.nome, self.telefone, self.empresa, self.__curtida))

    def curtir(self):
        ## __ deixa o campo privad, nao conseguindo acessa diretamente a propriedade curtida
        self.__curtida+=1

    def obter_curtidas(self):
        return self.__curtida

    def obter_creditos(self):
        if self.__tipo == 1:
            return self.__curtida * 10.0

    def obter_tipo(self):
        return self.__tipo


# Aula 10 -  Heranca
class Perfil_Vip(Perfil):
   'Classe padrão para perfis de usuários VIPs'

   def __init__(self, nome, telefone, empresa, apelido):
       super(Perfil_Vip, self).__init__(nome, telefone, empresa)
       self.apelido = apelido

   def obter_creditos(self):
       # obter curtidas esta na classe pai
      return super(Perfil_Vip, self).obter_curtidas() * 10.0



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


class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def calcular_imposto(self):
        imposto = self.saldo * 0.10
        return imposto


class ContaCorrente(Conta):
    def __init__(self, titular, saldo, bonus):
        super(ContaCorrente, self).__init__(titular, saldo)
        self.bonus =bonus

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20

