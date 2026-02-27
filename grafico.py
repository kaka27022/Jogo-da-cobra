import matplotlib.pyplot as plt

arquivo = "placar.txt"

vitorias = {}

# Lê o arquivo
with open(arquivo, "r") as f:
    for linha in f:
        linha = linha.strip()
        if ":" in linha:
            nome, pontos = linha.split(":")
            vitorias[nome] = int(pontos)

# Separando dados para o gráfico
jogadores = list(vitorias.keys())
valores = list(vitorias.values())

# Criando gráfico
plt.figure()
plt.bar(jogadores, valores)

plt.title("Placar - Jogo da Cobra")
plt.xlabel("Jogadores")
plt.ylabel("Número de Vitórias")

plt.show()