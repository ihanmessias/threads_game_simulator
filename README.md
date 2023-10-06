# 🤖 Simulador de Jogo Multiplayer com Threads
Este é um exemplo prático de um simulador de jogo multiplayer em Python que utiliza threads para simular ações concorrentes de vários jogadores. Este código foi construído para fins de aprendizado e demonstração de como as threads podem ser usadas para criar sistemas paralelos.

## Como Funciona
O script utiliza a biblioteca `threading` para criar várias threads, uma para cada jogador, representando as ações que eles tomam no jogo.

*Dados dos Jogadores*: Os dados iniciais dos jogadores são definidos em um dicionário chamado `dados_personagens`, que inclui informações como `vida`  e `poder de ataque`.

*Função `processar_comandos`*: Esta função simula o processamento de comandos pelo servidor para cada jogador. Ela escolhe aleatoriamente entre dois comandos: **"atacar"** ou **"se_curar"**. Os comandos são processados de forma assíncrona em threads separadas para cada jogador. Os jogadores podem atacar outros jogadores ou se curar.

*Threads dos Jogadores*: O script cria uma lista de threads chamada `threads_jogadores` e, em seguida, inicializa e inicia uma thread separada para cada jogador. Cada thread executa a função `processar_comandos` em paralelo, simulando as ações dos jogadores.

*Aguardando as Threads*: O script aguarda todas as threads dos jogadores terminarem de processar seus comandos usando o método `join()`.

*Resultado*: Após todas as ações serem processadas, o script imprime o estado atual das personagens dos jogadores e informa que todos os comandos dos jogadores foram processados.

### 🤝 Suporte/Contato

[![LinkedIn Badge](https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=)](https://www.linkedin.com/in/ihanmessias/)
[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/61996487935)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/devlinuxtv/)

✉ ihanmessias.dev@gmail.com

<p align="center">Ihan Messias Nascimento dos Santos</p>