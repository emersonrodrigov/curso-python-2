

# TRABALHANDO COM LISTA

#declarando lista
convites = ['Flavio Almeida', 'Nico Steppat', 'Romulo Henrique']
print( 'Imprimir lista %s' % (convites))

# get item lista

print('Pegando item na posição 1 convites[0] %s' %(convites[0]))
print('Pegando item na posição 2 convites[1] %s' %(convites[1]))
print('Pegando item na posição 2 convites[2] %s' %(convites[2]))

print('Pegando itens da lista com slice [0:2] %s' %(convites[0:2]))

print('Pegando itens da lista apartir posicao [1:] %s' %(convites[1:]))


## Adicionando elemento na lista
convites.append(10)

print('Imprime lista com item adicionado (10) Lista -> %s' % (convites))



# Removendo elemento na lista
print('Lista antes de remover %s' % (convites))
print('Removendo item 10')
convites.remove(10);
print('Lista depois de remover %s' % (convites))