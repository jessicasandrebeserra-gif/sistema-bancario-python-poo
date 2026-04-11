# LOGÍCA DE NEGÓCIO


from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
     def __init__(self, endereco):
          self.endereco = endereco
          self.contas = []
          
     def realizar_transacao(self, conta, transacao):
          transacao.registrar(conta)
          
     def adicionar_conta(self, conta):
          self.contas.append(conta)
          
class PessoaFisica(Cliente):
     def __init__ (self, nome, data_nascimento, cpf, endereco):
          super().__init__(endereco)
          self.nome = nome
          self.data_nascimento = data_nascimento
          self.cpf = cpf
          
class Conta:
     def __init__(self, numero, cliente):
          self._numero = numero
          self._agencia = "0001"
          self._cliente = cliente
          self._saldo = 0
          self._historico = Historico()
          
     @classmethod
     def nova_conta(cls, cliente, numero):
          return cls(numero, cliente)
          
     @property
     def saldo(self):
          return self._saldo
          
     @property
     def historico(self):
          return self._historico
          
     def sacar(self, valor):
          if valor > self._saldo:
               print("Saldo insuficiente.")
               return False
          if valor > 0:
               self._saldo -= valor
               return True
          return False
     
     def depositar(self, valor):
          if valor > 0:
               self._saldo += valor
               return True
          return False
     
class Historico:
     def __init__(self):
          self._transacoes = []         
     @property
     def transacoes(self):
          return self._transacoes
     
     def adicionar_transacao(self, transacao):
          self._transacoes.append({
               "tipo": transacao.__class__.__name__,
               "valor": transacao.valor,
               "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          })             
          
class Transacao(ABC):
     @property
     @abstractmethod
     def valor(self): pass
          
     @abstractmethod
     def registrar(self, conta): pass
     
class Saque(Transacao):
     def __init__(self, valor):
          self._valor = valor
          
     @property
     def valor(self):
          return self._valor
     
     def registrar(self, conta):
          if conta.sacar(self.valor):
               conta.historico.adicionar_transacao(self)
               print(f"Saque de R${self.valor} realizado com sucesso.")
          else:
               print("Falha ao realizar o saque.")
               
class Deposito(Transacao):
     def __init__(self, valor):
          self._valor = valor
     
     @property
     def valor(self):
          return self._valor
                         
     def registrar(self, conta):
          if conta.depositar(self.valor):
               conta.historico.adicionar_transacao(self)
               print(f"Depósito de R${self.valor} realizado com sucesso.")
          else:
               print("Falha ao realizar o depósito.")

          
            
     