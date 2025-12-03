# Bot_discord


1. bot.py
Este é o arquivo principal do bot Discord. Ele contém:

Configuração das permissões (intents) para permitir que o bot leia o conteúdo das mensagens.

Criação do cliente (discord.Client) que conecta o bot ao Discord.

Eventos principais:

on_ready → Executado quando o bot entra online, mostrando no console que o login foi feito.

on_message → Responsável por interpretar os comandos enviados pelos usuários e responder de acordo.

Lista de comandos implementados:

$Qual o seu nome ? → O bot responde com seu nome.

$bye → O bot envia um emoji aleatório.

$gerar senha → Gera uma senha aleatória.

$jogar moeda → Simula o lançamento de uma moeda.

$rolar dado → Simula o lançamento de um dado.

$numero aleatorio <start> <end> → Gera um número aleatório dentro de um intervalo.

$jogar adivinhacao → Jogo de adivinhação de números.

$pedra papel tesoura <sua escolha> → Jogo de pedra, papel ou tesoura contra o bot.

$funçoes → Mostra a lista de comandos disponíveis.

Caso o usuário digite um comando inválido, o bot responde com uma mensagem explicando como ver os comandos disponíveis.

👉 Em resumo: bot.py é o cérebro que conecta o bot ao Discord e interpreta os comandos dos usuários.

2. bot_logic.py
Este arquivo contém a lógica das funções que o bot utiliza. Ele funciona como uma biblioteca auxiliar para o bot.py.

Funções implementadas:

gen_pass(pass_length) → Gera uma senha aleatória com símbolos.

gen_emodji() → Retorna um emoji aleatório.

flip_coin() → Simula o lançamento de uma moeda (cara ou coroa).

roll_dice() → Simula o lançamento de um dado (1 a 6).

numero_aleatorio(start, end) → Retorna um número aleatório dentro de um intervalo.

jogar_adivinhacao() → Jogo de adivinhação: o bot escolhe um número secreto e faz palpites automáticos, dando feedback.

pedra_papel_tesoura(escolha_usuario) → Jogo de pedra, papel ou tesoura contra o computador, determinando o vencedor.

get_soundboard_sound(name) → Retorna o caminho de arquivos de sons pré-definidos (aplausos, vaias, rufar de tambores).

👉 Em resumo: bot_logic.py é o conjunto de funções que dão vida às respostas do bot.

🎯 Visão Geral
bot.py → Interface com o Discord, responsável por receber mensagens e enviar respostas.

bot_logic.py → Biblioteca de funções que implementa a lógica dos jogos e utilidades usadas pelo bot.
