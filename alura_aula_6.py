
# indicado para o processador python que utilizara UTF-8
#  -*- coding: UTF-8 -*-


# frase = 'Python'
# contador = 0
# while(contador < len(frase)):
#     print(frase[contador])
#     contador+=1
# print('FIM')

import re


def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)

def listar(nomes):
    print('Lista nomes')
    for nome in nomes:
        print(nome)

def remover(nomes):
    print('Digita o nome que deseja remover ? ')
    nome_digitado = input()
    nomes.remove(nome_digitado)

def alterar(nomes):
    print('Digita o nome que deseja alterar? ')
    nome_atual = input()

    posicao = nomes.index(nome_atual)

    # if (nome_atual in nomes):
    #     posicao = nomes.index(nome_a_alterar)


    if(posicao >= 0):
        print('Digita o novo nome: ')
        nome_novo = input()
        nomes[posicao] = nome_novo
    else:
        print('nome digitado não encontrado')


def procurar(nomes):
    print('Digite nome a procurar:')
    nome_a_procurar = input()

    if(nome_a_procurar in nomes):
        print('Nome %s  encontrado !!!!!' % nome_a_procurar)
    else:
        print('Nome %s não Ensontrado !!!!!' % nome_a_procurar)




#### Aula 7 - exercicio

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = input()
    #concatene os nomes
    nomes_concatenados = ' '.join(nomes)

    #busque pela expressão regular no string
    resultados = re.findall(regex, nomes_concatenados)

    #imprime o resultado
    print(resultados)





def menu():

    nomes = []

    escolha = ''
    while(escolha != '0'):
        print('Digite: '
              '1 - para cadastrar, '
              '2 - para Lista, '
              '3 -  para deletar, '
              '4 -  para alterar,'
              '5 -  para procurar na lista, '
              '6 -  para procurar com regex, '
              '0 para terminar')
        escolha = input()

        if( escolha == '1') :
            cadastrar(nomes)

        if( escolha == '2') :
            listar(nomes)

        if (escolha == '3') :
            remover(nomes)

        if (escolha == '4') :
            alterar(nomes)

        if (escolha == '5') :
            procurar(nomes)

        if (escolha == '6') :
            procurar_regex(nomes)

menu()