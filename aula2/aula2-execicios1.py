def hello():
    print("hello world")

def mensagem(texto):
    print(texto)

def area(base, altura):
    return base*altura

def comparador(num1, num2):
    if num1 < num2:
        print(num1)
    elif num1 > num2:
        print(num2)
    else:
        print("Numeros Iguais")

def sinal(num):
    if num >= 0:
        print("Positivo")
    else:
        print("Negativo")



if __name__ == "__main__":
    texto = input("Texto: ")
    hello()
    mensagem(texto)
    print(f"Area: {area(3,5)}")
    comparador(1,2)
    sinal(-1)
    
