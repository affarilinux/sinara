import random

import sensitive_ext
import main
import CELULA

from sistema_hardware.orgao_portas.tecido_teclado.db_neo import NeoTecidoSS
from sistema_hardware.orgao_portas.tecido_teclado.db_sqlite import SqliteTecido
from sistema_hardware.orgao_portas.tecido_teclado.celula import Nucleo
from sistema_hardware.orgao_portas.tecido_teclado.rede_vida import HistoriaVida

"""  LEITURA DE VARIAVEL - INICIO DE PROCESSO EXTERNO """


class Tecido:

    # ficar aqui para soma, contario erro soma
    loop_string = 0

    def __init__(self) -> None:

        checar = sensitive_ext.SensorExt.shared_teclado

        if len(checar) > 0:

            if checar[0] == r".\/desligar":

                main.Sistema.while_treads = False
                print(main.Sistema.while_treads)
            else:
                self.lista_sensor_ext()

    def lista_sensor_ext(self):

        # se for assim [] sem o if dar erro
        # isso e uma lista de outra classe sensitive_ext.py
        sensortec = sensitive_ext.SensorExt.shared_teclado

        lensensorlista = len(sensortec)

        # se lista sensitive_ext.py for maior que 0
        if lensensorlista > 0:

            ts = TeclaSensor()
            ts.Sensor(sensortec)

    """ 
        função primaria
    """


class TeclaSensor:

    def Sensor(self, sensor):

        # quantidade itens na lista sensitive_ext
        lensensorstring = len(sensor[0])

        # loop contagem da classe
        if Tecido.loop_string < lensensorstring:

            st = sensor[0][Tecido.loop_string]

            sql_tecido = SqliteTecido()
            sql_tec = sql_tecido.verificar_caractere(str(st))

            dbt = NeoTecidoSS()

            # tem no banco os caracteres
            if sql_tec == True:

                freq_caractere = sql_tecido.verificar_frequencia_por_caractere(
                    st)

                lista_sensores = dbt.lista_celular_sensor()

                self.calculo_ss(freq_caractere, lista_sensores)

            # nao tem no banco os caracteres
            elif sql_tec == False:

                list_freqsql = sql_tecido.obter_lista_frequencias()
                randon_1 = self.sec_randon_string(list_freqsql)

                # linha tabela
                sql_tecido.inserir_caractere(st, randon_1)

                if len(list_freqsql) == 0:

                    dbt.inserir_celular_Sensor(0, randon_1)
                else:
                    max = dbt.get_max_ID()

                    # celula
                    dbt.inserir_celular_Sensor(int(max) + 1, randon_1)

                # soma da classe
            Tecido.loop_string += 1

        # loop contagem da classe
        else:
            # remove indice 0 da lista
            sensitive_ext.SensorExt.shared_teclado.pop(0)
            Tecido.loop_string = 0

    def sec_randon_string(self, nun_ins):

        # Define o intervalo de números e a lista de exceções
        intervalo = range(1, 10001)  # Números de 1 a 10 000

        # Cria uma lista com os números que não estão na lista de exceções
        numeros_validos = [
            num for num in intervalo if num not in nun_ins]

        # Escolhe um número aleatório da lista de números válidos
        numero_aleatorio = random.choice(numeros_validos)
        # retorn de um valor
        return numero_aleatorio

    def calculo_ss(self, freq, lista_s):

        quant_len = len(lista_s)
        valor = 0
        lista = {}
        while valor < quant_len:

            valor_list = int(lista_s[valor].get("sensor"))

            resultado = None
            if valor_list > freq or valor_list < freq:

                # int para evitar numeros fracionado
                resultado = int((
                    CELULA.Celula.pico / Nucleo.sinapse) * valor_list)

            else:
                resultado = CELULA.Celula.pico

            valor_id = int(lista_s[valor].get("ID"))

            if resultado >= CELULA.Celula.limiar:

                lista[valor_id] = resultado

                # vida celular soma
                id_ht = HistoriaVida()
                id_ht.soma_vida_sensores_81(valor_id)

            valor = valor + 1

        Nucleo.lista_processamento["SS"] = lista

        print(Nucleo.lista_processamento)
