import random
def escolher_palavra():
    palavras = ["morango","banana","abacate","uva","laranja"]
    return random.choice(palavras)
def avaliar_tentativa(palavra_secreta, tentativa):
    corretas = []
    erradas = []
    for i, letra in enumerate(tentativa):
        if letra == palavra_secreta[i]:
            corretas.append(letra)
        elif letra in palavra_secreta:
            erradas.append(letra)
        return corretas, erradas
def gerar_dica(tentativas, palavra_secreta):
    dicas = []
    for tentativa in tentativas:
        corretas, erradas = avaliar_tentativa(palavra_secreta, tentativa)
        dicas.append(f'Tentativa: {tentativa} | Corretas: {''.join(corretas)} | Erradas: {''.join(erradas)}')
    return dicas
def jogo_adivinhacao():
    palavra_secreta = escolher_palavra()
    tentativas = []
    tentativas_maximas = 6

    print('Bem-vindo ao Guess Fruit!')
    print('Você tem', tentativas_maximas, 'tentativas para adivinhar a fruta.')

    while len(tentativas) < tentativas_maximas:
        tentativa = input('Digite sua fruta: ').lower()
        if len(tentativa) != len(palavra_secreta):
            print(f'A palavra deve ter {len(palavra_secreta)} letras. Tente novamente.')
            continue
        tentativas.append(tentativa)
        corretas, erradas = avaliar_tentativa(palavra_secreta, tentativa)

        if tentativa == palavra_secreta:
            print('Parabéns! Você acertou a fruta:', palavra_secreta)
            break

        print(f'Letras corretas na posição correta: {''.join(corretas)}')
        print(f'Letras corretas mas em posição errada: {''.join(erradas)}')
#        print(f'Tentativas até agora:{tentativas}')

        if len(tentativas) >= tentativas_maximas:
            print('Você esgotou suas tentativas! A palavras era:', palavra_secreta)
            break

        dicas = gerar_dica(tentativas, palavra_secreta)
        print('Dicas até agora:')
        for dica in dicas:
            print(dica)

if __name__ == '__main__':
    jogo_adivinhacao()