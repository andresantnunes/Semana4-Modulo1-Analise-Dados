# import denota uma importação de outro arquivo e sua lógica
# podemos importar: class, def/função
import models.carro as carro

# objeto é toda Classe preenchida com dados
# objeto é uma instancia de uma Classe
# objeto é uma ocorrecia de uma Classe
ford_ka = carro.Carro("Ford", "KA", "2017", "Preto")
nissan_yaris = carro.Carro("Nissan", "Yaris", "2017", "Prata")
ford_ka_max = ford_ka
nivus = carro.Carro("Volkwagen", "Nivus", "2017", "Prata")
print(ford_ka)
print(ford_ka_max)
print(nissan_yaris)
print(nivus)

print(f"Ford KA Ligado? {ford_ka.ligado}")
print(f"Ford KA Max Ligado? {ford_ka_max.ligado}")
ford_ka.ligar() # acesso a o método de Carro, dentro do objeto
print(f"Ford KA Ligado? {ford_ka.ligado}")
print(f"Ford KA Max Ligado? {ford_ka_max.ligado}")
print()
print(f"Nissan Ligado? {nissan_yaris.ligado}")


onibus1 = carro.Onibus("Volkwagen", "Nivus", "2017", "Prata")




def soma(numero1, numero2):
    return numero1+numero2

resultado = soma(1,2)
# print(resultado)

resultado = soma(1,soma(soma(1,4),53))
# print(resultado)


