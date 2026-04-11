# Sistema Bancário com Python e POO 
Desafio de sistema bancário utilizando Programação Orientada a Objetos em Python.

Este projeto é uma implementação de um sistema bancário modularizado, desenvolvido para praticar conceitos de **Programação Orientada a Objetos (POO)** e organização de código em Python.

##  Tecnologias Utilizadas
* **Python 3.10+**
* **Biblioteca ABC:** Para criação de classes abstratas.
* **DateTime:** Para registro de logs no histórico.

## Estrutura do Projeto
O código foi dividido em três módulos principais para seguir os princípios de separação de responsabilidades:

1.  **`modelos.py`**: Contém as classes base (Cliente, Conta, Histórico) e a lógica de transações (Saque, Depósito) utilizando herança e polimorfismo.
2.  **`funcoes.py`**: Gerencia a lógica de aplicação, como busca de clientes e orquestração das operações bancárias.
3.  **`main.py`**: Ponto de entrada do sistema que gerencia a interface de usuário (menu).

## Execução
1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/sistema-bancario-python-poo.git](https://github.com/SEU_USUARIO/sistema-bancario-python-poo.git)
