# Forma obsoleta de ler arquivos

file = open("example.txt", "r") # abre uma conexão
content = file.read()
print(content)

file.close() # fecha uma conexão manualmente
# se por alguma razão o fechar não acontecer vamos 
# ter um espaço na memória sempre utilizado pelo read
# pode dar problema no restante do código


# modelo recomendado
# context manager, gerenciador de contexto
with open("example.txt", "r") as file: # abro a conexão
    content = file.read()
    print(content)
    # fecha uma conexão automaticamente
    # ao finalizar a função ou o arquivo dessa conexão,
    # ela vai fechar a conexão
