# decorators/desconto_pix.py
from .base_pedido import BasePedido

class DescontoPix(BasePedido):
    def __init__(self, pedido: BasePedido):
        self.pedido = pedido

    def calcular_valor(self) -> float:
        valor = self.pedido.calcular_valor()
        desconto = valor * 0.05
        print(f"Aplicando desconto PIX: -R${desconto:.2f}")
        return valor - desconto
