import discord
from bot_logic import *
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Qual o seu nome ?'):
        await message.channel.send("Meu nome é chatbot!")
    elif message.content.startswith('$bye'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$gerar senha'):
        senha = gen_pass(10)
        await message.channel.send(f"Sua senha é: {senha}")
    elif message.content.startswith('$jogar moeda'):
        resultado = flip_coin()
        await message.channel.send(f"O resultado do lançamento da moeda é: {resultado}")
    elif message.content.startswith('$rolar dado'):
        resultado2 = roll_dice()
        await message.channel.send(f"O resultado do dado é: {resultado2}")
    elif message.content.startswith('$numero aleatorio'):
        partes = message.content.split()
        if len(partes) == 4:
            start = int(partes[2])
            end = int(partes[3])
            numero = numero_aleatorio(start, end)
            await message.channel.send(f"Número aleatório entre {start} e {end}: {numero}")
        else:
            await message.channel.send("Por favor, use o formato: $numero aleatorio <start> <end>")
    elif message.content.startswith('$jogar adivinhacao'):
        resultados, feedback = jogar_adivinhacao()
        await message.channel.send(f"Resultados dos palpites: {resultados}\n{feedback}")
    elif message.content.startswith('$pedra papel tesoura'):
        partes = message.content.split()
        if len(partes) == 4:
            escolha_usuario = partes[3].lower()
            if escolha_usuario in ["pedra", "papel", "tesoura"]:
                resultado3 = pedra_papel_tesoura(escolha_usuario)
                await message.channel.send(f"Você escolheu: {escolha_usuario}\n{resultado3}")
            else:
                await message.channel.send("Escolha inválida! Por favor, escolha entre 'pedra', 'papel' ou 'tesoura'.")
        else:
            await message.channel.send("Por favor, use o formato: $pedra papel tesoura <sua escolha>")
    elif message.content.startswith('$funçoes'):
        funcoes = """
        $Qual o seu nome ? - O bot responde com seu nome.
        $bye - O bot responde com um emoji.
        $gerar senha - Gera uma senha aleatória.
        $jogar moeda - Simula o lançamento de uma moeda.
        $rolar dado - Simula o lançamento de um dado.
        $numero aleatorio <start> <end> - Gera um número aleatório entre start e end.
        $jogar adivinhacao - Joga o jogo de adivinhação de números.
        $pedra papel tesoura <sua escolha> - Joga pedra, papel ou tesoura contra o bot.
        """
        await message.channel.send(funcoes)
   
        
        
        
    else:
        await message.channel.send("Comando não reconhecido. Use $funçoes para ver a lista de comandos disponíveis.")
# Substitua "YOUR_BOT_TOKEN" pelo token real do seu bot                         



client.run("Seu_token_aqui")
