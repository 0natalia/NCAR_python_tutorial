# Reading data file
# Python introductory class by Julia Kent

# *********** PARTE 1: abrir dado com readline
# Bom para ler algumas linhas do começo e ver se está tudo ok
# Teria que digirar muitas vezes p ler o arquivo todo
# filename = 'wxobs20170821.txt'
# datafile = open(filename, 'r')
# # # a cada chamada vai lendo as linhas em sequencia
# # print(datafile.readline())
# # print(datafile.readline())
# # print(datafile.readline())
# # print(datafile.readline())

# *********** PARTE 2: Abrir read
# Mais rápido para ler todo o arquivo de uma vez
# Se tiver muitas linhas, vai ter que subir muito p ler .head()
# filename = 'wxobs20170821.txt'
# datafile = open(filename, 'r')
# data = datafile.read()
# datafile.close()
# print(data)

# *********** PARTE 3: Abrir com a função with
# Lê tudo de uma vez com menos linhas e ainda fecha o dado após a leitura
# Bom para quem esquece de fechar o dado
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     data = datafile.read()

# print(data)

# *********** PARTE 4: Descobrir qual o tipo de dado
filename = 'wxobs20170821.txt'
with open(filename, 'r') as datafile:
    data = datafile.read()
