import random

arquivo = "placar5.txt"

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

for n in range(0, 10000):
    def jogar_dado():
        dado = random.randint(1, 6)
        return dado

    def jogo (jogador, num_jog):
        global contador_cobra
        # Escada
        if jogador == 3:
            jogador = 16
        
        # Escada
        if jogador == 5:
            jogador = 7
        
        # Cobra
        if jogador == 12:
            if num_jog == 1 or contador_cobra > 0:
                jogador = 2
            
            if num_jog == 2:
                contador_cobra += 1

            #print(f"Contador cobra: {contador_cobra}")

        # Cobra
        if jogador == 14:
            if num_jog == 1 or contador_cobra > 0:
                jogador = 11
            
            if num_jog == 2:
                contador_cobra += 1

            #print(f"Contador cobra: {contador_cobra}")
        
        # Escada
        if jogador == 15:
            jogador = 25
        
        # Cobra
        if jogador == 17:
            if num_jog == 1 or contador_cobra > 0:
                jogador = 4
            
            if num_jog == 2:
                contador_cobra += 1

            #print(f"Contador cobra: {contador_cobra}")

        # Escada
        if jogador == 18:
            jogador = 20

        # Escada
        if jogador == 21:
            jogador = 32
        
        # Cobra
        if jogador == 31:
            if num_jog == 1 or contador_cobra > 0:
                jogador = 19
            
            if num_jog == 2:
                contador_cobra += 1

            #print(f"Contador cobra: {contador_cobra}")

        # Cobra
        if jogador == 35:
            if num_jog == 1 or contador_cobra > 0:
                jogador = 22
            
            if num_jog == 2:
                contador_cobra += 1

        if jogador > 36:
            jogador = 36
        return jogador
        
    jogador1 = 1
    jogador2 = 1

    contador_cobra = 0

    while jogador1 < 36 or jogador2 < 36:
        jogador1 = jogador1 + jogar_dado()
        jogador1 = int(jogo(jogador1, 1))
        #print(f"Jogador 1 na posicao: {jogador1}")
        if jogador1 == 36:
            break

        jogador2 = jogador2 + jogar_dado()
        jogador2 = int(jogo(jogador2, 2))
        #print(f"Jogador 2 na posicao: {jogador2}")
        if jogador2 == 36:
            break

    if jogador1 == 36:
        #print("Jogador 1 venceu")
        vitorias["jogador1"] += 1
    elif jogador2 == 36:
        #print("Jogador 2 venceu")
        vitorias["jogador2"] += 1

    with open(arquivo, "w") as f:
        for nome in vitorias:
            f.write(f"{nome}:{vitorias[nome]}\n")