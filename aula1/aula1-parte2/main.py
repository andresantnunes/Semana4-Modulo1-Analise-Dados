from service.transacionar import depositar, sacar
from model.conta import Conta

conta_corrente = Conta("Marcos Aurélio", "0102", 100.01)
conta_corrente1 = Conta("Marcos Marques", "0102", 101.01)
conta_corrente2 = Conta("Marcos Julio", "0102", 102.01)
conta_corrente3 = Conta("João Marcos", "0102", 103.01)


# print(conta_corrente.consultar_saldo())
# print(conta_corrente1.consultar_saldo())
# print(conta_corrente2.consultar_saldo())
# print(conta_corrente3.consultar_saldo())


Conta.adiciona_agencia()
print(f"Total de agencias é {Conta.total_agencias()}")
print(f"Total de clientes é {Conta.total_clientes()}")
