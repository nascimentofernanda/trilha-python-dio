# Criar um sistema bancário com as operações: sacar, depositar
#e visualizar extrato.

#Fomos contratados por um grande banco para desenvolver o
#seu novo sistema. Esse banco deseja modernizar suas
#operações e para isso escolheu a linguagem Python. Para a
#primeira versão do sistema devemos implementar apenas 3
#operações: depósito, saque e extrato.

#Deve ser possível depositar valores positivos para a minha
#conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
#dessa forma não precisamos nos preocupar em identificar qual
#é o número da agência e conta bancária. Todos os depósitos
#devem ser armazenados em uma variável e exibidos na
#operação de extrato.

#O sistema deve permitir realizar 3 saques diários com limite
#máximo de R$ 500,00 por saque. Caso o usuário não tenha
#saldo em conta, o sistema deve exibir uma mensagem
#informando que não será possível sacar o dinheiro por falta de
#saldo. Todos os saques devem ser armazenados em uma
#variável e exibidos na operação de extrato.

#Essa operação deve listar todos os depósitos e saques
#realizados na conta. No fim da listagem deve ser exibido o
#saldo atual da conta. Se o extrato estiver em branco, exibir a
#mensagem: Não foram realizadas movimentações.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
#exemplo:
#1500.45 = R$ 1500.45

#STRINGS
extrato=f"""
"""
LIMITE_DIÁRIO="O valor limite por saque é de R$ 500,00, por favor, digite outro valor até R$ 500,00 ou [0] para sair."
SAQUE_ZERADO="Valor inválido, por favor, escolha outro valor ou tecle [0] para sair."
AGRADECIMENTO="Obrigado por utilizar o nosso banco."
saldo_indisponível=" "

#float e int
LIMITE_SAQUE = 500.00
saldo_disponível= 0.00
depósito= 0.00
opção_escolhida=0
saque= 0.00
quantidade_de_saques= 0

#VARIÁVEIS CONDICIONAIS
x_while=1
x_menu=0


boas_vindas= f"""
*********Olá, seja bem-vindo ao nosso banco**************
Por favor, digite um número para começar o seu atendimento
[1]DEPÓSITO
[2]SAQUE
[3]EXTRATO
[0]SAIR
*********************************************************
"""

while x_while!=0:
    print(boas_vindas)
    opção_escolhida=int(input())
    if opção_escolhida==0:
        print(AGRADECIMENTO)
        x_while=0
    elif opção_escolhida==1 or opção_escolhida==2 or opção_escolhida==3:
        if (opção_escolhida==1):
            print("Digite o valor que deseja depositar: ")
            depósito=float(input())
            x_menu=int(depósito)
            if depósito==0:
                print("Valor inválido, por favor digite outro valor ou tecle [0] para sair")
                depósito=float(input())
                x_menu=int(depósito)
                if x_menu==0:
                    print(AGRADECIMENTO)
                    x_while=0
                else:
                    saldo_disponível +=depósito
                    extrato = f"{extrato} Depósito realizado no valor de R$ {depósito} \n"
                    print("Depósito realizado com sucesso, deseja realizar mais alguma operação?")
                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                    x_menu=int(input())
                    while x_menu !=0 and x_menu !=4:
                        print("Opção inválida")
                        print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                        x_menu=int(input())
                    else:
                        if x_menu==0:
                            print(AGRADECIMENTO)
                            x_while=0
                        else:
                            x_while +=1
            else:
                saldo_disponível +=depósito
                extrato = f"{extrato} Depósito realizado no valor de R$ {depósito} \n"
                print("Depósito realizado com sucesso, deseja realizar mais alguma operação?")
                print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                x_menu=int(input())
                while x_menu !=0 and x_menu !=4:
                    print("Opção inválida")
                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                    x_menu=int(input())
                else:
                    if x_menu==0:
                        print(AGRADECIMENTO)
                        x_while=0
                    else:
                        x_while +=1
        if (opção_escolhida==2):
            print("Digite o valor que deseja sacar: ")
            saque=float(input())
            x_menu=int(saque)
            if int(saque)==0:
                print(SAQUE_ZERADO)
                saque=float(input())
                x_menu=int(saque)
                if x_menu==0:
                    print(AGRADECIMENTO)
                    x_while=0
                else:
                    if quantidade_de_saques>=3:
                        print("Você excedeu a quantidade diária de saques, por favor, volte amanhã.")
                        print("Deseja realizar mais alguma operação?")
                        print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                        x_menu=int(input())
                        while x_menu !=0 and x_menu !=4:
                            print("Opção inválida")
                            print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                            x_menu=int(input())
                        else:
                            if x_menu==0:
                                print(AGRADECIMENTO)
                                x_while=0
                            else:
                                x_while +=1
                    else:
                        if int(saque)>LIMITE_SAQUE:
                                while int(saque)>LIMITE_SAQUE:
                                    print(LIMITE_DIÁRIO)
                                    saque=float(input())
                                    x_menu=int(saque)
                                    if x_menu==0:
                                        print(AGRADECIMENTO)
                                        x_while=0
                                    else:
                                        x_while +=1
                        else:
                            if int(saque)<=int(saldo_disponível) :
                                quantidade_de_saques +=1
                                saldo_disponível -=saque
                                extrato = f"{extrato} Saque realizado no valor de R$ {saque} \n"
                                print("Saque realizado com sucesso, deseja realizar mais alguma operação?")
                                print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                                x_menu=int(input())
                                while x_menu !=0 and x_menu !=4:
                                    print("Opção inválida")
                                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                                    x_menu=int(input())
                                else:
                                    if x_menu==0:
                                        print(AGRADECIMENTO)
                                        x_while=0
                                    else:
                                        x_while +=1
                            else:
                                saldo_indisponível=f"Você não tem saldo suficiente para esse saque, por favor, escolha um valor até R$ {saldo_disponível},00 ou digite [0] para sair."
                                print(saldo_indisponível)
                                saque=float(input())
                                x_menu=int(saque)
                                if x_menu==0:
                                    print(AGRADECIMENTO)
                                    x_while=0
                                else:
                                    x_while +=1
            else:
                if quantidade_de_saques>=3:
                    print("Você excedeu a quantidade diária de saques, por favor, volte amanhã.")
                    print("Deseja realizar mais alguma operação?")
                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                    x_menu=int(input())
                    while x_menu !=0 and x_menu !=4:
                        print("Opção inválida")
                        print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                        x_menu=int(input())
                    else:
                        if x_menu==0:
                            print(AGRADECIMENTO)
                            x_while=0
                        else:
                            x_while +=1
                else:
                    if int(saque)> int(LIMITE_SAQUE):
                        while int(saque)> int(LIMITE_SAQUE):
                            print(LIMITE_DIÁRIO)
                            saque=float(input())
                            x_menu=int(saque)
                            if x_menu==0:
                                print(AGRADECIMENTO)
                                x_while=0
                            else:
                                x_while +=1
                        else:
                            if int(saque)<=int(saldo_disponível) :
                                quantidade_de_saques +=1
                                saldo_disponível -=saque
                                extrato = f"{extrato} Saque realizado no valor de R$ {saque} \n"
                                print("Saque realizado com sucesso, deseja realizar mais alguma operação?")
                                print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                                x_menu=int(input())
                                while x_menu !=0 and x_menu !=4:
                                    print("Opção inválida")
                                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                                    x_menu=int(input())
                                else:
                                    if x_menu==0:
                                        print(AGRADECIMENTO)
                                        x_while=0
                                    else:
                                        x_while +=1
                            else:
                                saldo_indisponível=f"Você não tem saldo suficiente para esse saque, por favor, escolha um valor até R$ {saldo_disponível},00 ou digite [0] para sair."
                                print(saldo_indisponível)
                                saque=float(input())
                                x_menu=int(saque)
                                if x_menu==0:
                                    print(AGRADECIMENTO)
                                    x_while=0
                                else:
                                    x_while +=1
                    else:
                        if int(saque) <=int(saldo_disponível) :
                            quantidade_de_saques +=1
                            saldo_disponível -=saque
                            extrato = f"{extrato} Saque realizado no valor de R$ {saque} \n"
                            print("Saque realizado com sucesso, deseja realizar mais alguma operação?")
                            print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                            x_menu=int(input())
                            while x_menu !=0 and x_menu !=4:
                                print("Opção inválida")
                                print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                                x_menu=int(input())
                            else:
                                if x_menu==0:
                                    print(AGRADECIMENTO)
                                    x_while=0
                                else:
                                    x_while +=1
                        else:
                            saldo_indisponível=f"Você não tem saldo suficiente para esse saque, por favor, escolha um valor até R$ {saldo_disponível},00 ou digite [0] para sair."
                            print(saldo_indisponível)
                            saque=float(input())
                            x_menu=int(saque)
                            if x_menu==0:
                                print(AGRADECIMENTO)
                                x_while=0
                            else:
                                x_while +=1
        if (opção_escolhida==3):
            if len(extrato)==1:
                print("Não foram realizadas movimentações")
                print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                x_menu=int(input())
                while x_menu !=0 and x_menu !=4:
                    print("Opção inválida")
                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                    x_menu=int(input())
                else:
                    if x_menu==0:
                        print(AGRADECIMENTO)
                        x_while=0
                    else:
                        x_while +=1
            else:
                print(extrato)
                saldo_atual=f"Seu saldo atual é de R$ {saldo_disponível}"
                print(saldo_atual)
                print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                x_menu=int(input())
                while x_menu !=0 and x_menu !=4:
                    print("Opção inválida")
                    print("Digite [4] para retornar ao menu principal ou [0] para sair.")
                    x_menu=int(input())
                else:
                    if x_menu==0:
                        print(AGRADECIMENTO)
                        x_while=0
                    else:
                        x_while +=1                
    else:
        print("Opção inválida, por favor escolha uma das opções do menu principal")
        x_while +=1         