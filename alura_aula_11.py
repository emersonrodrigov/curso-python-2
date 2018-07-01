from model import *

# AULA - 11 - LEITURA E ESCRITA DE ARQUIVO

# # para leitura apenas, r – read
arquivo = open('perfil.csv','r')

linha = arquivo.readline()
print(linha)
#
# #para leitura e escrita (w+)
# arquivo = open('perfil.csv','w+')


# Imprimir linhas do arquivo
for linha in arquivo:
    print(linha)


arquivo_novo = open('arquivo_novo.csv','w')
arquivo_novo.write('PEDRO, 23-45631234, Gomes e amigos \n')
arquivo_novo.write('EMERSON Gomes, 23-45631234, Gomes e amigos \n')
arquivo_novo.write('RODRIGO Gomes, 23-45631234, Gomes e amigos \n')

arquivo_novo.close()

arquivo_lido = open('arquivo_novo.csv','r')

# Imprimir linhas do arquivo
for linha in arquivo_lido:
    print(linha)


arquivo = open('teste.txt', 'a')
arquivo.write('Python rocks \n')
arquivo.close()



