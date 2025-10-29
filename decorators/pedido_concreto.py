# decorators/pedido_concreto.py
from .base_pedido import BasePedido

class PedidoConcreto(BasePedido):
    def __init__(self, itens):
        self.itens = itens

    def calcular_valor(self) -> float:
        return sum(item['valor'] for item in self.itens)
