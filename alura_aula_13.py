

# Tratamento de excecoes

# -*- coding: UTF-8 -*-

#erros.py

#Não podemos nos esquecer de importar o módulo models
from model import *
# try:
#         arquivo = open('perfis.csv','r')
#         valores = arquivo.readline().split(':') #deve ser virgula, para simular o problema
#         Perfil(*valores)
#         arquivo.close()
# except IOError as erro:
#         print('Deu IOError %s' % erro)
# except  TypeError as erro:
#         print('Deu TypeError %s' % erro)
# except (IOError, TypeError) as erro:
#         print('Deu Error %s' % erro)


# FINALLY

# arquivo = None #inicializar a variável arquivo
# try:
#         arquivo = open('perfis.csv','r')
#         valores = arquivo.readline().split(',')
#         Perfil(*valores)
# except (IOError,TypeError) as erro:
#         print('Deu Error %s' % erro)
# finally:
#         if(arquivo is not None):
#                 print('fechando arquivo')
#                 arquivo.close()

# Sintaxe with-as

arquivo = None
try:
        arquivo = open('perfiL.csv','r')
        valores = arquivo.readline().split(',')
        Perfil(*valores)
finally:
        if(arquivo is not None):
                print('fechando arquivo')
                arquivo.close()