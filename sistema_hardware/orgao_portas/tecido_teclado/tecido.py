import random

import sensitive_ext
import main

from NEO4J.tabela import NeoTabela

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
            tabela = NeoTabela()

            # True e false
            rotulo_caractere = tabela.verificar_rotulo_CARACTERE("CARACTERE")

            if rotulo_caractere == "KeyError":

                print("02")
                # cada entrada tem esta numa variavel pois da erro em salvar
                randon = self.sec_randon_string([])
                # caractere
                dbt.inserir_string(st, randon)
                # celula
                dbt_1 = DBTecido()
                dbt_1.inserir_celular_Sensor(0, randon)

            elif rotulo_caractere == "ROTULO EXISTE":

                print("03")
                verificar = dbt.verificar_caractere(st)

                # inserir dicionario, processamento
                if verificar == True:

                    # verificar frequencia do caractere
                    verificar_1 = dbt.encontrar_frequencia_caractere(st)
                    # lista do sensor
                    # lista_sensores =
                    self.calculo_ss(verificar_1, lista_ss)
                # inserir rotulo
                elif verificar == False:

                    lista_ss = dbt.lista_frequencias()
                    randon_1 = self.sec_randon_string(lista_ss)

                    # caractere
                    dbt.inserir_string(st, randon_1)

                    max = dbt.get_max_ID()
                    # celula
                    dbt_2 = DBTecido()
                    dbt_2.inserir_celular_Sensor(max, randon_1)

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

    def calculo_ss(self, carac, lista_s):

        print(carac, lista_s)
