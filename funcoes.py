import random
def rolar_dados(n_dados):
    resultado = []
    for i in range(n_dados):
        resultado.append(random.randint(1, 6))
    return resultado