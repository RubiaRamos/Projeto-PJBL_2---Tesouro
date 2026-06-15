# LABIRINTO DO TESOURO

# Função que mostra o mapa
def mostrar_mapa(mapa):
    for linha in mapa:
        print(" ".join(linha))
    print()


# Função que calcula o movimento do jogador
def mover(linha, coluna, comando):

    # Move para cima
    if comando == "W":
        return linha - 1, coluna

    # Move para baixo
    elif comando == "S":
        return linha + 1, coluna

    # Move para esquerda
    elif comando == "A":
        return linha, coluna - 1

    # Move para direita
    elif comando == "D":
        return linha, coluna + 1

    return linha, coluna


# Mapa do jogo
mapa_nivel1 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🦕', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🌿', '🧱'],
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
    ['🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱'],
    ['🧱','🦕','🟫','🟫','☄️','🟫','☄️','🟫','🌿','🧱'],
    ['🧱','☄️','🟫','🟫','🟫','☄️','🟫','☄️','🟫','🧱'],
    ['🧱','🟫','☄️','🟫','☄️','🟫','☄️','🟫','🟫','🧱'],
    ['🧱','🟫','🟫','🟫','🟫','🌿','🟫','☄️','🟫','🧱'],
    ['🧱','🟫','☄️','🟫','☄️','🟫','☄️','🟫','☄️','🧱'],
    ['🧱','☄️','🟫','🟫','🟫','☄️','🟫','☄️','🟫','🧱'],
    ['🧱','🟫','☄️','🟫','☄️','🟫','☄️','🟫','🟫','🧱'],
    ['🧱','🟫','🟫','🟫','🟫','🟫','🟫','🟫','🟦','🧱'],
    ['🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱']
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

# Controla o nível atual
nivel = 1

# Estatísticas
movimentos_validos = 0
movimentos_invalidos = 0
bombas_ativadas = 0

print("Bem-vindo ao Labirinto do Tesouro!")
print("Você começa com 50 pontos e 3 vidas.")

while True:

    # Mostra o mapa
    mostrar_mapa(mapa)

    # Mostra informações do jogador
    print("Nível:", nivel)
    print("Pontuação:", pontos)
    print("Vidas:", vidas)

    print("\nW = Cima")
    print("S = Baixo")
    print("A = Esquerda")
    print("D = Direita")
    print("Q = Sair")

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

    # Verifica comando inválido
    if comando not in ["W", "A", "S", "D"]:
        print("Comando inválido!")
        continue

    # Calcula a nova posição
    nova_linha, nova_coluna = mover(
        linha_jogador,
        coluna_jogador,
        comando
    )

    # Verifica se saiu dos limites do mapa
    if (nova_linha < 0 or nova_linha > 9 or
            nova_coluna < 0 or nova_coluna > 9):

        print("Movimento inválido!")
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

        if vidas == 0:
            print("\nGAME OVER!")
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
            print("\n🏆🏆🏆 PARABÉNS! 🏆🏆🏆")
            print("Você concluiu o NÍVEL 1!")
            print("+100 pontos")

            nivel = 2
            mapa = mapa_nivel2

            linha_jogador = 1
            coluna_jogador = 1

            print("\n========================")
            print("   NÍVEL 2 LIBERADO!")
            print("========================")
            print("Agora existem muito mais meteoros ☄️")
            print("Boa sorte!")

            input("\nPressione ENTER para iniciar o Nível 2...")

            continue

    # Atualiza posição do jogador
    mapa[linha_jogador][coluna_jogador] = "🟫"

    linha_jogador = nova_linha
    coluna_jogador = nova_coluna

    mapa[linha_jogador][coluna_jogador] = "🦕"

    # Conta movimento válido
    movimentos_validos += 1

    # Ganha 1 ponto por andar
    pontos += 1d
