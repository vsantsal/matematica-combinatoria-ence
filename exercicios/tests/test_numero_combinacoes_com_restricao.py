import operator
import pytest

from exercicios.aula_05 import (
    numero_combinacoes_com_restricao_para_identidade_elementos,
    numero_combinacoes_com_restricao_para_soma_elementos,
    Restricao,
)


@pytest.mark.parametrize('iteravel, numero_escolhas, restricao, resultado_esperado',
                         [(range(4), 3, Restricao(operator.ge, 2), 4),
                          (range(3), 2, Restricao(operator.lt, 2), 1)])
def test_numero_combinacoes_com_restricao_para_soma_elementos_casos_base(iteravel,
                                                                         numero_escolhas,
                                                                         restricao,
                                                                         resultado_esperado):
    resultado_obtido: int = numero_combinacoes_com_restricao_para_soma_elementos(iteravel,
                                                                                 numero_escolhas,
                                                                                 restricao)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('iteravel, numero_escolhas, valor_pesquisado, numero, resultado_esperado',
                         [([1, 3, 7, 7, 7, 5],
                           5,
                           7,
                           2,
                           3)])
def test_numero_combinacoes_com_restricao_para_identidade_elementos_casos_base(iteravel,
                                                                               numero_escolhas,
                                                                               valor_pesquisado,
                                                                               numero,
                                                                               resultado_esperado):
    resultado_obtido: int = numero_combinacoes_com_restricao_para_identidade_elementos(iteravel,
                                                                                       numero_escolhas,
                                                                                       valor_pesquisado,
                                                                                       numero)
    assert resultado_obtido == resultado_esperado
