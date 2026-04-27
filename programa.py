#Aqui a gente faz o programa.
from funcoes import *
rodada = 0
while rodada<12:
    reroll = 0
    cartela = {"regra_simples": {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1}, "regra_avancada": {"sem_combinacao":-1, "quadra":-1, "full_house":-1, "sequencia_baixa":-1, "sequencia_alta":-1, "cinco_iguais":-1}}
    dados_em_jogo = rolar_dados(5)
    dados_no_estoque = []
    acao = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    while acao != "0":
        if acao == "1":
            dados_em_jogo, dados_em_estoque = guardar_dado(dados_em_jogo, dados_no_estoque, int(input("Digite o índice do dado a ser guardado (0 a 4):")))
        elif acao == "2":
            dados_em_jogo, dados_em_estoque = remover_dado(dados_em_jogo, dados_no_estoque, int(input("Digite o índice do dado a ser removido (0 a 4):")))
        elif acao == "3":
            if reroll == 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_em_jogo = rolar_dados(len(dados_em_jogo))
                reroll += 1
        elif acao == "4":
            imprime_cartela(cartela)
        elif acao == "0":
            while True:
                categoria = input("Digite a combinação desejada:")
                if categoria == "sem_combinacao" or categoria == "quadra" or categoria == "full_house" or categoria == "sequencia_baixa" or categoria == "sequencia_alta" or categoria == "cinco_iguais":
                    if cartela["regra_avancada"][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    cartela = faz_jogada(dados_em_jogo, categoria, cartela)
                    rodada += 1
                    break
                elif categoria in ["1", "2", "3", "4", "5", "6"]:
                    if cartela["regra_simples"][int(categoria)] != -1:
                        print("Essa combinação já foi utilizada.")
                    cartela = faz_jogada(dados_em_jogo, categoria, cartela)
                    rodada += 1
                    break
        else:
            print("Opção inválida, tente novamente.")


