import pytest

from uteis.permutacoes import posicao_de_numero_em_permutacoes_algarismos


@pytest.mark.parametrize('numero, is_decrescente, posicao_esperada',
                         [(75389, True, 66), ])
def test_retorna_posicao_esperada_passando_flag(numero, is_decrescente, posicao_esperada):
    posicao_obtida: int = posicao_de_numero_em_permutacoes_algarismos(numero, is_decrescente)
    assert posicao_obtida == posicao_esperada


@pytest.mark.parametrize('numero, posicao_esperada',
                         [(85379, 79), ])
def test_retorna_posicao_esperada_sem_passar_flag(numero, posicao_esperada):
    posicao_obtida: int = posicao_de_numero_em_permutacoes_algarismos(numero)
    assert posicao_obtida == posicao_esperada
