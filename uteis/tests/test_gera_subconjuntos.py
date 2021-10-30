from itertools import combinations
import pytest
from typing import (
    List,
)

from uteis.combinacoes import gera_subconjuntos


@pytest.mark.parametrize('conjunto_input, resultado_esperado', [
    (set(), [()]),
    ({100}, [(), (100,)]),
    ({0, 1}, [(), (0,), (1,), (0, 1)])
])
def test_gera_subconjuntos_retorna_resultado_esperado_de_conjunto_input_tipo_set(conjunto_input,
                                                                                 resultado_esperado):
    resultado_obtido: List = gera_subconjuntos(conjunto_input)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('tamanho_conjunto_input, tamanho_resultado_esperado', [
    (5, 2 ** 5),
    (10, 2 ** 10),
    (13, 2 ** 13),
    (20, 2 ** 20)
])
def test_gera_subconjuntos_retorna_lista_com_tamanho_esperado(tamanho_conjunto_input,
                                                              tamanho_resultado_esperado):
    # construindo conjunto de teste com os elementos 0, 1, ..., tamanho_conjunto_input - 1
    conjunto_teste = {*range(tamanho_conjunto_input)}
    resultado_obtido: List = gera_subconjuntos(conjunto_teste)
    assert len(resultado_obtido) == tamanho_resultado_esperado


@pytest.mark.parametrize('tamanho_conjunto_input, tamanho_resultado_esperado', [
    (21, 2 ** 21),
    (100, 2 ** 100),
])
def test_gera_subconjuntos_lanca_value_error_para_tamanhos_maiores(tamanho_conjunto_input,
                                                                   tamanho_resultado_esperado):
    # construindo conjunto de teste com os elementos 0, 1, ..., tamanho_conjunto_input - 1
    conjunto_teste = {*range(tamanho_conjunto_input)}
    with pytest.raises(ValueError) as excecao:
        gera_subconjuntos(conjunto_teste)

    assert 'gera_subconjuntos ainda não suporta conjuntos maiores' in excecao.value.args[0]


@pytest.mark.parametrize('conjunto_input, cardinalidade, resultado_esperado', [
    (range(3), 2, [*combinations(range(3), 2)]),
    (range(7), 3, [*combinations(range(7), 3)]),
])
def test_gera_subconjuntos_retorna_resultado_esperado_se_cardinalidade_passada(conjunto_input,
                                                                               cardinalidade,
                                                                               resultado_esperado):
    resultado_obtido: List = gera_subconjuntos(conjunto_input, cardinalidade)
    assert resultado_obtido == resultado_esperado
