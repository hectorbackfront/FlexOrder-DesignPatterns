# decorators/base_pedido.py
from abc import ABC, abstractmethod

class BasePedido(ABC):
    @abstractmethod
    def calcular_valor(self) -> float:
        pass
