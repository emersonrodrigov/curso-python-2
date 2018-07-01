# -*- coding: UTF-8 -*-
from model import *


print('Tratamento Simples')
try:
    [1,2] + (3,4)
except TypeError as erro:
    print('Deu IOError %s \n' %( erro))

# Tratamento simples
print('Tratamento Simples ')
try:
        open('nao_existe.txt','r')
        print('O arquivo foi aberto')
        arquivo.close()
except IOError as erro:
        print('Deu IOError %s \n ' % (erro))


print('Tratamento 2 Tipos de excecao ')
try:
        arquivo = open('perfil.csv','r')
        valores = arquivo.readline().split(':') #deve ser virgula, para simular o problema
        Perfil(*valores)
        arquivo.close()
except IOError as erro:
        print('Deu IOError %s \n' % erro)
except  TypeError as erro:
        print('Deu TypeError %s \n' % erro)


print('Tratamento 2 Tipos de excecao no mesmo bloco except ')
try:
        arquivo = open('perfil.csv','r')
        valores = arquivo.readline().split(':') #deve ser virgula, para simular o problema
        Perfil(*valores)
        arquivo.close()
except (IOError, TypeError) as erro:
        print('Deu Error %s \n' % erro)


print('Tratamento de excecao + bloco finally para fechar arquivo')
arquivo = None #inicializar a variável arquivo
try:
        arquivo = open('perfil.csv','r')
        valores = arquivo.readline().split(':')
        Perfil(*valores)
except (IOError,TypeError) as erro:
        print('Deu Error %s' % erro)
finally:
        if(arquivo is not None):
                print('Finally - fechando arquivo ')
                arquivo.close()



print('Tratamento de excecao - sem o Blobo except')
print('existe uma atalho para a abertura de arquivos')
try:
    with open("perfil.csv") as arquivo:
        for linha in arquivo:
            print(linha)
except (IOError,TypeError) as erro:
        print('Deu Error %s \n' % erro)


print('EXcecoes tratadas no GeraPerfil')
try:
    perfil = Perfil.gerar_perfis('perfil.csv')
except ValueError as erro:
        print('Deu Error %s \n' % erro)
except Argumento_Invalido_Error as erro:
        print('Deu Erro %s \n' % erro)


print('Validar Tamano das entrdas')

try:
    perfil = Perfil(nome='em', telefone='1000', empresa='ab')
except Argumento_Invalido_Error as erro:
    print('Deu Erro %s \n' % erro)