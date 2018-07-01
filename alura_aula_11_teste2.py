


# O código é praticamente idêntico aos exemplos anteriores. A única coisa que muda é o flag.
# Agora estamos usando rb para leitura binária e wb para escrita binária.



#arquivo copia.py
logo = open('files/python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('files/python-logo2.png', 'wb')
logo2.write(data)
logo2.close()