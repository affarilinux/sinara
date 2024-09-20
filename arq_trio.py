import trio

from sistema_hardware.orgao_portas.tecido_teclado.tecido import Tecido

import main


class TrioTasks:
    async def tim(self):

        # Função assíncrona que executa uma tarefa repetidamente usando Trio
        while main.Sistema.while_treads:

            tec = Tecido()
            await trio.sleep(2)  # Aguarda 2 segundos antes de continuar

    async def run(self):

        # Função para rodar todas as tarefas assíncronas usando o Trio
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.tim)  # Inicia a tarefa 'tim' no Trio

    def start_trio(self):

        # Executa o loop do Trio
        trio.run(self.run)
