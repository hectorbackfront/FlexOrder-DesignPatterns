🧩 FlexOrder – Padrões de Projeto
📘 Descrição

O projeto FlexOrder é uma refatoração de um sistema monolítico de processamento de pedidos, originalmente chamado SistemaPedidoAntigo.
O objetivo foi melhorar a organização do código, a coesão e o princípio de responsabilidade única (SRP), aplicando padrões de projeto de forma prática e clara.

🎯 Objetivo

Corrigir problemas do sistema legado (classe com muitas responsabilidades).

Permitir extensão de funcionalidades sem modificar o código existente (OCP).

Melhorar a manutenção e leitura do código.

Aplicar os padrões Estratégia, Decorador e Fachada.

🧠 Padrões Utilizados
🧩 Estratégia (Strategy)

Resolveu o problema de vários if/elif no código de pagamento e frete.

Agora, cada forma de pagamento e tipo de frete tem sua própria classe.

O comportamento pode ser trocado facilmente sem alterar a classe principal.

🎁 Decorador (Decorator)

Usado para aplicar descontos e taxas adicionais (ex: embalagem de presente).

Permite adicionar funcionalidades sem mudar a classe Pedido.

Cada regra extra é um decorador que modifica o valor total.

🏗️ Fachada (Facade)

Simplifica o processo de checkout.

A classe CheckoutFacade coordena todos os passos: pagamento, estoque e nota fiscal.

O código cliente chama apenas um método (concluir_transacao) para finalizar a compra.

🧾 Benefícios da Refatoração

Código mais limpo e organizado.

Facilidade para adicionar novas regras de negócio.

Menos acoplamento entre as partes do sistema.

Aplicação real dos princípios SRP e OCP.

📁 Estrutura do Projeto
/FlexOrder
│
├── estratégias/      → Estratégias de pagamento e frete
├── decoradores/      → Descontos e taxas extras
├── fachada/          → Classe principal de checkout e subsistemas
└── principal/        → Classe Pedido e ponto de execução

✅ Conclusão

O FlexOrder mostra como aplicar os padrões de projeto Estratégia, Decorador e Fachada para transformar um código monolítico em uma arquitetura modular, extensível e fácil de manter.
