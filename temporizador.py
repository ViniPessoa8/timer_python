import time
import os
import threading as th
import keyboard
import datetime
import math 

class Temporizador:
    def __init__(self, master=None, stopkey='space', label='-', minutos=0, segundos=0):
        # Instanciação das variáveis
        self.executando = True
        self.temporizando = False
        self.reiniciado = False

        # Tempo inicial
        self.min_inic = minutos
        self.seg_inic = segundos

        # Tempo atual (usado na contagem)
        self.min_atual = minutos
        self.seg_atual = segundos
        
        # Strings
        self.label = label
        self.stop_key = stopkey
        self.restart_key = 'r'

        # Threads
        self.t_temporizador = th.Thread(name='Temporizador-Thread('+label+')', target=self.__temporizar) # Inicia o temporizador

        self.t_temporizador.start()

        print('\n')
        self.__printar_saida()

    def mudar_status(self):
        self.temporizando = not self.temporizando

        if (self.temporizando):
            print('Ativado!')
        else:
            print('Parado!')

    def reiniciar(self):
        os.system('cls')
        self.min_atual = self.min_inic
        self.seg_atual = self.seg_inic
        self.reiniciado = True
        
        print("Reiniciado!")
        self.__printar_saida()

    def __temporizar(self):
        """
        função que inicia o temporizador
        """
        print('__temporizar()')
        while(self.executando):
            while(self.temporizando):
                if (self.reiniciado):
                #     continue
                #     # self.__printar_saida()
                # else:
                    self.reiniciado = False
                
                if (self.seg_atual > 0):
                    self.seg_atual -= 1
                elif (self.min_atual > 0):
                    self.min_atual -= 1
                    self.seg_atual = 59
                else:
                    self.mudar_status()
                    print("Fim!")

                time.sleep(1)

    def finalizar(self):
        self.temporizando = False
        self.executando = False
        print('Finalizado!')

    # def __ler_entrada(self):
    #     """
    #     função que monitora o teclado e para o timer caso o usuário tecle a 'stopkey' 
    #     """
    #     # Tecla que inicia o timer 
    #     # keyboard.add_hotkey(self.start_key, self.mudar_status)
        
    #     # Tecla que para o timer
    #     keyboard.add_hotkey(self.stop_key, self.mudar_status)

    #     keyboard.add_hotkey('esc', self.finalizar)

    #     # Tecla para reiniciar o timer
    #     keyboard.add_hotkey(self.restart_key, self.reiniciar)

    def __formatar_saida(self, minutos, segundos):
        """
        função para formatar a saída de dados no formato 'mm:ss', 
        onde 'mm' são os minutos e 'ss' os segundos.
        """
        if (minutos < 10):
            txt_min = '0' + str(minutos)
        else:
            txt_min = str(minutos)
        
        if (segundos < 10):
            txt_seg = '0' + str(segundos)
        else:
            txt_seg = str(segundos)
        
        txt_result = txt_min + ':' + txt_seg
        return txt_result

    def get_tempo(self):
        return self.__formatar_saida(self.min_atual, self.seg_atual)

    def get_label(self):
        return self.label

    def executando(self):
        return self.executando

    def temporizando(self):
        return self.temporizando

    def __printar_saida(self):
        print(self.label + ': ' + self.__formatar_saida(self.min_atual, self.seg_atual))

    def __printar_comandos(self):
        print('espaço -> On/Off\nr -> reinicia o timer\nesc -> finaliza o timer\n')

if __name__ == '__main__':
    temp1 = Temporizador(label='temporizador-1', minutos=1, segundos=0)
    temp1.mudar_status()
    