def lista_de_compras():
    lista = []

    # --- Mensagem de Boas-Vindas ---
    print("\nBem-vindo à Lista de Compras Simples")
    print("Desenvolvida com muito amor e um pouco de ódio por Marcos Okamoto")
    print("------------------------------------------------------------------\n")

    while True:
        if lista:
            print("\n --- SUA LISTA DE COMPRAS ATUAL--- \n")
            for compra in lista:
                print(f"ID: {compra['id']} - {compra['nome']} ({compra['quantidade']} {compra['unidade']}) - "
                      f"{compra['descricao']}")
        print()

        # --- Menu Principal ---
        print("Lista de Compras:")
        print("  A. Adicionar produto")
        print("  B. Remover produto")
        print("  C. Pesquisar produto")
        print("  D. Sair do Programa")
        print("-" * 25)

        opcao = input("Selecione uma das letras associadas às funções, por favor: ")

        # --- Condição de Saída ---
        if opcao == 'D' or opcao == 'd':
            print("\nObrigado por utilizar a Lista de Compras. Até a próxima!\n")
            break

        # --- Verificação de Opção Inválida ---
        if opcao not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
            print("\n[ERRO] Opção inválida. Por favor, tente novamente.\n")
            continue

        # --- Lógica para Adicionar Produto ---
        if opcao == 'a' or opcao == 'A':
            novo_produto = {}
            print("\n--- Adicionando Novo Produto ---")

            novo_produto['nome'] = input("Digite o nome do produto: ")

            opcoes_unidades = {
                "A": "Quilograma",
                "B": "Grama",
                "C": "Litro",
                "D": "Mililitro",
                "E": "Unidade",
                "F": "Metro",
                "G": "Centímetro"
            }

            # Loop de validação para a unidade
            while True:
                print("\nEscolha a unidade de medida:")
                for letra_opcao, texto_unidade in opcoes_unidades.items():
                    print(f"  {letra_opcao}. {texto_unidade}")

                letra_escolhida = input("Digite a letra da unidade: ").upper()

                if letra_escolhida in opcoes_unidades:
                    novo_produto['unidade'] = opcoes_unidades[letra_escolhida]
                    break
                else:
                    print("\n[ERRO] Opção inválida! Por favor, escolha uma das letras da lista de opções.\n")

            # Coleta dos dados restantes
            novo_produto['quantidade'] = float(input("Digite a quantidade: "))
            novo_produto['descricao'] = input("Digite a descrição do produto (opcional): ")
            id_produto = len(lista) + 1
            novo_produto['id'] = id_produto

            lista += [novo_produto]

            print(f"\n[SUCESSO] Produto '{novo_produto['nome']}' ID:'{novo_produto['id']}' adicionado!\n")

        if opcao == 'b' or opcao == 'B':
           id_remover = int(input("\nDigite o `ID` do produto que deseja remover: "))
           item_foi_removido = False
           for produto_atual in lista:
               if produto_atual['id'] == id_remover:
                lista.remove(produto_atual)
                item_foi_removido = True
                print(f"\n[SUCESSO] O produto '{produto_atual['nome']}' (ID: {produto_atual['id']}) foi removido.\n")
                break
           if not item_foi_removido:
               print("ID não encontrado!")

# --- Início da execução do programa ---
lista_de_compras()