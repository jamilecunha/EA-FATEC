arquivo = open("dados_2.txt", "r")
dados = []

for linha in arquivo:
    linha = linha.strip('\n')
    dados.append(linha.strip(' '))

dados_ordenados = [float(i) for i in dados]
dados_ordenados = sorted(dados_ordenados)
print(dados_ordenados)

quantidade_de_dados = len(dados_ordenados)
print('Quantidade de dados = ', quantidade_de_dados)

soma_dados = 0
for soma in dados_ordenados:
    soma_dados += soma
print('Soma de valores = ', round(soma_dados))

media = soma_dados / quantidade_de_dados
print('Média = ', (media))

repeticao = 0
for i in dados_ordenados:
    descoberta = dados_ordenados.count(i)
    if descoberta > repeticao:
        repeticao = descoberta

moda = []

for i in dados_ordenados:
    descoberta = dados_ordenados.count(i)
    if descoberta == repeticao and i not in moda:
        moda.append(i)
print('Moda = ', moda)

dados_mediana = quantidade_de_dados
primeiro_quartil = quantidade_de_dados
terceiro_quartil = quantidade_de_dados
if dados_mediana % 2 == 1:
    mediana = dados_ordenados[dados_mediana//2]
    primeiro_quartil = dados_ordenados[primeiro_quartil//4]
    terceiro_quartil = dados_ordenados[terceiro_quartil//-4]
else:
    mediana = (dados_ordenados[dados_mediana//2 -1]+dados_ordenados[dados_mediana//2]) / 2
    primeiro_quartil= (dados_ordenados[primeiro_quartil//4]+dados_ordenados[primeiro_quartil//4]) / 2
    terceiro_quartil= (dados_ordenados[terceiro_quartil//-4]+dados_ordenados[terceiro_quartil//-4]) / 2
print("Primeiro Quartil (Q1) = ", primeiro_quartil)
print("Segundo Quartil - Mediana (Q2) = ", mediana)
print("Terceiro Quartil (Q3) = ", terceiro_quartil)