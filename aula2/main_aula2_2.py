# sugestão dos tipos, a menos que tenha uma lib para validar
# em geral é usado como documentação
def soma(numero1:int, numero2:int) -> int:
    return numero1+numero2

def multiplicacao(numero1 = 1, numero2 = 1):
    # Contexto da função 
    return numero1*numero2

def divisao(numero1, numero2, numero3):
    return numero1/numero2

# procedure -> não tem retorno
# não é tão importante no dia a dia
def soma_input():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))

    return numero1+numero2


num1 = 20
num2 = 30

resultado = soma(num1,num2)
resultado = soma(10,31)
print(f"Resultado soma: {resultado}")

resultado = multiplicacao(num1,num2)
print(f"Resultado multiplicacao: {resultado}")

resultado = divisao(num1,num2)
print(f"Resultado divisao: {resultado}")

resultado = soma_input() 
print(f"Resultado soma dos inputs: {resultado}")





dobrar = lambda x: x * 2

print(dobrar(5))