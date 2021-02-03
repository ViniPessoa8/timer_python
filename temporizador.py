import time
import os
import threading as th
import keyboard
import datetime
import math 

class Temporizador:
    def __init__(self, master=None):
        self.parar()

    def temporizar(self, minutos, segundos, label):
        """
        função que inicia um temporizador, dado os minutos e segundos como parâmetros
        """
        self.rodando = True

        print('Temporizando ' + self.formatar_saida(minutos,segundos))
        print(label + ': ' + self.formatar_saida(minutos,segundos))
        
        while (self.rodando):
            if (segundos > 0):
                segundos -= 1
            elif (minutos > 0):
                minutos -= 1
                segundos = 59
            else:
                self.parar()
                print("Fim!")

            time.sleep(1)
            print(label + ': ' + self.formatar_saida(minutos,segundos))
        
    def ler_entrada(self):
        """
        função que monitora o teclado e para o timer caso o usuário tecle 'Esc' 
        """
        keyboard.add_hotkey('esc', self.parar)

    def iniciar_threads(self):
        """
        função que inicia todas as threads
        """
        self.inicia_thread_timer(1,0,'a') # Thread de timer em um minuto (01:00) 
        
        # Thread para ler a entrada do usuário enquanto o timer é executado
        tInput = th.Thread(target=self.ler_entrada)
        tInput.start()

    def inicia_thread_timer(self, mins, secs, label):
        """
        Inicia uma thread que instancia um timer com o tempo fornecido
        
        mins = minutos 
        secs = segundos
        label = texto indetificador de cada Thread
        """
        t = th.Thread(target=self.temporizar, args=(mins, secs, label))
        t.start()

    def formatar_saida(self, minutos, segundos):
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

    def parar(self):
        """
        função que para todos os timers
        """
        self.rodando = False

    def main(self):
        """
        função principal
        """
        self.iniciar_threads()

if __name__ == '__main__':
    temp1 = Temporizador()

    temp1.main()