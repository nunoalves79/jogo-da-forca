import random
import os

# 1. Configurações gerais e variáveis
lista_palavras = ['Bulgaria', 'Chequia', 'Chipre', 'Croacia', 'Dinamarca', 'Eslovaquia', 'Eslovenia', 'Espanha',
'Estonia', 'Finlandia', 'Franca', 'Grecia', 'Hungria', 'Irlanda', 'Italia', 'Letonia', 'Lituania', 'Luxemburgo',
'Malta', 'Paises Baixos', 'Polonia', 'Portugal', 'Romenia', 'Suecia']

palavra_secreta = random.choice(lista_palavras).upper()
# CORREÇÃO: Garante que espaços em nomes como "Paises Baixos" não bloqueiam o jogo
letras_descobertas = [letra if letra == ' ' else '_' for letra in palavra_secreta]
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

    # TESTE DE INVÁLIDOS
    try:
        entrada = input('Qual o seu palpite? Indique uma Letra: ').strip() 
        
        if not entrada:
            raise ValueError('Atenção! O campo não pode estar vazio!')
        
        if len(entrada) > 1:
            # Adicionado 'f' para a f-string funcionar
            raise ValueError(f'Atenção! Introduziste "{entrada}". Tens que indicar apenas UMA letra!')
            
        if not entrada.isalpha():
            # CORREÇÃO: T maiúsculo em TypeError
            raise TypeError(f'Atenção! O valor introduzido "{entrada}" não é uma letra válida!')

        # 4. Registo do palpite (Só acontece se não houver erro acima)
        palpite = entrada.upper()

        # 5. Validar repetição de letra
        if palpite in letras_descobertas or palpite in letras_erradas:
            mensagem = f'ATENÇÃO! A LETRA "{palpite}" JÁ FOI USADA!'
            continue

        # 6. Validar se foi uma letra correta ou incorreta
        if palpite in palavra_secreta:
            mensagem = f"BOA! ACERTASTE NA LETRA '{palpite}'!"
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == palpite:
                    letras_descobertas[i] = palpite
        else:
            mensagem = f"OH QUE PENA! ERRASTE. A LETRA '{palpite}' NÃO PERTENCE À PALAVRA!"
            letras_erradas.append(palpite)
            tentativas -= 1

    # CORREÇÃO: Bloco essencial para capturar os erros gerados pelo raise
    except (ValueError, TypeError) as erro:
        mensagem = str(erro)
        continue

# 7. Conclusão do jogo (Fora do While)
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