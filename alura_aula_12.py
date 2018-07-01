from model import *



## Aula 12 - Metodos Estaticos

perfis = []

perfil = Perfil(nome='Ana Paula Gonçalves', telefone='21-34345432', empresa='Amigas Ltda')
perfis.append(perfil)


# arquivo = open('base_perfil.csv',  'r')
#
# for linha in arquivo:
#     valores = linha.split(',')
#     perfis.append(Perfil(*valores))
#     print(linha)
#
# arquivo.close()


# perfis = Perfil.gerar_perfis('base_perfil.csv')

perfis_vip = Perfil_Vip.gerar_perfis("base_perfil.csv")
print(type(perfis_vip[0]))
for linha in perfis_vip:
    linha.imprimir()