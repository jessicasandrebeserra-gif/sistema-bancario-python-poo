# INTERFACE DE USUÁRIO

import funcoes as f

def menu():
    text = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [cs]\tConsultar Saldo
    [nc]\tNova Conta
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(text)

def main():
    # Estas listas guardam OBJETOS, não apenas textos
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            # Chama a função depositar que está lá no funcoes.py
            f.depositar(clientes)

        elif opcao == "s":
            f.sacar(clientes)

        elif opcao == "e":
            f.exibir_extrato(clientes)
       
        elif opcao == "cs":
            f.consultar_saldo(clientes)     

        elif opcao == "nu":
            # cria o usuário para ele existir na lista
            f.criar_cliente(clientes)

        elif opcao == "nc":
            # cria a conta vinculada ao CPF do usuário
            numero_conta = len(contas) + 1
            f.criar_conta(numero_conta, clientes, contas)

        elif opcao == "q":
            print("Encerrando sistema...")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main() #Só vai executar se eu chamar o main.py diretamente pelo terminal (python main.py)