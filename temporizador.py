import time
import os
import threading as th
import keyboard
import datetime
import math

class Temporizador:
    def __init__(self, master=None, stopkey='space', label='-', minutos=0, segundos=0, log_dict={}, func_log=None):
        # Instanciação das variáveis
        self.executando = True
        self.temporizando = False
        self.reiniciado = False
        self.parado = False
        self.l_dict = {'log_dict': log_dict}
        self.log = func_log

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

    def mudar_status(self):
        self.temporizando = not self.temporizando

        if (self.temporizando):
            self.log('[TEMPORIZADOR] Ativado!')
        else:
            self.log('[TEMPORIZADOR] Pausado!')

    def reiniciar(self):
        self.executando = True
        self.temporizando = False
        self.reiniciado = True
        self.parado = False
        
        self.min_atual = self.min_inic
        self.seg_atual = self.seg_inic

    def __temporizar(self):
        """ 
        função que inicia o temporizador
        """
        # self.log('[TEMPORIZADOR] __temporizar()')
        while(self.executando):
            while(self.temporizando and not self.parado):
                time.sleep(1)
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
                    self.parado = True
                    self.log("[TEMPORIZADOR] Fim!")

    def finalizar(self):
        self.temporizando = False
        self.executando = False
        self.log('[TEMPORIZADOR] Finalizado!')

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

if __name__ == '__main__':
    temp1 = Temporizador(label='temporizador-1', minutos=1, segundos=0)
    temp1.mudar_status()
    