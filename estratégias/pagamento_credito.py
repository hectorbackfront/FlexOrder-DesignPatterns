# estrategias/pagamento_credito.py
from .estrategia_pagamento import EstrategiaPagamento

class PagamentoCredito(EstrategiaPagamento):
    def processar_pagamento(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via Cartão de Crédito...")
        if valor_final < 1000:
            print(" -> Pagamento com Crédito APROVADO.")
            return True
        else:
            print(" -> Pagamento com Crédito REJEITADO (limite excedido).")
            return False
