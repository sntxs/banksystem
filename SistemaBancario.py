valorAtual = 5455

for _ in range(3):  # Aqui você pode especificar o número de iterações
    print(
        f"""
        ======================================
            Olá, seja bem vindo ao Banco
        ====================================== 
        """
    )

    print("Qual operação você gostaria de fazer?")
    opcao = input(
        """
        ======================================
            1 - Depositar
            2 - Sacar
            3 - Ver Saldo
        ====================================== 
        """
    )

    if opcao == '3':
        print(f"O saldo de sua conta é de: R${valorAtual}")

    elif opcao == '1':
        deposito = float(input("Quanto você gostaria de depositar: "))
        valorTotal = valorAtual + deposito
        print(f"Com o valor do depósito de R$ {deposito}, o valor atual da sua conta é de: R$ {valorTotal}")
        valorAtual = valorTotal

    elif opcao == '2':
        saque = float(input("Quanto você gostaria de sacar: "))
        valorTotal = valorAtual - saque
        if valorTotal >= 0:
            print(f"Com o valor de saque de R$ {saque}, o valor atual da sua conta é de: R$ {valorTotal}")
            valorAtual = valorTotal
        else:
            print("Saldo insuficiente para realizar o saque.")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
