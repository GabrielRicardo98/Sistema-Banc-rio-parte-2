def transferir():
    """Realiza a operação de transferência."""
    global saldo, extrato
    conta_destino = input("Digite o número da conta do destinatário: ")
    
    while True:
        try:
            valor_transferencia = float(input("Digite o valor a transferir: R$ "))
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    if valor_transferencia <= saldo:
        saldo -= valor_transferencia
        agora = datetime.datetime.now()
        extrato.append({
            "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
            "tipo": "Transferência",
            "valor": -valor_transferencia,
            "destino": conta_destino
        })
        print(f"Transferência de R$ {valor_transferencia:.2f} realizada com sucesso para a conta {conta_destino}.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente para realizar a transferência.")
