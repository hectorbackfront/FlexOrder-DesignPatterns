# estrategias/estrategia_frete.py
from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular_frete(self, valor_com_desconto: float) -> float:
        pass
