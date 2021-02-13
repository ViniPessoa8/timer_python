from tkinter import *
from mttkinter import mtTkinter
import temporizador as temp
import threading as th
import time

class Interface:
    def __init__(self, temporizador):
        self.executando = True
        self.temporizando = False
        self.temporizador = temporizador

        # self.mudar_status()

        # Root
        self.root = mtTkinter.Tk()
        self.root.title('Timer.py')
        self.root.protocol('WM_DELETE_WINDOW', self.__del__)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Variáveis
        self.tempo_atual = StringVar(value=temporizador.get_tempo())
        self.texto_botao = StringVar(value='Iniciar')

        # Frame
        self.content = Frame(self.root, width=200, height=300)
        self.content.grid(column=0, row=0, sticky=(N, E, S, W))

        # Imagens
        self.restart_icon = PhotoImage(file='./media/restart_icon_20px.png')

        # Widgets
        self.b_iniciar = Button(self.content, textvariable=self.texto_botao, command=self.mudar_status)
        self.txt_temporizador_1 = Label(self.content, textvariable=self.tempo_atual, width=5)
        self.b_reiniciar = Button(self.content, command=self.reinicia_temporizador, image=self.restart_icon)

        # Mostrando os Widgets
        self.b_iniciar.grid(column=1, row=1, sticky=(E))
        self.txt_temporizador_1.grid(column=2, row=1, sticky=(W, E))
        self.b_reiniciar.grid(column=3, row=1, sticky=(W))

        # Configurações Adicionais
        self.b_reiniciar['state'] = DISABLED
        for child in self.content.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.inicia_threads()

    # Funções
    def mudar_status(self):
        self.b_reiniciar['state'] = NORMAL
        if (self.temporizando):
            self.texto_botao.set('Iniciar')
            self.temporizando = False
            self.temporizador.mudar_status()
        else:
            self.temporizador.mudar_status()
            self.texto_botao.set('Parar')
            self.temporizando = True

    def iniciar_temporizador(self):
        self.texto_botao.set('Iniciar') 
        self.temporizando = False
        self.b_reiniciar['state'] = NORMAL

    def para_temporizador(self):
        self.b_iniciar['state'] = DISABLED
        self.temporizando = False

    def finaliza_temporizador(self):
        self.temporizador.mudar_status()
        self.texto_botao.set('Parar')
        self.temporizando = True

    def atualiza_tempo(self, tempo):
        self.tempo_atual.set(tempo)

    def reinicia_temporizador(self):
        self.temporizando = False
        self.texto_botao.set('Iniciar')

        self.b_reiniciar['state'] = DISABLED
        self.b_iniciar['state'] = NORMAL

        self.temporizador.reiniciar()
        self.tempo_atual.set(self.temporizador.get_tempo())

    # Threads
    def t_atualiza_tempo(self):
        while(self.executando):
            while (self.temporizando):
                # Codigo para atualizar thread a partir do temporizador instanciado
                temporizador_tempo = self.temporizador.get_tempo()
                self.atualiza_tempo(temporizador_tempo)
                if (temporizador_tempo == '00:00'):
                    print('para_temporizador()')
                    self.para_temporizador()

    def inicia_threads(self):
        self.t_atualiza_tempo = th.Thread(target=self.t_atualiza_tempo)
        self.t_atualiza_tempo.start()
        self.iniciar()

    def __del__(self):
        self.temporizador.finalizar()
        self.rodando = False
        self.executando = False
        try:
            self.root.destroy()
        except:
            pass

    # Main
    def iniciar(self):
        self.root.mainloop()

if __name__ == '__main__':

    t = temp.Temporizador(segundos=2)
    interface = Interface(t)