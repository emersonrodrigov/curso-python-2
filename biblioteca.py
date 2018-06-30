


def processa_convite(convite):
    nome_formatado = gera_nome_convite(convite)
    envia_convite(nome_formatado)

# Funcao reutilizada na aula 4
def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    # print("%s %s" % (parte1, parte2))
    return parte1 + ' ' + parte2


# Funcao reutilizada na aula 4
def envia_convite(nome_formatado):
    print( "Enviando convite para %s" % (nome_formatado))


def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)



def remover_item_lista(nomes):
    print('Qual nome gostaria de remover ?')
    print(nomes)
    nome = input()
    nomes.remove(nome)

    print('Removido com sucesso, lista atual %s' % (nomes))


