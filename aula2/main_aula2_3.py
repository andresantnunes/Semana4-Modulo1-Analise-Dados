# parametros com valor padrão se tornam opcionais
def multiplicacao(numero1 = 1, numero2 = 1):
    # Contexto da função 
    return numero1*numero2


num1 = 20
num2 = 30

# Podemos preencher apenas o parametro utilizando o seu nome
resultado = multiplicacao(numero1=num1)
resultado = multiplicacao(num1)
resultado = multiplicacao(numero2=num2, numero1=num2)
print(f"Resultado multiplicacao: {resultado}")