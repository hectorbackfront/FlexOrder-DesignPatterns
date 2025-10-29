# decorators/taxa_embalagem_presente.py
from .base_pedido import BasePedido

class TaxaEmbalagemPresente(BasePedido):
    def __init__(self, pedido: BasePedido):
        self.pedido = pedido

    def calcular_valor(self) -> float:
        valor = self.pedido.calcular_valor()
        taxa = 5.00
        print(f"Adicionando taxa de embalagem presente: +R${taxa:.2f}")
        return valor + taxa
