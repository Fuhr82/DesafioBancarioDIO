"""
    Desafio 1: Crie um programa que simule um caixa eletrônico, onde o usuário poderá depositar e sacar dinheiro, mantendo o controle do saldo da conta. 
    O programa deverá exibir o saldo da conta, permitir fazer depósitos e saques, e ao final exibir o extrato da conta. 
    O programa deverá ser executado até que o usuário escolha a opção de sair.
"""
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = [] # Lista para armazenar as operações
limite = 500 # Limite de saque por operação
numero_saques = 0
LIMITE_SAQUES = 3 # Limite de saques por dia

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: '))
        if valor <= 0:
            print('Valor inválido. Tente novamente.')
            continue
        saldo += valor
        extrato.append(f'Depósito de R$ {valor:.2f}')

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingido.')
            continue

        valor = float(input('Digite o valor do saque: '))
        if valor > saldo:
            print('Saldo insuficiente.')
        elif valor > limite:
            print(f'O valor máximo por saque é de R$ {limite:.2f}')
        elif valor <= 0:
            print('Valor inválido. Tente novamente.')
            continue
        else:
            saldo -= valor
            extrato.append(f'Saque de R$ {valor:.2f}')
            numero_saques += 1

    elif opcao == 'e':
        print(f'Saldo: R$ {saldo:.2f}')
        print('Extrato:')
        for operation in extrato:
            print(f'  {operation}')

    elif opcao == 'q':
        break

    else:
        print('Opção inválida. Tente novamente seleciononando uma das opcões acima.')
