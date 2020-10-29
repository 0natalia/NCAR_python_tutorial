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
# DEBUG
# print(data)

# *********** PARTE 3: Abrir com a função with
# Lê tudo de uma vez com menos linhas e ainda fecha o dado após a leitura
# Bom para quem esquece de fechar o dado
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     data = datafile.read()
# DEBUG
# print(data)

# *********** PARTE 4: Descobrir qual o tipo de dado
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     data = datafile.read()

# *********** PARTE 5: Initialize data variable with dictionary
# data = []
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     #
#     for _ in range(3):  # same as loop in a list [0, 1, 2]
#         # print(_). # Just to see what is the _, which is the same as i..
#         datafile.readline()  # read one line three times
#     #
#     for line in datafile:  # Read and parse all the file but the header
#         # print(line)
#         datum = line.split()  # Faz uma lista de "listas"
#         data.append(datum)  # Adiciona uma lista ao final do dicionário

# # DEBUG
# for datum in data:
#     print(datum)

# *********** PARTE 6: Usar os índices para localizar os dados
# data = []
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     #
#     for line in datafile:  # Read and parse all the file but the header
#         # print(line)
#         datum = line.split()  # Faz uma lista de "listas"
#         data.append(datum)  # Adiciona uma lista ao final do dicionário

# # DEBUG
# print(data[0])  # first index
# print(data[-1])  # negative index works for reverse indices in list
# print(data[0:10])  # start and stop at these indices

# # A better way to look at the output:
# for datum in data[0:10]:
#     print(datum)  # imprime cada linha de uma vez

# # If you don't specify your start, it will always initialize in index 0:
# for datum in data[:10]:
#     print(datum)

# # You can also set the step in your range:
# for datum in data[0:10:2]:
#     print(datum)  # imprime a cada 2 linhas

# # Print the fifth element of the ninith row in data:
# print(data[8][4])

# # Since we're dealing with strings, we can select which character we want.
# # For instance, the first charactere of the fifth element in the ninith row:
# print(data[8][4][0])

# # Print the five first indices of row nine
# print(data[0][:5])  # header
# print(data[8][:5])

# # Print every index in row 8, but with a step of two
# print(data[0][::2])  # header
# print(data[8][::2])

# *********** PARTE 7: É dificil saber qual coluna corresponde à que variável.
# É mais interessante abrir o dado como um dicionário, ao invés de lista
# Ao invés de buscar por índice na row, podemos buscar por variável (tempo, T)
# Ao invés de colchetes, abrimos chaves. Ao invés de lista, dicionário...
# Initialize my data variable
data = {'date': [], 'time': [], 'tempout': []}
filename = "wxobs20170821.txt"
with open(filename, 'r') as datafile:
    #
    for _ in range(3):  # Read the first three lines (header)
        datafile.readline()  # Se não ler as primeiras linhas vai dar erro --?
    #
    # Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(split_line[2])

# DEBUG
print(data['time'])
