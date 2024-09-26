
class SNP:

    um = 0


class Nucleo:

    lista_processamento = {}


class MembranaPlasmatica:

    def sensor_tecla_inserir(self,fim):

        if Nucleo.lista_processamento.get(fim) is not None:

            print("sim")

        else:

            print("nao")
