import os
import random

nsorteado = random.randint(1,100)

while True:
    palpite = int(input('Digite um numero entre 1 e 100: '))

    if palpite == nsorteado:
        print(f'Parabens !! Você acertou Miseravi !!: {nsorteado}')
        break
    elif palpite<nsorteado:
        print('Digite um numero maior !!')
    else:
        print('Digite um numero menor')