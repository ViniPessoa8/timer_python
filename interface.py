from tkinter import *
from mttkinter import mtTkinter
import temporizador as temp
import threading as th
import time

class Interface:
    def __init__(self, temporizador):
        self.executando = True
        self.iniciado = False
        self.temporizador = temporizador

        # self.mudar_status()

        # Root
        self.root = mtTkinter.Tk()
        self.root.title('Timer.py')
        self.root.protocol('WM_DELETE_WINDOW', self.__del__)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        #Variáveis
        self.tempo_atual = StringVar(value=temporizador.get_tempo())
        self.texto_botao = StringVar(value='Iniciar')

        # Frame
        self.content = Frame(self.root, width=200, height=300)
        self.content.grid(column=0, row=0, sticky=(N, E, S, W))

        # Widgets
        self.button = Button(self.content, textvariable=self.texto_botao, command=self.mudar_status)
        self.txt_temporizador_1 = Label(self.content, textvariable=self.tempo_atual, width=5)
        

        # Showing Widgets
        self.button.grid(column=1, row=1, sticky=(E))
        self.txt_temporizador_1.grid(column=2, row=1, sticky=(W))

        # Adding Padding
        for child in self.content.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.inicia_threads()

    # Funções
    def mudar_status(self):
        if (self.iniciado):
            self.texto_botao.set('Iniciar')
            self.iniciado = False
        else:
            self.temporizador.mudar_status()
            self.texto_botao.set('Parar')
            self.iniciado = True

        print('[DEBUG] iniciado = false')

    def atualiza_tempo(self, tempo):
        self.tempo_atual.set(tempo)

    # Threads
    def t_atualiza_tempo(self):
        # print('[DEBUG] t_atualiza_tempo')
        while(self.executando):
            # print('[DEBUG] t_atualiza_tempo EXECUTANDO')
            while (self.iniciado):
                # print('[DEBUG] t_atualiza_tempo INICIADO')

                # Codigo para atualizar thread a partir do temporizador instanciado
                self.atualiza_tempo(self.temporizador.get_tempo())

    def inicia_threads(self):
        # print('[DEBUG] inicia-threads')
        self.t_atualiza_tempo = th.Thread(target=self.t_atualiza_tempo)
        self.t_atualiza_tempo.start()
        self.iniciar()

    def __del__(self):
        # print('[DEBUG] __del__')
        self.temporizador.finalizar()
        self.rodando = False
        self.executando = False
        # print('[DEBUG] rodando = false')
        try:
            self.root.destroy()
        except:
            pass

    # Main
    def iniciar(self):
        # print('[DEBUG] iniciar()')
        self.root.mainloop()

if __name__ == '__main__':

    t = temp.Temporizador(segundos=20)
    interface = Interface(t)

