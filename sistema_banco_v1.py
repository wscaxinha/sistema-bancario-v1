menu = """
****** Sistema Bancário - V1 ******

    [d] - Deposito
    [s] - Sacar
    [e] - Extrato    
    [q] - Sair

->  Informe a opção: """

saldo = numeros_saques = lim_diario_saque = qtde_dep = total_saque = total_deposito = 0
valor_limite_saque = 500
extrato = " Extrato "
transacao_dep = ""
transacao_saque = ""
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)     
# Lógica para realizar o depósito no sistema ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if opcao == "d":   

        deposito = float(input("Digite o valor do depósito R$: "))

        if deposito > 0:
            transacao_dep += f"deposito: R$ {deposito:.2f}\n"           
            total_deposito += deposito
            saldo += deposito
            qtde_dep += 1
            print(f"Depósito de R$: {deposito} realizado com sucesso!")
        else:
            print("Digite um valor valido, positivo")
# Lógica para realizar o saque no sistema ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif opcao == "s":
        
        if lim_diario_saque >= LIMITE_SAQUES:
            print("Atingiu o limite diário de saque.")                
            break

        saque = float(input("Digite o valor do saque R$: ")) 

        if saque > 0:
            if saque > valor_limite_saque:
                print("Excedeu o valor máximo para saque.")    

            elif saque > saldo:           
                print("Não será possível sacar o dinheiro por falta de saldo.")  
            else:
                saldo -= saque
                lim_diario_saque += 1
                total_saque += saque
                transacao_saque += f"Saque:    R$ {saque:.2f}\n"     
                print(f"Saque de R$ {saque} realizado com sucesso!")
        else:
            print("Digite um valor valido, positivo")
# Lógica para o exibir o extrato ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif opcao == "e":
        if not (transacao_dep and transacao_saque):   
            print(extrato.center(40,"*"))    
            print()                  
            print("Não foram realizadas movimentaçãoes")      
        else:            
            print(extrato.center(40,"*")) 
            print()
            print(f"Qtde de depositos: {qtde_dep} depositos.")
            print(f"Qtde de saques: {lim_diario_saque} saques.")
            print(transacao_dep,end="")
            print(transacao_saque)
            print(f"(+)Total Depositado R$ {total_deposito:.2f}")
            print(f"(-)Total sacado R$ {total_saque:.2f}")
            print(f"Saldo disponível R$ {saldo:.2f}") 
# Exibir mensagem de encerramento das operações ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
    elif opcao == "q":
        print("Obrigado por utilizar nosso Banco!")
        break
    else:
        print("Operação inválida, Por favor selecione a operação desejada.")