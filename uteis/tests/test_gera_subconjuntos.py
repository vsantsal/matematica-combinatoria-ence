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


@pytest.mark.parametrize('len_input, len_resultado_esperado', [
    (5, 2 ** 5),
    (10, 2 ** 10),
    (13, 2 ** 13),
    (20, 2 ** 20)
])
def test_gera_subconjuntos_retorna_lista_com_tamanho_esperado(len_input,
                                                              len_resultado_esperado):
    # construindo conjunto de teste com os elementos 0, 1, ..., len_input - 1
    conjunto_teste = {*range(len_input)}
    resultado_obtido: List = gera_subconjuntos(conjunto_teste)
    assert len(resultado_obtido) == len_resultado_esperado


@pytest.mark.parametrize('len_input', [21, 100])
def test_gera_subconjuntos_lanca_value_error_para_tamanhos_maiores_e_gerador_false(len_input):
    # construindo conjunto de teste com os elementos 0, 1, ..., len_input - 1
    conjunto_teste = {*range(len_input)}
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


@pytest.mark.parametrize('len_input, len_resposta_esperada', [
    (21, 2 ** 21),
    (22, 2 ** 22),
])
def test_gera_subconjuntos_nao_lanca_value_error_para_tamanhos_maiores_e_gerador_true(len_input,
                                                                                      len_resposta_esperada):
    # construindo conjunto de teste com os elementos 0, 1, ..., len_input - 1
    conjunto_teste = {*range(len_input)}
    iterador = gera_subconjuntos(conjunto_teste, gerador=True)
    num_elementos = sum(1 for _ in iterador)
    assert num_elementos == len_resposta_esperada
