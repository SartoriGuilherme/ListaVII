import random

sorteio = random.randint(0, 100)
acertou = False

for i in range(1, 11):
    palpite = int(input('Informe o seu palpite: '))

    if palpite == sorteio:
        acertou = True
        print(f'Parabéns, você acertou em {i} tentativas!')
        break
    else:
        print('Errou! Tenta de novo doidão!')
    if sorteio > palpite:
        print('DICA: O número é maior!')
    else:
        print('DICA: O número é menor!')

if not acertou:
    print(f'O número sorteado foi {sorteio}')