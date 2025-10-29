# facade/checkout_facade.py
from estrategias.estrategia_pagamento import EstrategiaPagamento
from estrategias.estrategia_frete import EstrategiaFrete
from facade.sistema_estoque import SistemaEstoque
from facade.gerador_nota_fiscal import GeradorNotaFiscal

class CheckoutFacade:
    def __init__(self, estrategia_pagamento: EstrategiaPagamento, estrategia_frete: EstrategiaFrete):
        self.estrategia_pagamento = estrategia_pagamento
        self.estrategia_frete = estrategia_frete
        self.estoque = SistemaEstoque()
        self.nota = GeradorNotaFiscal()

    def concluir_transacao(self, pedido):
        print("\n=== Iniciando Checkout ===")
        valor = pedido.calcular_valor()

        frete = self.estrategia_frete.calcular_frete(valor)
        total = valor + frete

        print(f"Valor final com frete: R${total:.2f}")

        if self.estrategia_pagamento.processar_pagamento(total):
            print("Pagamento aprovado!")
            self.estoque.atualizar_estoque([])
            self.nota.emitir_nota(pedido)
            print("Checkout concluído com sucesso.")
        else:
            print("Falha no pagamento. Pedido cancelado.")
