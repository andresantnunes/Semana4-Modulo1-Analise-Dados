# import que retorna somente a classe importada
from models.carro import Carro

# esse método recebe 3 parametros, e retorna um objeto do tipo Carro
# o valor padrão para uma cor não preenchida é Prata
# os valos de modelo e ano devem ser do tipo string
def monta_ford(modelo:str, ano:str, cor="Prata") -> Carro:
    return Carro("Ford", modelo, ano, cor)

def novo_ano_carro(carro:Carro, ano:str) -> Carro:
    return Carro("Ford", carro.modelo, ano, carro.cor)

def atualiza_ano_carro(carro:Carro, ano:str) -> Carro:
    carro.ano = ano