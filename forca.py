import random

# 1. Lista de palavras a escolher aleatoriamente
lista_palavras = ['Portugal']

# 2. Escolher uma palavra aleatória da lista
palavra_secreta = random.choice(lista_palavras)

# 3. criar a lista de letras descobertas de forma automática
letras_descobertas = ['_' for _ in palavra_secreta]

# 4. Definir o número de vidas
tentativas = 6

# 5. Lista de letras erradas
letras_erradas = []

print('|***||***| BEM-VINDO AO JOGO DA FORCA: VERSÃO UNIÃO EUROPEIA |***||***|')
print()
print('\n' + '='*40)
print(f'Palavra Secreta: {" ".join(letras_descobertas)}')
print(f'Vidas Restantes: {tentativas}')
print(f'Letras Erradas: {", ".join(letras_erradas)}')

#6. Criar o ciclo do jogo
while tentativas > 0 and '_' in letras_descobertas:
    palpite = input('\nDigite uma letra: ').upper()

    #Verifica se a letra está na palavra secreta
    if palpite in palavra_secreta.upper():
        print(f"Bom palpite! A Letra: '{palpite}' existe na palavra secreta.")
        #Atualizar a letra na palavra secreta
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i].upper() == palpite:
                letras_descobertas[i] = palpite
    else:
        print(f"Oh, que pena! A Letra '{palpite}' não existe na palavra secreta. Tenta novamente!")
        letras_erradas.append(palpite)
        tentativas -= 1