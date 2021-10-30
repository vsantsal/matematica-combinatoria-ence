import pytest
from typing import (
    List,
)

from uteis.combinacoes import gera_subconjuntos


@pytest.mark.parametrize('conjunto_input, resultado_esperado', [
    (set(), [()]),
    ({100}, [(), (100, )]),
    ({0, 1}, [(), (0, ), (1, ), (0, 1)])
])
def test_gera_subconjuntos_retorna_resultado_esperado_de_conjunto_input_tipo_set(conjunto_input,
                                                                                 resultado_esperado):
    resultado_obtido: List = gera_subconjuntos(conjunto_input)
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('tamanho_conjunto_input, tamanho_resultado_esperado',[
    (5, 2**5),
    (10, 2**10),
    (13, 2**13),
])
def test_gera_subconjuntos_retorna_lista_com_tamanho_esperado(tamanho_conjunto_input,
                                                              tamanho_resultado_esperado):
    # construindo conjunto de teste com os elementos 0, 1, ..., tamanho_conjunto_input - 1
    conjunto_teste = {*range(tamanho_conjunto_input)}
    resultado_obtido: List = gera_subconjuntos(conjunto_teste)
    assert len(resultado_obtido) == tamanho_resultado_esperado
