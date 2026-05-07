# podemos ter variáveis globais que são acessadas por todo o sistema
# Upper Sneak_case
# Configuração -> string de conexão
#   usuario e senha
# Constante - Não pode ser alterada depois de criada
VARIAVEL_GLOBAL = 1

# Buscar flags de sistema
# Em geral são booleanos que ativam ou desativam partes do sistema
MULTIPLICACAO_ATIVA = True

# Contadores globais
# contador_operacoes = 0 # Não consegue ser alterado pelas funções
# ALERTA - Variáveis globais são dificeis de ler e confusas
#   prefira parametros
contador_operacoes = 0

def soma(numero1, numero2):
    global contador_operacoes
    contador_operacoes += 1
    return numero1+numero2+VARIAVEL_GLOBAL

def multiplicacao(numero1, numero2):
    if not MULTIPLICACAO_ATIVA:
        return
    global contador_operacoes
    contador_operacoes += 1

    return numero1*numero2

def divisao(numero1, numero2):
    global contador_operacoes
    contador_operacoes += 1

    return numero1/numero2

def soma_input():
    global contador_operacoes
    contador_operacoes += 1

    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))

    return numero1+numero2+VARIAVEL_GLOBAL


def multiplicar_input():
    if not MULTIPLICACAO_ATIVA:
        return
    
    global contador_operacoes
    contador_operacoes += 1

    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    resultado = numero1 * numero2
    print(f"Resultado multiplicacao: {resultado}")

def exponencial(numero1, numero2):
    global contador_operacoes
    contador_operacoes += 1

    return numero1**numero2

exponencial(1,2)

num1 = 20
num2 = 30

resultado = soma(num1,num2)
print(f"Resultado soma: {resultado}")

resultado = multiplicacao(num1,num2)
print(f"Resultado multiplicacao: {resultado}")

resultado = divisao(num1,num2)
print(f"Resultado divisao: {resultado}")

resultado = soma_input() 
print(f"Resultado soma dos inputs: {resultado}")

resultado = multiplicar_input()
print(f"Resultado multiplicacao dos inputs: {resultado}")

print(f"Total de Operações: {contador_operacoes}")

