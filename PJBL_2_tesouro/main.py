# LABIRINTO DO TESOURO

def mostrar_mapa(mapa):
    for linha in mapa:
        print(" ".join(linha))
    print()

## Mover dino
def mover(linha, coluna, jogador):
    if jogador == "W":
        return linha - 1, coluna
    elif jogador == "S":
        return linha + 1, coluna
    elif jogador == "A":
        return linha, coluna - 1
    elif jogador == "D":
        return linha, coluna + 1

    return linha, coluna

# funções de validação de movimento (VINICIUS)
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

mapa = [
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
## Dino andar
linha = 1
coluna = 1
## Dino andar
movimentos_validos = 0
movimentos_invalidos = 0
bombas_ativadas = 0

# Posição inicial do jogador
linha_jogador = 1
coluna_jogador = 1

# Pontuação inicial
pontos = 50

# Quantidade de vidas
vidas = 3

while True:

    mostrar_mapa(mapa)

    print("Pontuação:", pontos)
    print("W = Cima")
    print("S = Baixo")
    print("A = Esquerda")
    print("D = Direita")
    print("Q = Sair")

    comando = input("Digite um comando: ").upper()

    if comando == "Q":
        print("Jogo encerrado!")
        break

    if comando not in ["W", "A", "S", "D"]:
        print("Comando inválido!")
        continue

    nova_linha, nova_coluna = mover(linha, coluna, comando)

    # validação de limites
    if not dentro_do_mapa(nova_linha, nova_coluna):
        print("Movimento inválido! Você tentou sair do mapa.")
        pontos -= 5
        movimentos_invalidos += 1
        continue

    # validação de paredes
    if tem_parede(mapa, nova_linha, nova_coluna):
        print("Você bateu em uma parede!")
        pontos -= 5
        movimentos_invalidos += 1
        continue

        # Verifica planta
    if mapa[nova_linha][nova_coluna] == "🌿":
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

        print("Pontuação atual:", pontos)
        print("Vidas restantes:", vidas)

        # Acabaram as vidas
        if vidas == 0:
            print("\nGAME OVER!")
            print("Você perdeu todas as vidas!")

            print("\n===== RELATÓRIO FINAL =====")
            print("Pontuação final:", pontos)
            print("Movimentos válidos:", movimentos_validos)
            print("Movimentos inválidos:", movimentos_invalidos)
            print("Meteoros ativados:", bombas_ativadas)
            break

        # Remove jogador da posição atual
        mapa[linha_jogador][coluna_jogador] = "🟫"

        # Volta para o início
        linha_jogador = 1
        coluna_jogador = 1

        # Coloca o jogador no início
        mapa[linha_jogador][coluna_jogador] = "🦕"

        print("Você voltou para o início!")

        continue

        # Verifica tesouro
    elif mapa[nova_linha][nova_coluna] == "🟦":

        pontos += 100

        mapa[linha_jogador][coluna_jogador] = "🟫"

        linha_jogador = nova_linha
        coluna_jogador = nova_coluna

        mapa[linha_jogador][coluna_jogador] = "🦕"

        print("\nPARABÉNS!")
        print("Você encontrou o tesouro!")
        print("+100 pontos")

        print("\n===== RELATÓRIO FINAL =====")
        print("Pontuação final:", pontos)
        print("Vidas restantes:", vidas)
        print("Movimentos válidos:", movimentos_validos)
        print("Movimentos inválidos:", movimentos_invalidos)
        print("Meteoros ativados:", bombas_ativadas)

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

    # Limpa posição antiga
    mapa[linha][coluna] = "🟫"

    # Atualiza posição
    linha = nova_linha
    coluna = nova_coluna

    # Coloca o dinossauro na nova posição
    mapa[linha][coluna] = "🦕"

