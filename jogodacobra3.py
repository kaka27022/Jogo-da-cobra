import random

arquivo = "placar3.txt"

# Inicializa placar padrão
vitorias = {"jogador1": 0, "jogador2": 0}

# Tenta ler o arquivo (se existir)
try:
    with open(arquivo, "r") as f:
        for linha in f:
            nome, pontos = linha.strip().split(":")
            vitorias[nome] = int(pontos)
except FileNotFoundError:
    pass  # Se o arquivo não existir, começa do zero

dados_jogados = 0

for n in range(0, 10000):
    def jogar_dado():
        global dados_jogados
        dado = random.randint(1, 6)
        dados_jogados += 1
        return dado

    def jogo (jogador):
        # Escada
        if jogador == 3:
            chance = random.randint(1,2)
            print(f"Chance: {chance}")
            if chance == 1:
                jogador = 16
        
        # Escada
        if jogador == 5:
            chance = random.randint(1,2)
            print(f"Chance: {chance}")
            if chance == 1:
                jogador = 7
        
        # Cobra
        if jogador == 12:
            jogador = 2

        # Cobra
        if jogador == 14:
            jogador = 11
        
        # Escada
        if jogador == 15:
            chance = random.randint(1,2)
            print(f"Chance: {chance}")
            if chance == 1:
                jogador = 25
        
        # Cobra
        if jogador == 17:
            jogador = 4

        # Escada
        if jogador == 18:
            chance = random.randint(1,2)
            print(f"Chance: {chance}")
            if chance == 1:
                jogador = 20

        # Escada
        if jogador == 21:
            chance = random.randint(1,2)
            print(f"Chance: {chance}")
            if chance == 1:
                jogador = 32
        
        # Cobra
        if jogador == 31:
            jogador = 19

        # Cobra
        if jogador == 35:
            jogador = 22

        if jogador > 36:
            jogador = 36
        return jogador
        
    jogador1 = 1
    jogador2 = 1

    while jogador1 < 36 or jogador2 < 36:
        jogador1 = jogador1 + jogar_dado()
        jogador1 = int(jogo(jogador1))
        print(f"Jogador 1 na posicao: {jogador1}")
        if jogador1 == 36:
            break

        jogador2 = jogador2 + jogar_dado()
        jogador2 = int(jogo(jogador2))
        print(f"Jogador 2 na posicao: {jogador2}")
        if jogador2 == 36:
            break

    if jogador1 == 36:
        print("Jogador 1 venceu")
        vitorias["jogador1"] += 1
    elif jogador2 == 36:
        print("Jogador 2 venceu")
        vitorias["jogador2"] += 1

    with open(arquivo, "w") as f:
        for nome in vitorias:
            f.write(f"{nome}:{vitorias[nome]}\n")

print(f"Média de dados jogados: {dados_jogados/10000}")
