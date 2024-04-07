from random import randint

def adivinha(escolha):
    aleatorio = randint(1, 10)
    #print(aleatorio)
    if escolha == 1:
        jogadas = 4
        while jogadas > 0:
            print('Você tem {} jogadas'.format(jogadas))
            numero = int(input('Tente adivinhar o número: '))
            if aleatorio > numero:
                print('Ops! Número tem que ser maior.')
                jogadas -= 1
            elif aleatorio < numero:
                print('Ops!Número tem que ser menor')
                jogadas -= 1
            elif aleatorio == numero:
                print('Você acertou parabêns!👏')
                jogadas = 0
            print()
    elif escolha == 2:
        jogadas = 2
        while jogadas > 0:
            print('Você tem {} jogadas'.format(jogadas))
            numero = int(input('Tente adivinhar o número: '))
            if aleatorio > numero:
                print('Ops! Número tem que ser maior.')
                jogadas -= 1
            elif aleatorio < numero:
                print('Ops!Número tem que ser menor')
                jogadas -= 1
            elif aleatorio == numero:
                print('Você acertou parabêns!👏')
                jogadas = 0
            print()
    elif escolha == 3:
        jogadas = 1
        while jogadas > 0:
            print('Você tem {} jogadas'.format(jogadas))
            numero = int(input('Tente adivinhar o número: '))
            if aleatorio > numero:
                print('Ops! Número tem que ser maior.')
                jogadas -= 1
            elif aleatorio < numero:
                print('Ops!Número tem que ser menor')
                jogadas -= 1
            elif aleatorio == numero:
                print('Você acertou parabêns!👏')
                jogadas = 0
            print()
    elif escolha == 4:
        print('Tente adivinhar o número gerao pelo computador.')
        print('As regras são básicas, no modo fácil você tem 4 chances de acertar o número.')
        print('No médio 2.')
        print('E no difícil 1.')

# Programa Principal
while True:
    try:
        print('-=' * 10, 'Adivinhe o número', '-=' * 10)
        print('Escolha o nível: ')
        print('1 - Fácil')
        print('2 - Médio')
        print('3 - Difícil')
        print('4 - Instruções')
        print('5 - Sair')
        escolha = int(input('>> '))
        if escolha == 5:
            break
        elif escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
            adivinha(escolha)
        else:
            print('Opção inválida')

    except ValueError:
        print('Somente número!')
