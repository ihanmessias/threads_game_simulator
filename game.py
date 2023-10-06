import threading
import time
import random

# Dados iniciais das personagens dos jogadores
dados_personagens = {
    "Jogador1": {"vida": 100, "ataque": 10},
    "Jogador2": {"vida": 120, "ataque": 12},
    "Jogador3": {"vida": 80, "ataque": 8},
    "Jogador4": {"vida": 150, "ataque": 15},
    "Jogador5": {"vida": 110, "ataque": 11}
}

# Função que simula o processamento de comandos pelo servidor
def processar_comandos(jogador):
    global dados_personagens
    
    comandos = random.choice(["atacar", "se_curar"])
    
    print(f"{jogador}: Enviando comandos: {comandos}")
    time.sleep(random.uniform(0.5, 2))  # Simulando tempo de processamento variável
    
    if comandos == "atacar":
        alvo = random.choice(list(dados_personagens.keys()))
        if alvo != jogador:
            dano = dados_personagens[jogador]["ataque"]
            dados_personagens[alvo]["vida"] -= dano
            print(f"{jogador} atacou {alvo} e causou {dano} de dano.")
    
    elif comandos == "se_curar":
        cura = random.randint(10, 20)
        dados_personagens[jogador]["vida"] += cura
        print(f"{jogador} se curou e recuperou {cura} de vida.")
    
    print(f"{jogador}: Comandos processados pelo servidor.")
    print(f"{jogador}: Vida restante: {dados_personagens[jogador]['vida']}")

# Cria uma lista de threads para representar os jogadores
threads_jogadores = []

# Inicializa e inicia as threads dos jogadores
for jogador in dados_personagens.keys():
    thread = threading.Thread(target=processar_comandos, args=(jogador,))
    threads_jogadores.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads_jogadores:
    thread.join()

print("Todos os comandos dos jogadores foram processados.")
print("Estado atual das personagens:", dados_personagens)