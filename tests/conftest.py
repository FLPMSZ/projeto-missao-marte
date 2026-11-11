import pytest
from src.gerenciador_recursos import GerenciadorRecursosMarte
from src.servico_telemetria import ServicoTelemetriaEspacial
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def parametros_iniciais():
    return {"oxigenio_inicial": 1000, "agua_inicial": 1000}

@pytest.fixture(scope="function")
def gerenciador():
    telemetria = ServicoTelemetriaEspacial()
    gen = GerenciadorRecursosMarte(telemetria)
    yield gen
    gen.estoque_oxigenio = 0

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()