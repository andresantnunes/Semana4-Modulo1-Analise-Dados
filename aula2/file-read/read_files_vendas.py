
try:
    # tempo O(n) - n = numero de linhas
    # espaço é O(1)

    # utf-8 permite acentos e simbolos em geral, ex:ç
    with open("./aula2/file-read/vendas_modelo.csv", "r", encoding="utf-8") as arq: 
        for linha in arq.readlines()[1:]:
            # strip - remove espaços em branco ao redor da string
            # split - quebrar os item em diferentes variáveis pela strint ","
            # estrutura que eu controlo, limitada
            id_venda,produto,quantidade,preco_unitario = linha.strip().split(",")

            print(f"Venda com id {id_venda}, com a quantidade {quantidade}")

except FileNotFoundError as e: # segura, captura erro
    print("Arquivo não encontrado")
