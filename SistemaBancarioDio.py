from os import system
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ''

while True:
    opc = input("""==========MENU==========
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair\n""")

    if opc == "d":
        valor = float(input('Informe o valor do depósito:'))

        if valor > 0:
            saldo += valor
            print(f'Depósito de R${valor:.2f} realizado.')
            extrato += (f'Depósito R${valor:.2f}\n')
        else:
            print('Operação falhou! Valor informado inválido.')

    elif opc == "s":
        valor = float(input('Informe o valor do saque:'))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Saldo insuficiente')

        elif excedeu_limite:
            print('Operação falhou! Valor do saque maior que o limite.')

        elif excedeu_saque:
            print('Operação falhou! Limite de saques diários excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += (f'Saque R$ {valor:.2f}\n')
            numero_saques += 1
            print(f'Saque de R${valor:.2f} realizado.')
            print(f"Saques disponíveis:{LIMITE_SAQUES - numero_saques}")\

        else:
            print('Operação falhou! Valor inválido.')
    elif opc == "e":
        system('cls')
        print(f"""
\n----------Extrato----------
{'Não foram realizas movimentações.' if not extrato else extrato}
---------------------------
Saldo: R${saldo:.2f}
""")
        input('Pressione qualquer tecla para continuar...')

    elif opc == "q":
        print('Sessão encerrada')
        break

    else:
        print('Operação inválida\n')
