def somar(num1, num2):
    return num1+num2

# É possível, mas NÃO RECOMENDADO
# O lambda tem um motivo de existencia especifico
# maps, sorts, filters
somar_itens = lambda num1,num2: num1+num2

print(somar(10,20))
print()
print(somar_itens(10,20))


# Sort -> Ordenação
# Tuple é imutável
# Perfeita para trasportar valores
produtos = [
    # 0,1 -> indices
    ("Teclado", 300), # item[1] = 300
    ("Mouse", 200), # item[1] = 200
    ("Mouse1", 200), # item[1] = 200
    ("Mouse2", 200), # item[1] = 200
    ("CPU", 2000), # item[1] = 2000
    ("Chocolate", 20), 
    ("Chocolate1", 20), 
    ("Chocolate2", 20), 
    ("Agua", 5)
]

#ordernar produto usamos o sorted()
# for loop para cada item e vai usar o lambda na variavel key 
# como o método de decisão do campo que vamos usar para separar 
# maior de menor 
produtos_ordenados = sorted(
    produtos,
    key=lambda item: item[1] # produtos[0][1] > produtos[1][1]
)

print("produtos_ordenados")
print(produtos_ordenados)

produtos_filtrados = list(filter(
    lambda item: item[1] >= 300 # retorna um booleano
    ,produtos
))

print("produtos_filtrados")
print(produtos_filtrados)


numeros = [1, 2, 3, 4, 5]

# para cada item da lista, multiplique por 2
# lambdas são mais lentos em geral para maps
# isso pode ser resolvido com outros tipos de mapeamentos
dobrados = list(map(lambda item: item * 2, numeros))
dobrados_comp = [numero * 2 for numero in numeros]
        # faça a operação item * 2 para cara item em numeros
        # faça operaçao for each item 

print(dobrados)
print(dobrados_comp)
# Saída: [2, 4, 6, 8, 10]


###############
def multiplicar(numero):
    # Input vezes memória
    return lambda x: x * numero
# double -> multiplicar (2) -> lambda
# doube(5) -> lambda x=5 numero=2

double = multiplicar(2)  # Cria uma closure com o numero=2
triple = multiplicar(3)  # Cria uma closure com o numero=3

# multiplicar(2) - 2 é o numero
# lambda 5: 5*2
print(double(5))  # 10
print(double(6))  # 10
print(double(7))  # 10
print(triple(5))  # 15


