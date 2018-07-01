# heranca de orientacao a objeto

from model import *

# perfis VIP's possuem um benefício especial que perfis padrões não têm: para cada curtida,
# eles ganham R$ 10,00 em crédito em compras virtuais. Já temos a classe Perfil criada, vamos
# implementar essa lógica através do método obter_creditos:


perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')
perfil.curtir()
perfil.curtir()

print(perfil.obter_curtidas())

padrao = Perfil('Nico Steppat', 'não informado', 'Caelum') # Perfil nao possui apelido
vip = Perfil_Vip('Flávio Almeida', 'não informado', 'Caelum', 'Apelido') ## Perfil VIP possui um apelido

# // padrao
# Só soma no obter credito se for perfil VIP (1)

padrao.curtir()
# print('obter credito pefil padrao(nao fazer calculo)) %s' % padrao.obter_creditos())

vip.curtir()
vip.curtir()
vip.curtir()
print('obter credito pefil vip(fazer calculo)) %s' % vip.obter_creditos())
vip.obter_creditos()

vip = Perfil_Vip('Flávio Almeida', 'não informado', 'Caelum', 'Almeida')
vip.curtir()
vip.curtir()
vip.obter_creditos()


#### Exercicio

conta_corrente = ContaCorrente('Leonardo', 2000,50)
print('Exercicio conta corrento (conta_corrente.calcular_imposto()) %s' % (conta_corrente.calcular_imposto()) )