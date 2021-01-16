import time
import tkinter as tk

class App:
    
    def __init__(self, master=None):
        
        self.segundosTimer = 58
        self.minutosTimer = 0
        self.horasTimer = 0

        # self.segundosTimer.set('00')
        # self.minutosTimer.set('00')
        # self.horasTimer.set('00')

        # Cria o widget 1
        self.widget1 = tk.Frame(master)
        self.widget1['bg'] = 'white'
        self.widget1.pack(expand=1)

        self.contador = tk.Frame(self.widget1)
        self.contador['bg'] = 'white'
        self.contador.pack(ipady=30)

        # --- Contador ---
        self.horasTimerEntrada = tk.Entry(self.contador, width=2, font=("Arial",18,""), ,textvariable=self.formatarNumero(self.horasTimer))
        self.horasTimerEntrada.
        # hourEntry.place(x=80,y=20)
        self.horasTimerEntrada.pack(side='left', padx=5)

        labelDoisPontos1 = tk.Label(self.contador, text=':')
        labelDoisPontos1['bg'] = 'white'
        labelDoisPontos1['font'] = 'TkTextFont'
        labelDoisPontos1['fg'] = 'black'
        labelDoisPontos1.pack(side='left')
        
        self.minutosTimerEntrada = tk.Entry(self.contador, width=2, font=("Arial",18,""), textvariable=self.formatarNumero(self.minutosTimer))
        self.minutosTimerEntrada.pack(side='left', padx=5)

        labelDoisPontos2 = tk.Label(self.contador, text=':')
        labelDoisPontos2['bg'] = 'white'
        labelDoisPontos2['font'] = 'TkTextFont'
        labelDoisPontos2['fg'] = 'black'
        labelDoisPontos2.pack(side='left')
        
        self.segundosTimerEntrada = tk.Entry(self.contador, width=2, font=("Arial",18,""), textvariable=self.formatarNumero(self.segundosTimer))
        self.segundosTimerEntrada.pack(side='left', padx=5)

        # Cria botão de Iniciar
        self.btnMudarTexto = tk.Button(self.widget1)
        self.btnMudarTexto['text'] = 'Iniciar'
        # self.btnMudarTexto["font"] = ("Calibri", "10")
        # self.btnMudarTexto["width"] = 5
        self.btnMudarTexto.bind("<Button-1>", self.iniciarTimer)
        self.btnMudarTexto.pack()

        # Cria o botão de sair
        self.sair = tk.Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack ()

    def iniciarTimer(arg1, arg2):
        timerIniciado = True
        while (timerIniciado):
          arg1.mostrarTempo(arg1)
          arg1.passarTempo()
          time.sleep(1)
          

    def passarTempo(self):
        # A cada segundo
        self.segundosTimer += 1
        if (self.segundosTimer == 60):
            self.segundosTimer = 0
            self.minutosTimer += 1

        if (self.minutosTimer == 60):
            self.minutosTimer = 0
            self.horasTimer += 1

        if (self.horasTimer == 24):
            self.horasTimer = 0

        self.atualizaContador()

    def formatarNumero(self, num):
        if (num < 10):
            return '0'+str(num)
        return str(num)

    def mostrarTempo(arg1, arg2):
        print(''+ arg1.formatarNumero(arg1.horasTimer) + ':' + arg1.formatarNumero(arg1.minutosTimer) + ':' + arg1.formatarNumero(arg1.segundosTimer))

    def atualizaContador(self):
        print(self.horasTimerEntrada.get())
        self.horasTimerEntrada.setvar(value=self.formatarNumero(self.horasTimer))

        # print('teste')
        # print(arg1, arg2)
        # print(arg1.segundosTimer.get())
        # print(arg1.minutosTimer.get())

        # print(arg2)
        # print(self.horasTimer)
    
    def formatTimer(arg1):
        print(arg1)
        return '-'

# Cria a janela Tk
root = tk.Tk()

# Configurações da janela Tk
root.configure(bg='white')
# root.geometry('200x150')

# Instancía o programa
App(root)

# Inicia o programa
root.mainloop()