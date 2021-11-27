print(f'{" TABUADA ":=^50}')
while True:
    print('-' * 20)
    numero = int(input('Digite um número: [0 para sair] '))
    print('-'*20)
    if numero <= 0:
        break
    for n in range(1, 11, 1):
        print(f'{numero} x {n} = {numero * n}', end='\n')
print('Fim do programa!')
