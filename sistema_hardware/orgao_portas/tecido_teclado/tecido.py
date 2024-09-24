import random

import sensitive_ext
import main

from sistema_hardware.orgao_portas.tecido_teclado.db_teclas import DBTecido

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

            dbt = DBTecido()

            # inseri no banco
            rotulo_existe = dbt.verificar_rotulo_caractere()

            if rotulo_existe == "KeyError":

                dbt.inserir_string(st, self.sec_randon_string([]))

            else:

                verificar = dbt.verificar_caractere(st)

                if verificar == True:

                    print(st)

                else:

                    lista_frequencia = dbt.lista_frequencias()
                    print(lista_frequencia)
                    # dbt.inserir_string(st, self.sec_randon_string([]))

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
