# Tuples e Dictionary


tipos_convite = ['vip', 'normal', 'meia', 'cortesia']

tipos_convite.append('Penetra')

print(tipos_convite)


# Tuples é parecido com o ENUM no java
tipos_convite = ('vip', 'normal', 'meia', 'cortesia')
#print('Tuples criada %s' % (tipos_convite))

# convertento lista para Tuple
Estado = ('RJ','SP') + tuple(['MG','ES'])

# print('Convertendo lista para tuple tuple([MG,ES]) %s' % tuple(['MG','ES']))


# Tuples não é possive adicionar apos criada
# tipos_convite.append('Chocalho')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'

# Dicionario
convite_com_valor = {'vip' : 60 , 'normal' : 40 , 'meia': 30 , 'cortesia':0}
print("Imprimir dicionatio %s " % (convite_com_valor))
print('Imprimir keys do dicionarios %s' % (convite_com_valor.keys()))
print('Imprimir value do dicionarios %s' % (convite_com_valor.values()))


#  Funções MAX e MIM

print('Maior numero de uma lista max %s' % max([10, 5, 7]))

print('Maior numero de uma lista min %s' % min((10, 3, 9)))

nomes = ['Leonardo', 'Flávio', 'Rômulo', 'Arnaldo', 'Zebra']
print('Ordenar lista [Leonardo, Flávio, Rômulo, Arnaldo, Zebra] Ordenado -> %s ' % sorted(nomes))


