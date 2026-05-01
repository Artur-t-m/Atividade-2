from funcoes import *
rodada = 0
cartela = {"regra_simples": {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
           "regra_avancada": {"sem_combinacao":-1,"quadra":-1,"full_house":-1,"sequencia_baixa":-1,"sequencia_alta":-1,"cinco_iguais":-1}}

while rodada < 12:
    reroll = 0
    dados_em_jogo = rolar_dados(5)
    dados_no_estoque = []

    while True:
        print("Dados rolados:", dados_em_jogo)
        print("Dados guardados:", dados_no_estoque)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        acao = input(">")

        if acao == "1":
            print(f"Digite o índice do dado a ser guardado (0 a {len(dados_em_jogo)-1}):")
            pos = int(input(">"))

            if pos < 0 or pos >= len(dados_em_jogo):
                print("Opção inválida. Tente novamente.")
            else:
                dados_em_jogo, dados_no_estoque = guardar_dado(dados_em_jogo, dados_no_estoque, pos)

        elif acao == "2":
            print(f"Digite o índice do dado a ser removido (0 a {len(dados_no_estoque)-1}):")
            pos = int(input(">"))

            if pos < 0 or pos >= len(dados_no_estoque):
                print("Opção inválida. Tente novamente.")
            else:
                dados_em_jogo, dados_no_estoque = remover_dado(dados_em_jogo, dados_no_estoque, pos)

        elif acao == "3":
            if reroll >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_em_jogo = rolar_dados(len(dados_em_jogo))
                reroll += 1

        elif acao == "4":
            imprime_cartela(cartela)

        elif acao == "0":
            dados_totais = dados_em_jogo + dados_no_estoque

            while True:
                print("Digite a combinação desejada:")
                categoria = input(">")

                if categoria in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados_totais, categoria, cartela)
                        rodada += 1
                        break

                elif categoria in ["1","2","3","4","5","6"]:
                    if cartela["regra_simples"][int(categoria)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados_totais, categoria, cartela)
                        rodada += 1
                        break

                else:
                    print("Combinação inválida. Tente novamente.")

            break

        else:
            print("Opção inválida. Tente novamente.")

pontuacao = 0

soma_simples = sum(v for v in cartela["regra_simples"].values() if v != -1)
pontuacao += soma_simples

pontuacao += sum(v for v in cartela["regra_avancada"].values() if v != -1)

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print("Pontuação total:", pontuacao)