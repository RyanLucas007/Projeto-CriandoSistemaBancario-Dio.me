enu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saque = 0
limite_de_saque = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que você deseja depositar. "))

        if valor > 0:                                                                
            saldo += valor      #saldo igual mais valor              
            extrato += f"Depósito: R$ {valor:.2f}\n"        #Extrato igual mais deposito, valor etc..

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saque >= limite_de_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : R$ {valor:.2f}\n"
            numero_de_saque += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: RS {saldo:.2f}")
        print("===============================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")