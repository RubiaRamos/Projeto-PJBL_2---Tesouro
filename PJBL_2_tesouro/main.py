# LABIRINTO DO TESOURO

# Função que mostra o mapa
def mostrar_mapa(mapa):
    for linha in mapa:
        print(" ".join(linha))
    print()


# Função que calcula o movimento do jogador
def mover(linha, coluna, comando, passos=1):
    # Move para cima
    if comando == "W":
        return linha - passos, coluna

    # Move para baixo
    elif comando == "S":
        return linha + passos, coluna

    # Move para esquerda
    elif comando == "A":
        return linha, coluna - passos

    # Move para direita
    elif comando == "D":
        return linha, coluna + passos

    return linha, coluna

# funções de validação de movimento
# verifica se a posição está dentro da matriz
def dentro_do_mapa(linha, coluna):
    if linha < 0 or linha > 9:
        return False
    if coluna < 0 or coluna > 9:
        return False
    return True


# verifica se a posição contém uma parede
def tem_parede(mapa, linha, coluna):
    return mapa[linha][coluna] == "🧱"

print("\n---------------------Seja bem-vindo ao Salve o Dino-----------------------------\n")

nome_user = input("\nInforme seu nome: ")

print(f"\nBem-vindo(a) {nome_user} esse é o Salve o Dino!")
print("Você começa com 50 pontos e 3 vidas.\n")
print(f"Bem-vindo {nome_user} Labirinto do Tesouro!")
print("Você começa com 50 pontos e 3 vidas.")

# Mapa do jogo
mapa_nivel1 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🦕', '🟫', '🟫', '🍎', '🟫', '🟫', '🟫', '🌿', '🧱'],
    ['🧱', '🟫', '☄️', '🌿', '🟫', '🟫', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱'],
    ['🧱', '🟫', '🟫', '☄️', '🟫', '🌿', '🟫', '🟫', '🟫', '🧱'],
    ['🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🌿', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱'],
    ['🧱', '🟫', '☄️', '🟫', '🟫', '🟫', '🌿', '🟫', '🟫', '🧱'],
    ['🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟦', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
]

# Mapa do nível 2 (Difícil)
mapa_nivel2 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🦕', '🟫', '🟫', '☄️', '🟫', '☄️', '🟫', '🌿', '🧱'],
    ['🧱', '☄️', '🟫', '🟫', '🟫', '☄️', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🟫', '☄️', '🟫', '☄️', '🟫', '☄️', '🟫', '🟫', '🧱'],
    ['🧱', '🟫', '🍎', '🟫', '🟫', '🌿', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🟫', '☄️', '🟫', '☄️', '🟫', '☄️', '🟫', '☄️', '🧱'],
    ['🧱', '☄️', '🟫', '🟫', '🟫', '☄️', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🟫', '☄️', '🟫', '☄️', '🟫', '☄️', '🟫', '🟫', '🧱'],
    ['🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟦', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
]

# Mapa do nível 3
mapa_nivel3 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🦕', '🟫', '☄️', '☄️', '🟫', '☄️', '☄️', '🟫', '🧱'],
    ['🧱', '☄️', '🟫', '🟫', '🟫', '☄️', '🟫', '🟫', '☄️', '🧱'],
    ['🧱', '🟫', '☄️', '🟫', '☄️', '🟫', '☄️', '🟫', '🟫', '🧱'],
    ['🧱', '🌿', '🟫', '🟫', '🟫', '🌿', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🟫', '☄️', '☄️', '🟫', '🟫', '🟫', '🟫', '🍎', '🧱'],
    ['🧱', '☄️', '🟫', '🌿', '🟫', '☄️', '🟫', '☄️', '🟫', '🧱'],
    ['🧱', '🟫', '☄️', '☄️', '☄️', '🟫', '☄️', '🟫', '🟫', '🧱'],
    ['🧱', '🟦', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🌿', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
]

# Posição inicial do jogador
linha_jogador = 1
coluna_jogador = 1

# Usa o mapa do nível 1
mapa = mapa_nivel1

# Pontuação inicial
pontos = 50

# Quantidade de vidas
vidas = 3

# Poder especial
poder_duplo = False

# Controla o nível atual
nivel = 1

# Estatísticas
movimentos_validos = 0
movimentos_invalidos = 0
bombas_ativadas = 0

# passos
passos = 1

while True:

    # Mostra o mapa
    mostrar_mapa(mapa)

    # Mostra informações do jogador
    print("Nível:", nivel)
    print("Pontuação:", pontos)
    print("Vidas:", vidas)
    if poder_duplo:
        print("Poder especial: Disponível")
    else:
        print("Poder especial: Indisponível")

    print("\nW = Cima")
    print("S = Baixo")
    print("A = Esquerda")
    print("D = Direita")
    print("Q = Sair")
    print("P = Poder Especial")

    comando = input("\nDigite um comando: ").upper()

    print("Linha atual:", linha_jogador)
    print("Coluna atual:", coluna_jogador)

    nova_linha, nova_coluna = mover(
        linha_jogador,
        coluna_jogador,
        comando
    )

    print("Nova linha:", nova_linha)
    print("Nova coluna:", nova_coluna)

    # Sair do jogo
    if comando == "Q":
        print("Jogo encerrado!")
        break

    if comando == "P":

        if not poder_duplo:
            print("Você não possui poder especial!")
            continue

        direcao = input("Direção (W/A/S/D): ").upper()

        if direcao not in ["W", "A", "S", "D"]:
            print("Direção inválida!")
            continue

        print("Movimento duplo ativado!")
        passos = 2
        comando = direcao
        poder_duplo = False

    # Verifica comando inválido
    if comando not in ["W", "A", "S", "D", "P"]:
        print("Comando inválido!")
        continue

    # Calcula a nova posição
    nova_linha, nova_coluna = mover(
        linha_jogador,
        coluna_jogador,
        comando,
        passos
    )

    # validação de limites
    if not dentro_do_mapa(nova_linha, nova_coluna):
        print("Movimento inválido!")
        print("-5 pontos")
        pontos -= 5
        movimentos_invalidos += 1
        continue

    # Verifica parede
    if mapa[nova_linha][nova_coluna] == "🧱":
        print("Você bateu em uma parede!")
        print("-5 pontos")
        pontos -= 5
        movimentos_invalidos += 1
        continue

    # Verifica fruta
    elif mapa[nova_linha][nova_coluna] == "🍎":

        print("🍎 Fruta especial encontrada!")
        print("Poder de movimento duplo desbloqueado!")

        poder_duplo = True

    # Verifica planta
    elif mapa[nova_linha][nova_coluna] == "🌿":
        print("Você encontrou uma planta!")
        print("+10 pontos")
        pontos += 10

    # Verifica meteoro
    elif mapa[nova_linha][nova_coluna] == "☄️":

        print("\nUM METEORO ATINGIU VOCÊ!")
        print("-20 pontos")
        print("-1 vida")

        pontos -= 20
        vidas -= 1
        bombas_ativadas += 1

        # Game Over pergunta
        if vidas <= 0:
            print("💀 GAME OVER! Suas vidas acabaram.")
            opcao = input("Deseja reiniciar o jogo? (S/N): ").upper()

            if opcao == "S":

                mapa = mapa_nivel1
                linha_jogador = 1
                coluna_jogador = 1

                pontos = 50
                vidas = 3
                nivel = 1

                movimentos_validos = 0
                movimentos_invalidos = 0
                bombas_ativadas = 0

                print("\nReiniciando o jogo do Nível 1...\n")
                continue

            else:
                print("Obrigado por jogar!")
                break

        mapa[linha_jogador][coluna_jogador] = "🟫"

        linha_jogador = 1
        coluna_jogador = 1

        mapa[linha_jogador][coluna_jogador] = "🦕"

        print("Você voltou para o início!")

        continue

    # Verifica tesouro
    elif mapa[nova_linha][nova_coluna] == "🟦":

        pontos += 100

        if nivel == 1:
            print(f"\n🏆🏆🏆 PARABÉNS {nome_user}! 🏆🏆🏆")
            print("Você concluiu o NÍVEL 1!")
            print("+100 pontos")

            nivel = 2
            mapa = mapa_nivel2

            linha_jogador = 1
            coluna_jogador = 1

            print("\n========================")
            print("🎉🎉🎉NÍVEL 2 LIBERADO!🎉🎉🎉")
            print("========================")
            print("Agora existem muito mais meteoros ☄️")
            print("Boa sorte!")

            input("\nPressione ENTER para iniciar o Nível 2...")

            continue

        elif nivel == 2:
            nivel = 3
            mapa = mapa_nivel3

            linha_jogador = 1
            coluna_jogador = 1

            print("\n========================")
            print("🎉🎉🎉NÍVEL 3 LIBERADO!🎉🎉🎉")
            print("========================")
            print("Agora existem muito mais meteoros ☄️")
            print("Boa sorte!")

            input("\nPressione ENTER para iniciar o Nível 3...")

            continue


        else:

            print("\n========================")
            print(f"PARABENS {nome_user} CONCLUIU OS 3 NIVEIS!!!")
            print("========================")
            print("ESPERAMOS QUE TENHA GOSTADO!!!")
            print("NOME DOS CRIADORES:")
            print("Maria Clara Cordova, Rúbia Ramos e Vinicius Akio")
            print(f"Sua pontuação foi: {pontos}")
            print(f"Pontuação total {movimentos_validos}")

            break

    # Atualiza posição do jogador
    mapa[linha_jogador][coluna_jogador] = "🟫"

    linha_jogador = nova_linha
    coluna_jogador = nova_coluna

    mapa[linha_jogador][coluna_jogador] = "🦕"

    # Conta movimento válido
    movimentos_validos += 1

    # Ganha 1 ponto por andar
    pontos += 1

    # Reseta o poder
    passos = 1

