import service.montadora as mt
import models.carro as cr

onibus_objeto = cr.Onibus(
    marca="Marca", 
    modelo="Modelo", 
    ano="12311", 
    cor="Cor"
)
print("\nOnibus")
print(onibus_objeto.marca)
print(onibus_objeto.ano)

# resultado é um objeto de tipo Carro
carro = mt.monta_ford("T",1968)
print(carro.ano)

mt.atualiza_ano_carro(carro, 2001)
print(carro.ano)
