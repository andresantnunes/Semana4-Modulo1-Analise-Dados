
from model.conta import Conta

def sacar(conta:Conta, valor:float):
    if(valor < 0):
        return
    conta.saldo -= valor

def depositar(conta:Conta, valor:float):
    if(valor < 0):
        return # retornar sem valor, interrompe o código
    conta.saldo += valor