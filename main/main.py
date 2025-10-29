# main.py
from estrategias.pagamento_pix import PagamentoPix
from estrategias.pagamento_credito import PagamentoCredito
from estrategias.frete_normal import FreteNormal
from estrategias.frete_expresso import FreteExpresso

from decorators.pedido_concreto import PedidoConcreto
from decorators.desconto_pix import DescontoPix
from decorators.taxa_embalagem_presente import TaxaEmbalagemPresente

from facade.checkout_facade import CheckoutFacade

if __name__ == "__main__":
    itens = [
        {'nome': 'Capa da Invisibilidade', 'valor': 150.0},
        {'nome': 'Poção de Voo', 'valor': 80.0}
    ]

    # Pedido base
    pedido = PedidoConcreto(itens)

    # Aplica desconto PIX e embalagem presente (com Decorator)
    pedido_com_desconto = DescontoPix(pedido)
    pedido_final = TaxaEmbalagemPresente(pedido_com_desconto)

    # Cria estratégias
    pagamento = PagamentoPix()
    frete = FreteNormal()

    # Usa a Fachada
    checkout = CheckoutFacade(pagamento, frete)
    checkout.concluir_transacao(pedido_final)
