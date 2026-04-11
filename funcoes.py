# lÓGICA DE APLICAÇÃO

from modelos import PessoaFisica, Deposito, Saque , Conta, Historico, Transacao

def filtrar_cliente(cpf, clientes):
     for cliente in clientes:
          if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
               return cliente
     return None

def recuperar_conta_cliente(cliente):
     if not cliente.contas:
          print("Cliente não possui contas.")
          return None
     return cliente.contas[0]  # Retorna a primeira conta do cliente

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    novo_cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = Conta.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")

def depositar(clientes):
     cpf = input("Digite o CPF do cliente: ")
     cliente = filtrar_cliente(cpf, clientes)
     if not cliente:
          print("Cliente não encontrado.")
          return
     conta = recuperar_conta_cliente(cliente)
     if not conta:
          return
     valor = float(input("Digite o valor a ser depositado: "))
     transacao = Deposito(valor)
     cliente.realizar_transacao(conta, transacao)
     
def sacar(clientes):
     cpf = input("Digite o CPF do cliente: ")
     cliente = filtrar_cliente(cpf, clientes)
     if not cliente:
          print("Cliente não encontrado.")
          return
     conta = recuperar_conta_cliente(cliente)
     if not conta:
          return
     valor = float(input("Digite o valor a ser sacado: "))
     transacao = Saque(valor)
     cliente.realizar_transacao(conta, transacao)
     print(f"Saque de R${valor:.2f} realizado com sucesso.")
     
     
#Função para consultar o saldo#
def consultar_saldo(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ SALDO ================")
    print(f"Cliente: {cliente.nome}")
    print(f"Conta: {conta._numero} | Agência: {conta._agencia}")
    print(f"\nSaldo Atual: R$ {conta.saldo:.2f}")
    print("=======================================")     
#Função para consultar o saldo#     

#Função para exibir o extrato#
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    # Buscando dados do cabeçalho através dos objetos
    print(f"Nome do Cliente: {cliente.nome}")
    print(f"Agência: {conta._agencia}  |  C/C: {conta._numero}")
    print("-----------------------------------------")
    
    transacoes = conta.historico.transacoes
    extrato = ""
    
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            # Aqui exibimos o Tipo, Valor e a Data/Hora que já salvamos no Historico
            extrato += f"\n[{transacao['data']}] {transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print("\n-----------------------------------------")
    print(f"Saldo Atual: R$ {conta.saldo:.2f}")
    print("==========================================")         



