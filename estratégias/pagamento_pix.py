# estrategias/pagamento_pix.py
from .estrategia_pagamento import EstrategiaPagamento

class PagamentoPix(EstrategiaPagamento):
    def processar_pagamento(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via PIX...")
        print(" -> Pagamento com PIX APROVADO (QR Code gerado).")
        return True
