# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

#Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
#Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

#Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
#Todos os depósitosmdevem ser armazenados em uma variável e exibidos na operação de extrato.

#O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
#Caso o usuário não tenhamsaldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
#Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

#DECLARAÇÃO DE VARIÁVEIS

#DICIONÁRIOS E LISTAS
clientes={
    12345678900:{"nome":"Cliente 1", "conta-corrente":"000001", "conta-poupança":"100000"},
}

#STRINGS
extrato=f"""
"""
LIMITE_DIÁRIO="O valor limite por saque é de R$ 500,00, por favor, digite outro valor até R$ 500,00 ou [0] para sair."
SAQUE_ZERADO="Valor inválido, por favor, escolha outro valor ou tecle [0] para sair."
AGRADECIMENTO="Obrigado por utilizar o nosso banco."
saldo_indisponível=" "

#FLOAT E INT
LIMITE_SAQUE = 500.00
saldo_disponível=0.00
depósito= 0.00
opção_escolhida=0
saque= 0.00
quantidade_de_saques= 0
cpf=0

#VARIÁVEIS CONDICIONAIS
i=0
cliente=1
x_while=1
x_menu=0

#MENSAGENS PRINCIPAIS
inicio= f"""
Olá, seja bem-vindo(a) ao nosso banco, para iniciar seu atendimento, por favor, escolha uma opção:
[0] Quero acessar minha conta
[1] Sou cliente mas quero abrir uma nova conta
[2] Não sou cliente e quero abrir uma conta
"""

boas_vindas= f"""
Por favor, digite um número para começar o seu atendimento
[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[0] SAIR
*********************************************************
"""

def menu_principal(): #executa o menu principal com as opções de sacar, depositar e extrato
    global x_while
    while x_while!=0: #loop que executa o menu principal
        print(boas_vindas)
        opção_escolhida=int(input())
        if opção_escolhida==0:
            print(AGRADECIMENTO)
            x_while=0
        elif opção_escolhida==1 or opção_escolhida==2 or opção_escolhida==3:
            if (opção_escolhida==1):
                depositar()
            if (opção_escolhida==2):
                sacar()
            if (opção_escolhida==3):
                extract()               
        else:
            print("Opção inválida, por favor escolha uma das opções do menu principal")
            x_while +=1         

def buscar_cpf(): #executa a busca do cpf para identificar o cliente
    global i, cliente
    for cliente in clientes:
        if cpf == clientes[i]:
            menu_principal()
        else:
            i=int(i)
            cliente=cliente+1

def adicionar_conta(): #adiciona uma conta a um CPF que já tenha uma conta cadastrada
    while cpf != usuários[i]:
        i=i+1
    else:
        nova_conta = contas[-1]
        nova_conta = nova_conta+1
        contas.append(nova_conta)
        nova_conta=str(nova_conta)
        usuários[cpf][nova_conta]="0.00"
        print(usuários["nome"], ", sua conta criada com sucesso!")
        menu_principal()

def criar_conta(): #cria uma nova conta (nova chave para o dicionário usuários)
    print("Por favor, digite seu cpf")
    cpf=(input)
    print("Por favor, digite seu nome")
    nome=input()
    nova_conta = contas[-1]
    nova_conta = nova_conta+1
    contas.append(nova_conta)
    nova_conta=str(nova_conta)
    novos_dados= {cpf : {"nome":nome, nova_conta:"0.00"}}
    usuários.update(novos_dados)
    print(usuários["nome"], ", sua conta criada com sucesso!")
    menu_principal()

def retorno(): #função que executa o retorno ao menu principal
    global x_menu
    global x_while
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

def depositar(): #função que executa a opção de depositar
    global depósito
    global x_menu
    global x_while
    global saldo_disponível
    global extrato
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
            saldo_disponível += depósito
            extrato = f"{extrato} Depósito realizado no valor de R$ {depósito: .2f} \n"
            print("Depósito realizado com sucesso, deseja realizar mais alguma operação?")
            retorno()
    else:
        saldo_disponível += depósito
        extrato = f"{extrato} Depósito realizado no valor de R$ {depósito: .2f} \n"
        print("Depósito realizado com sucesso, deseja realizar mais alguma operação?")
        retorno()

def sacar(): #função que executa a opção de sacar
    global saque
    global x_menu
    global x_while
    global quantidade_de_saques
    global LIMITE_SAQUE
    global saldo_disponível
    global extrato
    global saldo_indisponível
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
                retorno()
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
                        extrato = f"{extrato} Saque realizado no valor de R$ {saque: .2f} \n"
                        print("Saque realizado com sucesso, deseja realizar mais alguma operação?")
                        retorno()
                    else:
                        saldo_indisponível=f"Você não tem saldo suficiente para esse saque, por favor, escolha um valor até R$ {saldo_disponível: .2f} ou digite [0] para sair."
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
            retorno()
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
                        extrato = f"{extrato} Saque realizado no valor de R$ {saque: .2f} \n"
                        print("Saque realizado com sucesso, deseja realizar mais alguma operação?")
                        retorno()
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
                    extrato = f"{extrato} Saque realizado no valor de R$ {saque: .2f} \n"
                    print("Saque realizado com sucesso, deseja realizar mais alguma operação?")
                    retorno()
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

def extract(): #função que executa a opção de exibir o extrato das transações
    global extrato
    global saldo_disponível
    if len(extrato)==1:
        print("Não foram realizadas movimentações")
        retorno()
    else:
        print(extrato)
        saldo_atual=f"Seu saldo atual é de R$ {saldo_disponível: .2f}"
        print(saldo_atual)
        retorno()  

print(inicio)
opção_inicial=int(input())
while opção_inicial ==0 or opção_inicial ==1 or opção_inicial==2:
    if opção_inicial==0:
        print("Por favor, digite o número do seu CPF")
        cpf=int(input())
        #colocar um if para verificar se a chave existe no dicionário clientes
        #se existir executa o menu principal, senão pede para o cliente redigitar o cpf
        menu_principal()
    elif opção_inicial==1:
        adicionar_conta()
    elif opção_inicial==2:
        criar_conta()
else:
    print("Opção não disponível, por favor, escolha uma das opções.")
    print(inicio)
    opção_inicial=int(input())