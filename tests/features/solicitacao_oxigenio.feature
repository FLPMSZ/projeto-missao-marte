Feature: Gestao de Suprimentos ECLSS
  Scenario: Consumo de oxigenio em condicoes normais
    Given o estoque inicial do habitat e 1000
    When 4 astronautas consomem oxigenio por 3 dias em taxa normal 1.0
    Then o estoque restante armazenado deve ser 880