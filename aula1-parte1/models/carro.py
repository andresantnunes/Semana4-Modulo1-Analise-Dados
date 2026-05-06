# Classes são uma junção de métodos e atributos
# class e nome
from pydantic import BaseModel, Field


class Carro():
    # dentro de uma classe temos um método de start
    # é a primeira coisa ser criada da classe
    # Método é toda função criada dentro de uma classe
    def __init__(self, marca, modelo, ano, cor):
        #Atributos de carros
        #Atributo é toda variável que existe apenas dentro de uma classe
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False # valor padrão de criação de uma Classe
        self.velocidade = 0

    # Métodos não padrão, ou seja são de escolha do programador
    # self = esse Objeto
    def ligar(self):
        if not self.ligado: # se o ligado estiver como False execute o código a seguir
            self.ligado = True
            print("Dar partida no carro")
        else:
            print("Carro ligado")

class Onibus(BaseModel):
    marca: str
    modelo: str
    ano: int = Field(gt=1885)
    cor: str

class RequisicaoCarro(BaseModel):
    marca:str
    modelo:str