import random
import os

# 1. Configurações gerais e variáveis
lista_palavras = ['Portugal']
palavra_secreta = random.choice(lista_palavras).upper()
letras_descobertas = ['_' for _ in palavra_secreta]
tentativas = 6
letras_erradas = []
mensagem = "Boa sorte! Tenta adivinhar a palavra secreta."

# 2. Ciclo do jogo
while tentativas > 0 and '_' in letras_descobertas:
    os.system('cls' if os.name == 'nt' else 'clear')

# 3. Quadro do jogo  
    print('|***||***| JOGO DA FORCA: EDIÇÃO - UNIÃO EUROPEIA |***||***|')
    print('\n')
    print('='*60)
    print(f'Palavra secreta: {" ".join(letras_descobertas)}')
    print(f'Vidas restantes: {tentativas}')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    print(f'Estado: {mensagem}')
    print('='*60)

# 4. Registo do palpite  
    palpite = input('Qual o seu palpite? Indique uma Letra: ').upper()

    # 5. Validar repetição de letra
    if palpite in letras_descobertas or palpite in letras_erradas:
        mensagem = f'ATENÇÃO! A LETRA "{palpite}" JA FOI USADA!'
        continue  # <--- ESTA LINHA É QUE TRAVA O DESCONTO DE VIDAS

    # 6. Validar se foi uma letra correta ou incorreta
    if palpite in palavra_secreta:
        mensagem = "BOA! ACERTASTE NUMA LETRA!"
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == palpite:
                letras_descobertas[i] = palpite
    else:
        mensagem = f"OH QUE PENA! ERRASTE. A LETRA '{palpite}' NÃO PERTENCE À PALAVRA!"
        letras_erradas.append(palpite)
        tentativas -= 1

# 7. Conclusão do jogo
os.system('cls' if os.name == 'nt' else 'clear')
print('|***||***| JOGO DA FORCA: EDIÇÃO - UNIÃO EUROPEIA |***||***|')
print('\n' + '='*60)
print(f'Palavra secreta: {" ".join(letras_descobertas)}')
print(f'Vidas restantes: {tentativas}')
print(f'Letras erradas: {", ".join(letras_erradas)}')
print('='*60)

if '_' not in letras_descobertas:
    print(f"\n MUITO BEM. GANHASTE! A palavra secreta era: {palavra_secreta}")
else:
    print(f"\n QUE PENA! PERDESTE! A palavra secreta era: {palavra_secreta}")

print('='*60)