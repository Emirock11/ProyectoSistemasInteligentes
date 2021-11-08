from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):
        bagsList = []
        mainItems =[]
        self.green="#4FB172"
        self.blue="#538CC0"
        self.red="#CE2644"

    def secondWindow(self):
        root2 = Tk()
        self.window2 = root2
        root2.title("Ingresa los datos de los artículos")
        root2.resizable(False, False)
        root2.geometry("950x540")
        root2.config(bg="#FFFFFF")

        labelWelcome = Label(root2, text="Ingresa los datos de tus bolsas", background=self.green, font=("Arial", 22), foreground="#FFFFFF", width=56, height=1)

        buttonBack = Button(root2, text="< Regresar", font=("Arial", 16), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", width=13, command=self.return2FirstPhase)
        buttonAddItems = Button(root2, text="Agregar producto/s", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF")
        buttonNextWindow = Button(root2, text="Siguiente >", font=("Arial", 16), background=self.blue, foreground="#FFFFFF", border=0, activebackground="#43709A", activeforeground="#FFFFFF", width=13)

        labelWelcome.place(x=0, y=0)


        buttonBack.place(x=110, y=460)
        buttonAddItems.place(x=375, y=460)
        buttonNextWindow.place(x=668, y=460)

    def secondPhase(self):
        self.window1.destroy()
        self.secondWindow()

    def return2FirstPhase(self):
        self.window2.destroy()
        self.start()

    def start(self):
        root1 = Tk()
        self.window1 = root1
        root1.title("Ingresa los datos de las bolsas")
        root1.resizable(False, False)
        root1.geometry("950x540")
        root1.config(bg="#FFFFFF")
        
        labelWelcome = Label(root1, text="Bienvenido, ingresa los datos de tus bolsas", background=self.green, font=("Arial", 22), foreground="#FFFFFF", width=56, height=1)

        labelBagQuantity = Label(root1, text="Ingresa la cantidad de bolsas: ", background="#FFFFFF", font=("Arial", 16))
        entryBagQuantity = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagSize = Label(root1, text="Ingresa el tamaño de las bolsas en centimetros: ", background="#FFFFFF", font=("Arial", 16))
        labelBagLong = Label(root1, text="Largo: ", background="#FFFFFF", font=("Arial", 16))
        entryBagLong = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagHigh = Label(root1, text="Alto: ", background="#FFFFFF", font=("Arial", 16))
        entryBagHigh = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagWidth = Label(root1, text="Ancho: ", background="#FFFFFF", font=("Arial", 16))
        entryBagWidth = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)

        buttonAddBags = Button(root1, text="Agregar bolsas", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF")
        buttonNextWindow = Button(root1, text="Siguiente >", font=("Arial", 16), background=self.blue, foreground="#FFFFFF", border=0, activebackground="#43709A", activeforeground="#FFFFFF", width=13, command=self.secondPhase)
        
        labelWelcome.place(x=0, y=0)
        labelBagQuantity.place(x=30, y=80)
        entryBagQuantity.place(x=320, y=80)
        labelBagSize.place(x=30, y=160)
        labelBagLong.place(x=30, y=210)
        entryBagLong.place(x=100, y=210)
        labelBagHigh.place(x=30, y=260)
        entryBagHigh.place(x=80, y=260)
        labelBagWidth.place(x=30, y=310)
        entryBagWidth.place(x=105, y=310)
        buttonAddBags.place(x=390, y=460)
        buttonNextWindow.place(x=668, y=460)


        root1.mainloop()


initApp = App()

initApp.start()

    