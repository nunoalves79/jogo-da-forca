import random

# 1. Lista de palavras a escolher aleatoriamente
lista_palavras = ['Bulgaria', 'Chequia', 'Chipre', 'Croacia', 'Dinamarca', 'Eslovaquia', 'Eslovenia', 'Espanha',
'Estonia', 'Finlandia', 'Franca', 'Grecia', 'Hungria', 'Irlanda', 'Italia', 'Letonia', 'Lituania', 'Luxemburgo',
'Malta', 'Paises Baixos', 'Polonia', 'Portugal', 'Romenia', 'Suecia']

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
