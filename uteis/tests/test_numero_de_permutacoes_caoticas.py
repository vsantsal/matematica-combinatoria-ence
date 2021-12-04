import pytest
from uteis.permutacoes import numero_de_permutacoes_caoticas


@pytest.mark.parametrize('inteiro, perms_esperadas',
                         [(6, 265),
                          (8, 14833),
                          (15, 481066515734)])
def test_resultados_basicos_de_numero_de_permutacoes_caoticas(inteiro, perms_esperadas):
    perms_obtidas: int = numero_de_permutacoes_caoticas(inteiro)
    assert perms_obtidas == perms_esperadas
