# trabalhofinal_algoritmos
 Algoritmos e Programação

##  Identificação do Projeto
* *Estudante:* Larissa Karoline
* *Disciplina:* Algoritmos e Programação
* *Título do Projeto:* Sistema de Atendimento e Pedidos em Python

##  Descrição do Programa
Este programa foi desenvolvido como avaliação prática para integrar os principais conceitos estudados na disciplina de Algoritmos e Programação. Trata-se de um sistema automatizado para substituição do registro manual de pedidos de uma lanchonete, permitindo a seleção de produtos através de um cardápio interativo, controle de quantidade, cálculo automático de subtotal, aplicação progressiva de descontos e escolha validada da forma de pagamento.

## Principais Funcionalidades Implementadas
* *Identificação Inicial:* Coleta do nome do cliente no início do atendimento.
* *Menu Interativo:* Exibição dinâmica de 5 opções de produtos e valores correspondentes.
* *Validação de Dados:* Mecanismos que impedem a inserção de códigos inexistentes ou quantidades inválidas (menores ou iguais a zero), evitando erros de cálculo.
* *Regra Progressiva de Desconto:* 
  * Compras abaixo de R$ 50,00: Sem desconto.
  * Compras de R$ 50,00 até R$ 99,99: 5% de desconto.
  * Compras a partir de R$ 100,00: 10% de desconto.
* *Gerenciamento de Fluxo:* Organização modular do código utilizando funções com responsabilidades bem definidas, sem o uso de estruturas de dados avançadas não estudadas (como listas ou dicionários).

## Instruções para Execução
1. Certifique-se de possuir o *Python 3.10 ou superior* instalado em sua máquina.
2. Abra o terminal ou prompt de comando na pasta onde os arquivos foram baixados.
3. Execute o programa principal utilizando o seguinte comando:
   bash
   python sistema_pedidos.py
   
4. Siga as instruções textuais apresentadas no terminal para realizar o pedido.
