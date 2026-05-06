class Conta:
    titular:str # jsons recebidos em apis web
    agencia:int # ou estruturas de dados
    saldo:float

    numero_clientes=0
    agencia = 1 # variavel com valor padrão
#  Os atributos que vc colocar nos parametros do init são obrigatórios de serem preenchidos na criação do objeto
    def __init__(self,titular,agencia,saldo):
        self.titular = titular # forma mais tradicional de criar atributos
        self.agencia = agencia
        self.saldo = saldo
        Conta.numero_clientes += 1
        Conta.agencia

    def consultar_saldo(self):
        return self.saldo # self é o valor do objeto
                          # sem o self o valor pertence a classe, ou seja static

    @staticmethod
    def total_clientes():
        return Conta.numero_clientes
    

    # é um valor que não é self
    # ele é parte da classe
    @staticmethod
    def total_agencias():
        return Conta.agencia
    
    @staticmethod
    def adiciona_agencia(numero=1):
        Conta.agencia+=numero

    @staticmethod
    def remover_agencia():
        Conta.agencia-=1


