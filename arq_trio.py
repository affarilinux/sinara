import trio
import main

from sistema_hardware.orgao_portas.tecido_teclado.tecido import Tecido
from REDE.rede import Rede


class TrioTasks:
    async def rede(self):

        # Função assíncrona que executa uma tarefa repetidamente usando Trio
        while main.Sistema.while_treads:
            rede = Rede()

            await trio.sleep(9)

    async def teclado(self):

        # Função assíncrona que executa uma tarefa repetidamente usando Trio
        while main.Sistema.while_treads:

            tec = Tecido()

            await trio.sleep(2)  # Aguarda 2 segundos antes de continuar

    async def run(self):

        # Função para rodar todas as tarefas assíncronas usando o Trio
        async with trio.open_nursery() as nursery:

            # Inicia a tarefa 'teclado' no Trio
            nursery.start_soon(self.teclado)
            # Inicia a tarefa 'rede' no Trio
            # filtra rede
            nursery.start_soon(self.rede)

    def start_trio(self):

        # Executa o loop do Trio
        trio.run(self.run)
