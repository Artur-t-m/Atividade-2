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
        dict_dados[dado] += 1               #Só pra garantir
    if 4 in dict_dados.values() or 5 in dict_dados.values() or 6 in dict_dados.values() or 7 in dict_dados.values() or 8 in dict_dados.values() or 9 in dict_dados.values() or 10 in dict_dados.values():
        soma = 0
        for i in range(len(lista_dados)):
            soma += lista_dados[i]
        return soma 
    else:
        return 0

def calcula_pontos_quina(lista_dados):
    dict_dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in lista_dados:
        dict_dados[dado] += 1               #Melhor não ter erro na entrega, gastei boa parte do meu tempo só fazendo essa parte, denovo
    if 5 in dict_dados.values() or 6 in dict_dados.values() or 7 in dict_dados.values() or 8 in dict_dados.values() or 9 in dict_dados.values() or 10 in dict_dados.values():
        return 50
    else:
        return 0

def calcula_pontos_regra_avancada(lista_dados):
    dict_pontos = {}
    dict_pontos["cinco_iguais"] = calcula_pontos_quina(lista_dados)
    dict_pontos["full_house"] = calcula_pontos_full_house(lista_dados)
    dict_pontos["quadra"] = calcula_pontos_quadra(lista_dados)
    dict_pontos["sem_combinacao"] = calcula_pontos_soma(lista_dados)
    dict_pontos["sequencia_alta"] = calcula_pontos_sequencia_alta(lista_dados)
    dict_pontos["sequencia_baixa"] = calcula_pontos_sequencia_baixa(lista_dados)
    return dict_pontos

def faz_jogada(dados, categoria, cartela):
    if categoria == "sem_combinacao":
        cartela["regra_avancada"]["sem_combinacao"] = calcula_pontos_regra_avancada(dados)["sem_combinacao"]
    elif categoria == "quadra":
        cartela["regra_avancada"]["quadra"] = calcula_pontos_regra_avancada(dados)["quadra"]
    elif categoria == "full_house":
        cartela["regra_avancada"]["full_house"] = calcula_pontos_regra_avancada(dados)["full_house"]
    elif categoria == "sequencia_baixa":
        cartela["regra_avancada"]["sequencia_baixa"] = calcula_pontos_regra_avancada(dados)["sequencia_baixa"]
    elif categoria == "sequencia_alta":
        cartela["regra_avancada"]["sequencia_alta"] = calcula_pontos_regra_avancada(dados)["sequencia_alta"]
    elif categoria == "cinco_iguais":
        cartela["regra_avancada"]["cinco_iguais"] = calcula_pontos_regra_avancada(dados)["cinco_iguais"]
    else:
        cartela["regra_simples"][categoria] = calcula_pontos_regra_simples(dados)[int(categoria)]
    return cartela