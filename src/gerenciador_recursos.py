class OxigenioInsuficienteError(Exception): 
    pass

class NivelEmergenciaInvalidoError(Exception): 
    pass

class GerenciadorRecursosMarte:
    def __init__(self, telemetria):
        self.estoque_oxigenio = 1000
        self.estoque_agua = 1000
        self.telemetria = telemetria

    def calcular_consumo(self, astronautas: int, dias: int, taxa_emergencia: float):
        if taxa_emergencia < 1:
            raise NivelEmergenciaInvalidoError("Taxa invalida")
        
        consumo = astronautas * dias * taxa_emergencia * 10
        
        if consumo > self.estoque_oxigenio:
            self.telemetria.disparar_alerta("Crise Critica de Oxigenio")
            raise OxigenioInsuficienteError("Estoque insuficiente")
            
        self.estoque_oxigenio -= consumo
        self.telemetria.enviar_relatorio("Consumo normal")
        return self.estoque_oxigenio