print('='*35)
print(' Bem- vinde ao Número por Extenso! ')
print('='*35)
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'

while True:
    num = int(input('\nDigite um número entre 0 e 10: '))
    while num > 10:
        num = int(input('Digite \033[0;31mapenas\033[m números entre 0 e 10: '))
    for c in range(0,len(extenso)):
        if num  == c:
            print(f'O número {c} por extenso é "{extenso[c]}".')
    resposta = str(input('\nDeseja saber mais números?'))
    while resposta.strip().capitalize()[0] != 'N' and resposta.strip().capitalize()[0] != 'S':
        resposta = str(input('Não entendi...'))
    if resposta.strip().capitalize()[0] == 'N':
        print('\nObrigade por usar o programa!\nAté mais!')
        break