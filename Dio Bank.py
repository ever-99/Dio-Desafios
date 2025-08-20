menu = """
[d] Deposito
[s] sacar
[e] Extrato
[x] Sair

=> """

saldo = 0                 ## Saldo atual da conta
limite = 500              ## Limite máximo por operação de saque
extrato = ""              ## Histórico textual das movimentações
numero_saques = 0         ## Contador de saques realizados
LIMITE_SAQUES = 3         ## Máximo de saques permitidos

## Mantém o app rodando até o usuário escolher 'x'

while True:

    opcao = input(menu)   ## Lê a opção escolhida no menu (ex.: 'd', 's', 'e', 'x')

    ## Operação: Depósito
    if opcao == "d": 
        valor = float(input("Informe o valor do depósito: "))  ## Converte a entrada para número decimal (float)

        if valor > 0:                                   ## Validação: só permite depósito positivo
            saldo += valor                              ## Atualiza saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"    ## Registra a operação no extrato
            print(f"Operação realizada com sucesso! seu saldo atual é de {saldo}")
        else:
            print("Operação falhou! O valor informado é inválido.")  ## Valor zero/negativo não é permitido
        
    ## Operação: Saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))  ## Lê e converte o valor solicitado

        ## Regras de validação do saque
        excedeu_saldo = valor > saldo                       ## Regra 1: não pode sacar mais do que tem
        excedeu_limite = valor > limite                     ## Regra 2: não pode ultrapassar o limite por saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES     ## Regra 3: respeitar a quantidade máxima de saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")       ## Bloqueia por saldo insuficiente
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")    ## Bloqueia por limite por operação
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")    ## Bloqueia por atingir o teto de saques
        elif valor > 0:
            saldo -= valor                                   ## Debita o valor do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"            ## Registra no extrato
            numero_saques += 1                               ## Incrementa o contador de saques
            print(f"Operação realizada com sucesso! seu saldo atual é de {saldo}")
        else:
            print("Operação falhou! O valor informado é inválido.")    ## Valor zero/negativo é inválido
    
    ## Operação: Extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")                         
        print("Não foram realizadas movimentações." if not extrato else extrato)    ## Mostra histórico ou mensagem padrão
        print(f"\nSaldo: R$ {saldo:.2f}")                                           ## Exibe saldo atual formatado com 2 casas
        print("==========================================")                     

    ## Operação: Sair
    elif opcao == "x":
        break  ## Encerra o loop e finaliza o programa

    ## Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
