import pytest
from src.gerenciador_recursos import OxigenioInsuficienteError, NivelEmergenciaInvalidoError

@pytest.mark.parametrize("astronautas, dias, taxa, esperado", [
    (2, 5, 1.0, 900),
    (3, 2, 2.0, 880),
    (1, 10, 1.5, 850)
])
def test_calculo_consumo(gerenciador, astronautas, dias, taxa, esperado):
    assert gerenciador.calcular_consumo(astronautas, dias, taxa) == esperado

def test_excecao_taxa_invalida(gerenciador):
    with pytest.raises(NivelEmergenciaInvalidoError):
        gerenciador.calcular_consumo(2, 5, 0.5)

def test_isolamento_telemetria(gerenciador, mocker):
    mock_alerta = mocker.patch.object(gerenciador.telemetria, 'disparar_alerta')
    with pytest.raises(OxigenioInsuficienteError):
        gerenciador.calcular_consumo(50, 10, 3.0)
    mock_alerta.assert_called_once_with("Crise Critica de Oxigenio")