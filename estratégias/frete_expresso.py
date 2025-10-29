# estrategias/frete_expresso.py
from .estrategia_frete import EstrategiaFrete

class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, valor_com_desconto: float) -> float:
        custo = valor_com_desconto * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo:.2f}")
        return custo
