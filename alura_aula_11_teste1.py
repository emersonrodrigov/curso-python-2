


# A flag a adiciona o conteúdo no final do arquivo, enquanto a w sempre começa no início:
#
# a - acrescenta no final do arquivo
#
# w - sempre escreve no inicio do arquivo, conteúdo existente será apagado
#
# Você também pode imprimir a flag (mode) de um arquivo em uso:


arquivo = open('teste.txt', 'a')
arquivo.write('Python rocks \n')
arquivo.close()