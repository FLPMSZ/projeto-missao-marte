import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_solicitacao_painel_web(driver):
    caminho_arquivo = f"file://{os.path.abspath('web/painel.html')}"
    driver.get(caminho_arquivo)
    try:
        driver.find_element(By.ID, "qtd_oxigenio").send_keys("150")
        driver.find_element(By.ID, "btn_solicitar").click()
        espera = WebDriverWait(driver, 3)
        status_atualizado = espera.until(
            EC.text_to_be_present_in_element((By.ID, "status_painel"), "Solicitação Aprovada")
        )
        assert status_atualizado is True
    except AssertionError:
        driver.save_screenshot("evidencia_falha_web.png")
        raise