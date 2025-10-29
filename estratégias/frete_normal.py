# estrategias/frete_normal.py
from .estrategia_frete import EstrategiaFrete

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, valor_com_desconto: float) -> float:
        custo = valor_com_desconto * 0.05
        print(f"Frete Normal: R${custo:.2f}")
        return custo
