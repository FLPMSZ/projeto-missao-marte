from pytest_bdd import scenarios, given, when, then
from src.gerenciador_recursos import GerenciadorRecursosMarte
from src.servico_telemetria import ServicoTelemetriaEspacial

scenarios('features/solicitacao_oxigenio.feature')

@given("o estoque inicial do habitat e 1000", target_fixture="gerenciador_bdd")
def estoque_inicial():
    return GerenciadorRecursosMarte(ServicoTelemetriaEspacial())

@when("4 astronautas consomem oxigenio por 3 dias em taxa normal 1.0")
def consumo_normal(gerenciador_bdd):
    gerenciador_bdd.calcular_consumo(4, 3, 1.0)

@then("o estoque restante armazenado deve ser 880")
def verifica_estoque_restante(gerenciador_bdd):
    assert gerenciador_bdd.estoque_oxigenio == 880