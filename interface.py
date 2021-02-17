from tkinter import *
from tkinter import ttk
import temporizador as temp
import threading as th
import time

class Interface:
    def __init__(self):
        self.iniciado = False
        
        # self.mudar_status()

        # Root
        self.root = Tk()
        self.root.title('Timer.py')
        root.attributes('-type', 'dialog') # Abre em uma janela no i3-wm
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Variáveis
        self.tempo_atual = StringVar(value='00:00')
        self.texto_botao = StringVar(value='Iniciar')

        # Frame
        self.content = ttk.Frame(self.root, width=200, height=300)
        self.content.grid(column=0, row=0, sticky=(N, E, S, W))

        # Widgets
        self.button = ttk.Button(self.content, textvariable=self.texto_botao, command=self.mudar_status)
        self.txt_temporizador_1 = ttk.Entry(self.content, textvariable=self.tempo_atual, width=5)

        # Showing Widgets
        self.button.grid(column=1, row=1, sticky=(E))
        self.entry.grid(column=2, row=1, sticky=(W))

        # Adding Padding
        for child in self.content.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.iniciar_threads()

    # Funções
    def mudar_status(self):
        if (self.iniciado):
            self.texto_botao.set('Iniciar')
            self.iniciado = False
        else:
            self.texto_botao.set('Parar')
            self.iniciado = True

        # self.temporizador.mudar_status()
    
    # def atualiza_temporizador(self, temporizador):
    #     self.txt_temporizador_1.

    def iniciar_threads(self):
        self.thread_saida = th.Thread(target=self.atualiza_temporizador)
        # self.thread_temporizador = th.Thread(target=self.instanciar_temporizador)

        # self.thread_temporizador.start()
        self.thread_saida.start()

    # def instanciar_temporizador(self):
    #     self.temporizador = temp.Temporizador(segundos=10)

    def iniciar(self):
        self.root.mainloop()

interface = Interface()
interface.iniciar()
# interface.iniciar_threads()

