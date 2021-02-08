import keyboard
import threading as th
import temporizador
import time
# import interface

class Controlador:

    def __init__(self, master=None):
        self.temporizadores = []

    def cria_temporizador(self, minutos, segundos, stopkey='esc'):
        print('Cria temporizador')

        self.temporizadores.append(temporizador.Temporizador(label='timer1', stopkey=stopkey, minutos=minutos, segundos=segundos))

        temporizador_count = len(self.temporizadores)
        print('Temporizadores ativos:', temporizador_count)

    def monitora_temporizador(self, index):
        temp = self.temporizadores[index]
        if (temp != None):
            while(temp.executando):
                if (temp.temporizando):
                    print(temp.get_tempo())
                    time.sleep(1)

    ### THREADS ###

    def finaliza_temporizador(self, index):
        temp = self.temporizadores[index] 
        temp.finalizar()
        self.temporizadores.remove(temp)

    def ler_entrada(self):
        keyboard.add_hotkey(hotkey='esc', callback=self.finaliza_temporizador, args=(0,))

    def main(self):
        """
        função principal
        """
        # print(th.current_thread()._ident)
        # self.iniciar_threads() 

if __name__ == '__main__':
    ctrl = Controlador()
    ctrl.cria_temporizador(0, 5)

    # Threads
    t_saida_temporizador = th.Thread(target=ctrl.monitora_temporizador, args=(0,))
    t_entrada = th.Thread(target=ctrl.ler_entrada)

    temp = ctrl.temporizadores[0]

    time.sleep(2)
    
    print('Iniciando o temporizador \''+temp.get_label()+'\'')
    temp.mudar_status()

    t_saida_temporizador.start()
    t_entrada.start()
    # while (temp.temporizando):
    #     print(temp.get_tempo())
    #     time.sleep(1)