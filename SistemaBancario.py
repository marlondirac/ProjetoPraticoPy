LIMITE = 3
VALOR_LIMITE = 500
extratos = []

cont = 0
total = 0

while True:
    print(" MENU ".center(50,"-"))
    print("[1] Depósito\n[2] Saque\n[3] Extrato\n[0] Sair")
    print("-".center(50,"-"))
    
    opcao = int(input("Digite a sua opção bancária:  "))

    if opcao == 0:
        print("Obrigado por usar nosso sistema!!")
        break

    elif opcao == 1:
        deposito = float(input("Valor a depositar: "))
        if deposito > 0:
            total+=deposito
            print(f"Foram depositados: R$ {deposito}\nTotal em conta: R$ {total}")
        else:
            print("Erro: somente é possível depositar valores positivos!")

        itemDep = f"[Depósito] - R$ {deposito}"
        extratos.append(itemDep)

    elif opcao == 2:
        
        saque = float(input("Valor a sacar: "))

        if cont>=LIMITE:
                print("Limite excedido")

        elif saque < total and saque <= VALOR_LIMITE:
            total-=saque
            print(f"Você sacou: R$ {saque}\nSaldo atual: R$ {total}")
            cont+=1
            itemSaque=f'[Saque] - R$ {saque}'
            extratos.append(itemSaque)

        else:
            print(f"Valor acima do seu saldo ou valor limite de R$ 500 excedido!")


    elif opcao ==3:
        if len(extratos) == 0:
            print("Sem movimentações bancárias")
        
        else:
            print(" Extrato ".center(50, "-"))
            print(extratos)
    
    else:
        print("Opção incorreta!")


    
