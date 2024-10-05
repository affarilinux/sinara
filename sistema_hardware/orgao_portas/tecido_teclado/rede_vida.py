# from REDE.snperiferico.teclado import Vida


class HistoriaVida:

    lista_vida_9 = {}

    # tempo 81
    def soma_vida_sensores_81(self, id):
        adicao = 1
        if id in HistoriaVida.lista_vida_9:

            HistoriaVida.lista_vida_9[id] += adicao

        else:

            HistoriaVida.lista_vida_9[id] = adicao

        print(HistoriaVida.lista_vida_9)
