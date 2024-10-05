from REDE.snperiferico.teclado.vida import Vida


class TempoTeclado:

    tempo_minuto = 0
    tempo_horas = 0
    tempo_dia = 0

    def __init__(self) -> None:

        self.vida = Vida()

    def contar_tempo(self):

        if TempoTeclado.tempo_minuto < 81:

            self.vida_81()
            TempoTeclado.tempo_minuto = TempoTeclado.tempo_minuto + 9

        elif TempoTeclado.tempo_minuto == 81:

            self.vida_81()

            TempoTeclado.tempo_minuto = 0

        """ horas"""
        if TempoTeclado.tempo_horas < 3600:

            TempoTeclado.tempo_horas = TempoTeclado.tempo_horas + 9

        elif TempoTeclado.tempo_horas == 3600:

            TempoTeclado.tempo_horas = 0

        """dia"""
        if TempoTeclado.tempo_dia < 86400:

            TempoTeclado.tempo_dia = TempoTeclado.tempo_dia + 9

        elif TempoTeclado.tempo_dia == 86400:

            TempoTeclado.tempo_dia = 0

    def vida_81(self):

        vid = Vida()
        # vid.lista_sensor_81()
