import random
def rolar_dados(n_dados):
    resultado = []
    for i in range(n_dados):
        resultado.append(random.randint(1, 6))
    return resultado

def guardar_dado(dados_rolados, dados_no_estoque, dados_para_guardar):
    dados_no_estoque.append(dados_rolados[dados_para_guardar])
    del dados_rolados[dados_para_guardar]
    lista_dados = [dados_rolados, dados_no_estoque]
    return lista_dados

def remover_dado(dados_rolados, dados_no_estoque, dados_para_remover):
    dados_rolados.append(dados_no_estoque[dados_para_remover])
    del dados_no_estoque[dados_para_remover]
    lista_dados = [dados_rolados, dados_no_estoque]
    return lista_dados

def calcula_pontos_regra_simples(lista_dados):
    pontos_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in lista_dados:
        pontos_dict[dado] += dado
    return pontos_dict

def calcula_pontos_soma(lista_dados):
    soma = 0
    for i in range(len(lista_dados)):
        soma += lista_dados[i]
    return soma

def calcula_pontos_sequencia_baixa(lista_dados): #irmão, deve ter um jeito mais fácil, mas não me importo, tá aí.
    dict_dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in lista_dados:
        dict_dados[dado] += 1
    if dict_dados[1] >= 1 and dict_dados[2] >= 1 and dict_dados[3] >= 1 and dict_dados[4] >= 1:
        return 15
    elif dict_dados[2] >= 1 and dict_dados[3] >= 1 and dict_dados[4] >= 1 and dict_dados[5] >= 1:
        return 15
    elif dict_dados[3] >= 1 and dict_dados[4] >= 1 and dict_dados[5] >= 1 and dict_dados[6] >= 1:
        return 15
    else:
        return 0
    
def calcula_pontos_sequencia_alta(lista_dados): 
    dict_dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in lista_dados:
        dict_dados[dado] += 1
    if dict_dados[1] >= 1 and dict_dados[2] >= 1 and dict_dados[3] >= 1 and dict_dados[4] >= 1 and dict_dados[5] >= 1:
        return 30
    elif dict_dados[2] >= 1 and dict_dados[3] >= 1 and dict_dados[4] >= 1 and dict_dados[5] >= 1 and dict_dados[6] >= 1:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(lista_dados): #Ou era dicionário ou era 1000000 de elifs.
    dict_dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in lista_dados:
        dict_dados[dado] += 1
    if 3 in dict_dados.values() and 2 in dict_dados.values():
        soma = 0
        for i in range(len(lista_dados)):
            soma += lista_dados[i]
        return soma 
    else:
        return 0

def calcula_pontos_quadra(lista_dados):
    dict_dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in lista_dados:
        dict_dados[dado] += 1
    if 4 in dict_dados.values():
        soma = 0
        for i in range(len(lista_dados)):
            soma += lista_dados[i]
        return soma 
    else:
        return 0