# jogo-da-forca

Objetivo do jogo:
  O jogador deve descobrir a palavra secreta, adivinhando uma letra de cada vez, antes que se esgote o número máximo de tentativas disponíveis.

Regras principais:
  i. a palavra secreta é apresentada inicialmente apenas com traços (_), que representam o número total de letras;
  ii. cada rodada, o jogador insere uma letra;
  iii. se a letra existir, esta é revelada;
  iv. se a letra não existir, o jogador perde a tentativa e o contador de erros aumenta.

Condições para a vitória ou derrota:
  Vitória: o jogador descobre a palavra secreta antes de atingir o limite máximo de erros;
  Derrota: o jogador não consegue descobrir a palavra secreta antes de atingir o limite máixmo de erros.

Limitações e inputs:
  Número máximo de erros: 6
  Inputs: letras de A a Z
  Letras: o jogo deve ser case insensitive, para permitir o tratamento de maiúsculas e minúsculas
