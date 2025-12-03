import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "cara"
    else:
        return "coroa"
    
def roll_dice():
    dice = random.randint(1, 6)
    return dice

def numero_aleatorio(start, end):
    return random.randint(start, end)

def jogar_adivinhacao():
    n = random.randint(1, 20)
    tentativas = 5
    resultados = []
    while tentativas > 0:
        palpite = random.randint(1, 20)
        resultados.append(palpite)
        if palpite < n:
            feedback = "Muito baixo!"
        elif palpite > n:
            feedback = "Muito alto!"
        else:
            feedback = f"Parabéns! Você acertou o número {n}"
            return resultados, feedback
        tentativas -= 1
    feedback = f"Suas tentativas acabaram. O número era {n}"
    return resultados, feedback

def pedra_papel_tesoura(escolha_usuario):
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    determinar_vencedor = lambda user, comp: (
        "Você venceu!" if (user == "pedra" and comp == "tesoura") or
                          (user == "papel" and comp == "pedra") or
                          (user == "tesoura" and comp == "papel")
        else "O computador venceu!" if user != comp
        else "Empate!"
    )
    if escolha_usuario == escolha_computador:
        return "Empate!"
        
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        
        return escolha_computador, determinar_vencedor(escolha_usuario, escolha_computador)
    else:
        
        return escolha_computador, determinar_vencedor(escolha_usuario, escolha_computador)
    
def get_soundboard_sound(name):
    sounds = {
        "applause": "sounds/applause.mp3",
        "boo": "sounds/boo.mp3",
        "drumroll": "sounds/drumroll.mp3"
    }
