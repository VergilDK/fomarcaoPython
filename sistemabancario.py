saldo = 0.0
limite_saque_diario = 500.0
saques_diarios = 0
historico = []

while True:
    opcao = input("Digite a operação desejada (depósito, saque ou extrato): ")

    if opcao == "depósito":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            historico.append(("depósito", valor_deposito))
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == "saque":
        if saques_diarios < 3:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > 0 and valor_saque <= limite_saque_diario and saldo >= valor_saque:
                saldo -= valor_saque
                saques_diarios += 1
                historico.append(("saque", valor_saque))
            elif saldo < valor_saque:
                print("Saldo insuficiente. Tente novamente.")
            else:
                print("Valor inválido. Tente novamente.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "extrato":
        if len(historico) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for operacao, valor in historico:
                if operacao == "depósito":
                    print("Depósito: R$ {:.2f}".format(valor))
                elif operacao == "saque":
                    print("Saque: R$ {:.2f}".format(valor))
            print("Saldo atual: R$ {:.2f}".format(saldo))

    else:
        print("Operação inválida. Tente novamente.")
