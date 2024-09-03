from utilitarios import (cadastrar_categoria, cadastrar_transacao, saldo_total)
from categoria import Categoria
from transacao import Transacao

print("Sistema de Finanças")
print("------------------------------------")

# categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_lazer = cadastrar_categoria("Lazer")
categoria_Viagens = cadastrar_categoria("Viagens")

# transacoes
cadastrar_transacao(
    descricao="Salário de Jun/2024",
    valor=1000.0,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Mamãe",
    valor=50.0,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Show da Bilie",
    valor=-120.0,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao="Disney",
    valor=-600.0,
    categoria=categoria_Viagens
)

cadastrar_transacao(
    descricao="Curso de medicina",
    valor=-125,
    categoria=categoria_Viagens
)

total = saldo_total()

print("O saldo total é de: ", total)
