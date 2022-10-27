from os import system
import textwrap


def menu():
    menu = """
    ====================MENU====================
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f'Depósito de R${valor:.2f} realizado.')
        extrato += (f'Depósito R${valor:.2f}\n')
    else:
        print('Operação falhou! Valor informado inválido.')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saque = numero_saques >= limite_saques

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
        print(f"Saques disponíveis:{limite_saques - numero_saques}")
        print(numero_saques)

    else:
        print('Operação falhou! Valor inválido.')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    system('cls')
    print('===============Extrato===============')
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo:\tR${saldo:.2f}')
    print('=====================================')
    input('Pressione qualquer tecla para continuar...')


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): \n=>')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n Já existe um usuário com esse CPF')
        return
    nome = input('Informe o nome completo: \n=>')
    data_nascimento = input('Informe a data de nascimento(dd-mm-aaaa):\n=>')
    endereco = input(
        'Informe o endereco (logradouro, nro - bairro - cidade/sigla estado)')

    usuarios.append({"nome": nome,
                     "data_nascimento": data_nascimento,
                     "cpf": cpf,
                     "endereco": endereco})
    print('Conta criada com sucesso!')


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário:\n=>')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuarios}
    print('Usuário não encontrado, fluxo de criação de conta encerrado.')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print('=' * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ''
    usuarios = []
    contas = []

    while True:
        opc = menu()

        if opc == "d":
            valor = float(input('Informe o valor do depósito:\n=>'))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opc == "s":
            valor = float(input('Informe o valor do saque:\n=>'))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES

            )

        elif opc == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opc == "nu":
            criar_usuario(usuarios)

        elif opc == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opc == "lc":
            listar_contas(contas)

        elif opc == "q":
            print('Sessão encerrada')

            break

        else:
            print('Operação inválida\n')


main()
