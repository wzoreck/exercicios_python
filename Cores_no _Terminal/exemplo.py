# \033[estilo;textoCor;corFundo m

'''
------- alguns códigos ---------

estilo:

0 - nenhum
1 - negrito
4 - sublinhado
7 - inverte config

cor texto:

30 a 37

30 (branco)
31 (vermelho)
32 (verde)
33 (amarelo)
34 (azul)
35 (roxo)
36 (azul claro)
37 (cinza)

cor fundo:

40 a 47 onde as cores seguem a oredem anterior

'''

print('\033[7;31m Olá Mundo \033[m') # o ultimo é para tirar a formatação que continua até o final da linha do terminal

print('\033[1;36m Olá Mundo \033[m')
