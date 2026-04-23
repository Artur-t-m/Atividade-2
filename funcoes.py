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
    pontos = 0
    for i in range(len(lista_dados)):
        pontos += lista_dados[i]
    return pontos