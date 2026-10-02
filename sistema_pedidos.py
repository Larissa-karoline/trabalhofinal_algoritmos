#---FUNÇÔES DO SISTEMA DE PEDIDOS---#

def exibir_cardapio():
    """Apresenta os 5 produtos disponíveis na lanchonete."""
    print("\n" + "=" * 30)
    print("    CARDÀPIO DA LANCHONETE    ")
    print("="*30)
    print("Codigo  |  Produto       |  Preço")
    print(" 1      |  Hambúrguer    | R$ 15.00")
    print(" 2      |  Batata Frita  | R$10.00")
    print(" 3      |  Refrigerante  | R$ 6.00")
    print(" 4      |  Suco Natural  | R$ 8.00")
    print(" 5      |  Combo do Dia  | R$ 29.90")
    print("="*30)

def calcular_desconto(total_compra):
    """Calcula o percentual e o valor do desconto com base no total."""
    if total_compra < 50.00:
        percentual = 0
    elif total_compra < 100.00:
        percentual = 5
    else:
        percentual = 10
    
    valor_desconto = total_compra * (percentual / 100)
    return percentual, valor_desconto

def obter_forma_pagamento(opcao):
    """Valida e retorna o nome da forma de pagamento escolhida pelo usuário."""
    match opcao:
        case 1: return "Dinheiro"
        case 2: return "Pix"
        case 3: return "Cartão de Crédito"
        case _:return "Opção inválida. Por favor, escolha uma forma de pagamento válida."


#---FLUXO PRINCIPAL DO PROGRAMA---#
def main():
    print("Bem vindo ao tótem de pedidos da lanchonete!")
    nome_cliente = input("Por favor, digite como deseja ser chamado: ").strip()

    total_acumulado = 0.0
    continuar = "s"

    # Laço de repetição para permitir varios pedidos
    while continuar.lower() == "s":
        exibir_cardapio()

        try:
            codigo = int(input("Digite o codigo do produto desejado:"))

        except ValueError:
            print("Erro: Por favor, digite um número válido para o código do produto.")
            continue

        # Identificação do produto e definição do preço diretamente no fluxo do codigo
        match codigo:
            case 1:
                preco_unitario = 15.00
                produto = "Hambúrguer"
            case 2:
                preco_unitario = 10.00
                produto = "Batata Frita"
            case 3:
                preco_unitario = 6.00
                produto = "Refrigerante"
            case 4:
                preco_unitario = 8.00
                produto = "Suco Natural"
            case 5:
                preco_unitario = 29.90
                produto = "Combo do Dia"
            case _:
                # Caso digite um codigo fora de 1 a 5, o programa informa que o código é inválido e reinicia o loop
                print("Código inválido! Por favor escolha entre os códigos disponíveis no cardápio.")
                continue #Pula o restante do laço e volta para o início do while

        try:
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que 0. Por favor, tente novamente.")
                continue
        except ValueError:
            print("Erro: Por favor, digite um número válido para a quantidade.")
            continue    

        #Calculo do subtotal e acumulação do total
        subtotal = preco_unitario * quantidade
        total_acumulado += subtotal
        print(f"Subtotal do item: R$ {subtotal:.2f} | Total acumulado: R$ {total_acumulado:.2f}")

        #Pergunta se deseja continuar comprando
        continuar = input("Deseja continuar comprando? (s/n): ").strip()
        while continuar.lower() not in ["s", "n"]:
            continuar = input("Opção inválida. Por favor, digite 's' para sim ou 'n' para não: ").strip()

        #Se o cliente não comprou nada, encerra o programa
        if total_acumulado == 0:
            print("\nNenhum pedido foi realizado. Atendimento finalizzado. Volte sempre!")
            return  

        #Processamento do desconto
        pct_desconto, valor_desconto = calcular_desconto(total_acumulado)
        total_com_desconto = total_acumulado - valor_desconto

        #Selecao e validação da forma de pagamento
        print("\n---Forma de Pagamento---")
        print("1 - Dinheiro")
        print("2 - Pix")
        print("3 - Cartão de Crédito")

        forma_texto = "invalido"
        while forma_texto == "invalido":
            try:
                opcao_pagamento = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))
                forma_texto = obter_forma_pagamento(opcao_pagamento)
                if forma_texto == "invalido":
                    print("Opção inválida. Por favor, escolha uma forma de pagamento válida, entre 1, 2 ou 3.")
            except ValueError:
                print("Erro: Digite um número válido para a forma de pagamento.")


    #---Resumo do Pedido---#
    print("\n" + "="*40)
    print("      RESUMO DO PEDIDO       ")
    print("="*40)
    print(f"Cliente: {nome_cliente}")
    print(f"Valor Original: R$ {total_acumulado:.2f}")
    print(f"Desconto aplicado: {pct_desconto:.0f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor final a pagar: R$ {total_com_desconto:.2f}")
    print(f"Forma de pagamento escolhida: {forma_texto}")
    print("="*40)
    print("Obrigada por comprar conosco! Volte sempre!")

#executa o programa
if __name__ == "__main__":
    main()
