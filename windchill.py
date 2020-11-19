# Reading data file
# Python introductory class by Julia Kent

# *********** PARTE 13: Comparar o valor de wind chill calculado com o que
# já veio no dado (se olharmos no header, veremos que esse dado vem na
# coluna 13 -- indice 12)

columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'wchill': 12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'wchill': float}

data = {}
for column in columns:
    data[column] = []

# Read and parse the data file
filename = "wxobs20170821.txt"
with open(filename, 'r') as datafile:

    # Read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    # Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            # data['float'] ---> str
            # tenta achar os dados do tipo float, mas se não achar, lê como str
            value = t(split_line[i])
            data[column].append(value)


# Definimos uma função, a qual o nome explicita o que faz e entre
# () quais argumentos ela irá usar para os cálculos
def compute_windchill(t, v):

    a, b, c, d = 35.74, 0.6215, 35.75, 0.4275

    v16 = v ** 0.16

    wci = a + (b * t) - (c * v16) + (d * t * v16)

    # Nenhuma outra variável definida dentro da função fica disponível para
    # o resto do código (ex. se chamar a, b, c, d e v16 fora fora da função
    # não vai existir). Apenas a variável de retorno pode ser usada depois
    return wci


# # DEBUG: Running the function to comput wci
# # Vamos rodar nossa função usando zip.
# # Zip pega os elementos de interesse da matriz e ignora os outros.
# Aqui, 5 está fora da matriz, então é ignorado
# for i, j in zip([1, 2], [3, 4, 5]):
#     print(i, j)
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

# Comparar os valores de WChill calculados e dos dados
# for wc_data, wc_comp in zip(data['wchill'], windchill):
#     print(f'{wc_data: .5f} {wc_comp: .5f} {wc_data - wc_comp: .5f}')

# Reescrevendo os ultimos comandos para melhorar a aprsentação
# Vamos incluir prints antes do loop como header para auxiliar na visualização
print(' DATE   TIME     WC_ORIG    WC_COMP    WC_DIFF')
print('------- ------  ---------  ---------  ----------')
# Colocamos as linhas como marcações para cada output

zip_data = zip(data['date'], data['time'], data['wchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time: >6} {wc_orig: 9.6f} {wc_comp:9.6f}  {wc_diff:10.6f}')

# # ***********# # ***********# # ***********# # ***********# # ***********


# # *********** PARTE 12: Escrevendo nossa função, que le os dados de vento
# columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}

# # Data types for each column (only if non-string)
# types = {'tempout': float, 'windspeed': float}

# data = {}
# for column in columns:
#     data[column] = []

# # Read and parse the data file
# filename = "wxobs20170821.txt"
# with open(filename, 'r') as datafile:

#     # Read the first three lines (header)
#     for _ in range(3):
#         datafile.readline()

#     # Read and parse the rest of the file
#     for line in datafile:
#         split_line = line.split()
#         for column in columns:
#             i = columns[column]
#             t = types.get(column, str)
#             value = t(split_line[i])
#             data[column].append(value)

# # Definimos uma função, a qual o nome explicita o que faz e entre
# # () quais argumentos ela irá usar para os cálculos
# def compute_windchill(t, v):

#     a = 35.74
#     b = 0.6215
#     c = 35.75
#     d = 0.4275

#     v16 = v ** 0.16

#     wci = a + (b * t) - (c * v16) + (d * t * v16)

#     # Nenhuma outra variável definida dentro da função fica disponível para
#     # o resto do código (ex. se chamar a, b, c, d e v16 fora fora da função
#     # não vai existir). Apenas a variável de retorno pode ser usada depois
#     return wci


# # # DEBUG: Running the function to comput wci
# # # Vamos rodar nossa função usando zip.
# # # Zip pega os elementos de interesse da matriz e ignora os outros.
# # Aqui, 5 está fora da matriz, então é ignorado
# # for i, j in zip([1, 2], [3, 4, 5]):
# #     print(i, j)
# windchill = []
# for temp, windspeed in zip(data['tempout'], data['windspeed']):
#     windchill.append(compute_windchill(temp, windspeed))


# # *********** PARTE 11: Com o print do header no passo 10,
# # descobrimos que os dados de vento correspondem aos índices 7 e 8.
# # Agora vamos lê-los e adicioná-los ao docionário
# columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}
# # Velocidade do vento na coluna 7

# types = {'tempout': float, 'windspeed': float}
# # Velocidade do vento vem no formato de número

# data = {}
# for column in columns:
#     data[column] = []

# # Read and parse the data file
# filename = "wxobs20170821.txt"
# with open(filename, 'r') as datafile:

#     # Read the first three lines (header)
#     for _ in range(3):
#         datafile.readline()

#     # Read and parse the rest of the file
#     for line in datafile:
#         split_line = line.split()
#         for column in columns:
#             i = columns[column]
#             t = types.get(column, str)
#             value = t(split_line[i])
#             data[column].append(value)

# # DEBUG
# print(data['windspeed'])


# # *********** PARTE 10: Vamos construir uma função que lê
# # velocidade e direção do vento, e retorna um índice de Wind Chill
# columns = {'date': 0, 'time': 1, 'tempout': 2}

# # Queremos ler a coluna de temperaturas como float
# types = {'tempout': float}

# data = {}
# for column in columns:
#     data[column] = []
# # Faz um dicionário com as variáveis como listas vazias.
# # Mesmo que o comando da parte 8

# # Read and parse the data file
# filename = "wxobs20170821.txt"
# with open(filename, 'r') as datafile:

#     # Read the first three lines (header)
#     for _ in range(3):
#         headerline = datafile.readline()
#         print(headerline)


# # *********** PARTE 9: E se quisermos adicionar mais variáveis ao dicionário?
# # Os índices [0, 1, 2] correspondem à coluna no dado
# columns = {'date': 0, 'time': 1, 'tempout': 2}

# # Queremos ler a coluna de temperaturas como float
# # Data types for each column (only if non-string)
# types = {'tempout': float}

# # Não vamos mais estabelecer quais as variáveis/listas dentro do dicionário.
# # Vamos usar um loop for que fará isso automaticamnete
# data = {}
# for column in columns:
#     data[column] = []
# # Faz um dicionário com as variáveis como listas vazias.
# # Mesmo que o comando da parte 8

# # Read and parse the data file
# filename = "wxobs20170821.txt"
# with open(filename, 'r') as datafile:

#     # Read the first three lines (header)
#     for _ in range(3):
#         datafile.readline()

#     # Read and parse the rest of the file
#     for line in datafile:
#         split_line = line.split()
#         for column in columns:
#             i = columns[column]
#             t = types.get(column, str)
#             # data['float'] ---> str
#             # tenta achar os dados do tipo float, mas se não achar, lê como str
#             value = t(split_line[i])  # como fizemos float(split_line[coluna])
#             data[column].append(value)  # append automático com o dado no
#             # formato correto para cada variável/lista

# # DEBUG
# print(data['date'])
# print(data['tempout'])


# *********** PARTE 8: As nossas variáveis ainda estão na forma de strings.
# Não podemos analisá-las desse jeito. Portanto, aqui vamos apenas inserir o
# comando float nas linhas de append, assim, podemos adicionar os dados
# como números nas listas, não adicionar strings.
# data = {'date': [], 'time': [], 'tempout': []}
# filename = "wxobs20170821.txt"
# with open(filename, 'r') as datafile:
#     #
#     for _ in range(3):  # Read the first three lines (header)
#         datafile.readline()  # Se não ler as primeiras linhas vai dar erro -?
#     #
#     # Read and parse the rest of the file
#     for line in datafile:
#         split_line = line.split()
#         # print(split_line)
#         # Pega a coluna na lista do arquivo e adiciona à variável
#         data['date'].append(split_line[0])
#         data['time'].append(split_line[1])
#         data['tempout'].append(float(split_line[2]))  # !!!!!!!!! FLOAT AQUI

# # DEBUG
# print(data['tempout'])


# *********** PARTE 7: É dificil saber qual coluna corresponde à que variável.
# É mais interessante abrir o dado como um dicionário, ao invés de lista
# Ao invés de buscar por índice na row, podemos buscar por variável (tempo, T)
# Ao invés de colchetes, abrimos chaves. Ao invés de lista, dicionário...
# Initialize my data variable
# data = {'date': [], 'time': [], 'tempout': []}
# filename = "wxobs20170821.txt"
# with open(filename, 'r') as datafile:
#     #
#     for _ in range(3):  # Read the first three lines (header)
#         datafile.readline()  # Se não ler as primeiras linhas vai dar erro -?
#     #
#     # Read and parse the rest of the file
#     for line in datafile:
#         split_line = line.split()
#         # print(split_line)
#         # Pega a coluna na lista do arquivo e adiciona à variável
#         data['date'].append(split_line[0])
#         data['time'].append(split_line[1])
#         data['tempout'].append(split_line[2])

# DEBUG
# print(data['time'])


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


# *********** PARTE 5: Initialize data variable with dictionary
# data = []
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     #
#     for _ in range(3):  # same as loop in a list [0, 1, 2]
#         # print(_)  # Just to see what is the _, which is the same as i..
#         datafile.readline()  # read one line three times
#     #
#     for line in datafile:  # Read and parse all the file but the header
#         # print(line)
#         datum = line.split()  # Faz uma lista de "listas"
#         data.append(datum)  # Adiciona uma lista ao final do dicionário

# # DEBUG
# for datum in data:
#     print(datum)


# *********** PARTE 4: Descobrir qual o tipo de dado
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     data = datafile.read()


# *********** PARTE 3: Abrir com a função with
# Lê tudo de uma vez com menos linhas e ainda fecha o dado após a leitura
# Bom para quem esquece de fechar o dado
# filename = 'wxobs20170821.txt'
# with open(filename, 'r') as datafile:
#     data = datafile.read()
# DEBUG
# print(data)


# *********** PARTE 2: Abrir - read
# Mais rápido para ler todo o arquivo de uma vez
# Se tiver muitas linhas, vai ter que subir muito p ler .head()
# filename = 'wxobs20170821.txt'
# datafile = open(filename, 'r')
# data = datafile.read()
# datafile.close()
# DEBUG
# print(data)


# *********** PARTE 1: abrir dado com readline
# Bom para ler algumas linhas do começo e ver se está tudo ok
# Teria que digitar muitas vezes p/ ler o arquivo todo
# filename = 'wxobs20170821.txt'
# datafile = open(filename, 'r')
# # a cada chamada vai lendo as linhas em sequencia

# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())
