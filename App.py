from tkinter import *

class Bags:
    def __init__(self, quantity, length, height, width, status):
        self.quantity = quantity
        self.length = length
        self.height = height
        self.width = width
        self.status = status
    
        

class App:
    def __init__(self):
        self.productTypes = ["Pasta", "Semillas", "Carne", "Fruta/verdura", "Embotellado", "Limpieza / aseo personal", "Caja"]
        self.temperaturesList = ["Frio / congelado", "Caliente", "No aplica"]
        self.bagsList = []
        self.mainItems =[]
        self.green="#4FB172"
        self.blue="#538CC0"
        self.red="#CE2644"
        self.activeWindow = 0

    def secondWindow(self):
        self.activeWindow = 2
        root2 = Tk()
        self.window2 = root2
        root2.title("Ingresa los datos de los productos")
        root2.resizable(False, False)
        root2.geometry("950x540")
        root2.config(bg="#FFFFFF")

        labelWelcome = Label(root2, text="Ingresa los productos a comprar", background=self.green, font=("Arial", 22), foreground="#FFFFFF", width=56, height=1)
        labelProductName = Label(root2, text="Nombre del producto: ", background="#FFFFFF", font=("Arial", 16))
        entryProductName = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=17)
        labelProductQuantity = Label(root2, text="Cantidad: ", background="#FFFFFF", font=("Arial", 16))
        entryProductQuantity = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductWeight = Label(root2, text="Ingresa peso aprox. del producto en Kg: ", background="#FFFFFF", font=("Arial", 16))
        entryProductWeight = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductSize = Label(root2, text="Ingresa tamaño aprox. del producto en cm: ", background="#FFFFFF", font=("Arial", 16))
        labelProductLong = Label(root2, text="Largo: ", background="#FFFFFF", font=("Arial", 16))
        entryProductLong = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductHeight = Label(root2, text="Alto: ", background="#FFFFFF", font=("Arial", 16))
        entryProductHeight = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductWidth = Label(root2, text="Ancho: ", background="#FFFFFF", font=("Arial", 16))
        entryProductWidth = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductType = Label(root2, text="Tipo de producto: ", background="#FFFFFF", font=("Arial", 16))
        varProductType = StringVar(root2)
        varProductType.set(self.productTypes[0])
        menuProductType = OptionMenu(root2, varProductType, *self.productTypes)
        menuProductType.config(width=21, font=("Arial", 10))
        checkBProductType = Checkbutton(root2, text="Fragil", font=("Arial", 12), background="#FFFFFF", activebackground="#FFFFFF")

        labelProductTemp = Label(root2, text="Temperatura de producto: ", background="#FFFFFF", font=("Arial", 16))
        varProductTemp = StringVar(root2)
        varProductTemp.set(self.temperaturesList[0])
        menuProductTemp = OptionMenu(root2, varProductTemp, *self.temperaturesList)
        menuProductTemp.config(width=21, font=("Arial", 10))

        buttonBack = Button(root2, text="< Regresar", font=("Arial", 16), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", width=13, command=self.return2FirstPhase)
        buttonAddItems = Button(root2, text="Agregar producto/s", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF")
        buttonNextWindow = Button(root2, text="Siguiente >", font=("Arial", 16), background=self.blue, foreground="#FFFFFF", border=0, activebackground="#43709A", activeforeground="#FFFFFF", width=13)

        labelWelcome.place(x=0, y=0)
        labelProductName.place(x=30, y=63)
        entryProductName.place(x=30, y=95)
        labelProductQuantity.place(x=272, y=80)
        entryProductQuantity.place(x=369, y=80)
        labelProductWeight.place(x=30, y=155)
        entryProductWeight.place(x=410, y=155)
        labelProductSize.place(x=30, y=210)
        labelProductLong.place(x=30, y=245)
        entryProductLong.place(x=99, y=245)
        labelProductHeight.place(x=168, y=245)
        entryProductHeight.place(x=217, y=245)
        labelProductWidth.place(x=293, y=245)
        entryProductWidth.place(x=365, y=245)
        labelProductType.place(x=30, y=308)
        menuProductType.place(x=200, y=308)
        checkBProductType.place(x=400, y=310)
        labelProductTemp.place(x=30, y=367)
        menuProductTemp.place(x=280, y=367)



        buttonBack.place(x=110, y=460)
        buttonAddItems.place(x=375, y=460)
        buttonNextWindow.place(x=668, y=460)

    '''
        EMPIEZAN LOS METODOS PARA EL MOVIMIENTO ENTRE VENTANAS
    
    '''

    def secondPhase(self):
        self.window1.destroy()
        self.secondWindow()

    def return2FirstPhase(self):
        self.window2.destroy()
        self.start()

    '''
        TERMINAN LOS METODOS PARA EL MOVIMIENTO ENTRE VENTANAS
    
    '''

    
    '''
        EMPIEZAN LOS METODOS PARA ACCIONES DE LAS VENTANAS 1 Y 2

    '''

    def hideErrors(self):
        if self.activeWindow == 1:
            self.labelErrorValue.place_forget()
            self.labelErrorMissing.place_forget()
            self.labelErrorEmptyList.place_forget()
            self.labelErrorNotSelected.place_forget()
        
    def checkData(self):
        if self.activeWindow == 1:
            if len(self.entryBagQuantity.get()) == 0 or len(self.entryBagLength.get()) == 0 or len(self.entryBagHeight.get()) == 0 or len(self.entryBagWidth.get()) == 0:
                self.hideErrors()
                self.labelErrorMissing.place(x=0, y=430)
                return False
            elif not self.checkIfNotStr():
                self.hideErrors()
                self.labelErrorValue.place(x=0, y=430)
                return False
            return True

    def checkIfNotStr(self):
        if self.activeWindow == 1:
            try:
                float(self.entryBagQuantity.get())
                float(self.entryBagLength.get())
                float(self.entryBagHeight.get())
                float(self.entryBagWidth.get())
            except ValueError:
                return False
            else:
                return True

    def showObjectsListBox(self):
        if self.activeWindow == 1:
            if len(self.bagsList) > 0:
                for bag in self.bagsList:
                    strBag = str(bag.quantity)+" bolsa/s, largo: "+str(bag.length)+" cm, alto: "+str(bag.height)+" cm, ancho: "+str(bag.width)+" cm."
                    self.listBoxBags.insert("end", strBag)

    def addObject2ListBox(self):
        if self.activeWindow == 1:
            strBag = str(self.entryBagQuantity.get())+" bolsa/s, largo: "+str(self.entryBagLength.get())+" cm, alto: "+str(self.entryBagHeight.get())+" cm, ancho: "+str(self.entryBagWidth.get())+" cm."
            self.listBoxBags.insert(END, strBag)

    def showEditButtons(self):
        if self.activeWindow == 1:
            self.buttonAddBags.place_forget()
            self.buttonModifyBags.place(x=390, y=460)
            self.buttonCancelBags.place(x=110, y=460)
    
    def hideEditButtons(self):
        if self.activeWindow == 1:
            self.buttonAddBags.place(x=390, y=460)
            self.buttonModifyBags.place_forget()
            self.buttonCancelBags.place_forget()

    def returnToAdd(self):
        if self.activeWindow == 1:
            self.entryBagQuantity.delete(0, END)
            self.entryBagLength.delete(0, END)
            self.entryBagHeight.delete(0, END)
            self.entryBagWidth.delete(0, END)
            self.listBoxBags.selection_clear(0, END)
            self.hideEditButtons()

    '''
        TERMINAN LOS METODOS PARA ACCIONES DE LAS VENTANAS 1 Y 2

    '''

    def start(self):
        self.activeWindow = 1
        root1 = Tk()
        self.window1 = root1
        root1.title("Ingresa los datos de las bolsas")
        root1.resizable(False, False)
        root1.geometry("950x540")
        root1.config(bg="#FFFFFF")
        
        labelWelcome = Label(root1, text="Bienvenido, ingresa los datos de tus bolsas", background=self.green, font=("Arial", 22), foreground="#FFFFFF", width=56, height=1)

        labelBagQuantity = Label(root1, text="Ingresa la cantidad de bolsas: ", background="#FFFFFF", font=("Arial", 16))
        self.entryBagQuantity = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagSize = Label(root1, text="Ingresa el tamaño de las bolsas en centimetros: ", background="#FFFFFF", font=("Arial", 16))
        labelBagLong = Label(root1, text="Largo: ", background="#FFFFFF", font=("Arial", 16))
        self.entryBagLength = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagHigh = Label(root1, text="Alto: ", background="#FFFFFF", font=("Arial", 16))
        self.entryBagHeight = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagWidth = Label(root1, text="Ancho: ", background="#FFFFFF", font=("Arial", 16))
        self.entryBagWidth = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBGList = Label(root1, text="BG", width=60, height=22, background=self.green)
        labelBagsEntered = Label(root1, text="Bolsas ingresadas", background="#DDF5F4", font=("Arial", 13), width=46)
        self.listBoxBags = Listbox(root1, width=52, height=16, highlightcolor=self.green, highlightthickness=2, background="#DDF5F4", border=0, font=("Arial", 11))
        

        self.labelErrorMissing = Label(root1, text="Falta uno o más datos para ingresar bolsas.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        self.labelErrorEmptyList = Label(root1, text="No hay bolsas en la lista.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        self.labelErrorNotSelected = Label(root1, text="Selecciona un dato de la lista de bolsas.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        self.labelErrorValue = Label(root1, text="Se deben ingresar solamente numeros con o sin punto decimal en las casillas de los tamaños y cantidades.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        buttonEditBags = Button(root1, text="Editar bolsa/s", font=("Arial", 12), background="#26BDB4", foreground="#FFFFFF", border=0, activebackground="#53C0BA", activeforeground="#FFFFFF", command=self.editBags)
        buttonDeleteBags = Button(root1, text="Eliminar bolsa/s", font=("Arial", 12), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", command=self.deleteBags)
        self.buttonAddBags = Button(root1, text="Agregar bolsa/s", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF", command=self.addBags)
        self.buttonModifyBags = Button(root1, text="Modificar bolsa/s", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF", command=self.modifyBags)
        self.buttonCancelBags = Button(root1, text="Cancelar", font=("Arial", 16), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", width=13, command=self.returnToAdd)        
        buttonNextWindow = Button(root1, text="Siguiente >", font=("Arial", 16), background=self.blue, foreground="#FFFFFF", border=0, activebackground="#43709A", activeforeground="#FFFFFF", width=13, command=self.secondPhase)
        
        labelWelcome.place(x=0, y=0)
        labelBagQuantity.place(x=30, y=80)
        self.entryBagQuantity.place(x=320, y=80)
        labelBagSize.place(x=30, y=160)
        labelBagLong.place(x=30, y=210)
        self.entryBagLength.place(x=100, y=210)
        labelBagHigh.place(x=30, y=260)
        self.entryBagHeight.place(x=80, y=260)
        labelBagWidth.place(x=30, y=310)
        self.entryBagWidth.place(x=105, y=310)
        labelBGList.place(x=515, y=61)
        labelBagsEntered.place(x=518, y=68)
        self.listBoxBags.place(x=518, y=99)
        
        buttonEditBags.place(x=600, y=400)
        buttonDeleteBags.place(x=740, y=400)
        self.buttonAddBags.place(x=390, y=460)
        buttonNextWindow.place(x=668, y=460)

        self.showObjectsListBox()
        self.hideErrors()
        

        root1.mainloop()

    '''
        INICIAN LOS METODOS PARA LAS ACCIONES DE LAS BOLSAS

    '''

    def editODeleteBags(self, action):
        if len(self.bagsList) == 0:
            self.hideErrors()
            self.labelErrorEmptyList.place(x=0, y=430)
        else:
            try:
                self.listBoxBags.get(self.listBoxBags.curselection())
            except TclError:
                self.hideErrors()
                self.labelErrorNotSelected.place(x=0, y=430)
            else:
                self.hideErrors()
                self.idBags = self.listBoxBags.curselection()[0]
                if action == 0:
                    self.entryBagQuantity.delete(0, END)
                    self.entryBagQuantity.insert(0, self.bagsList[self.idBags].quantity)
                    self.entryBagLength.delete(0, END)
                    self.entryBagLength.insert(0, self.bagsList[self.idBags].length)
                    self.entryBagHeight.delete(0, END)
                    self.entryBagHeight.insert(0, self.bagsList[self.idBags].height)
                    self.entryBagWidth.delete(0, END)
                    self.entryBagWidth.insert(0, self.bagsList[self.idBags].width)
                    self.showEditButtons()
                else:
                    self.bagsList.pop(self.idBags)
                    self.listBoxBags.delete(ANCHOR)

    def editBags(self):
        self.editODeleteBags(0)

    def deleteBags(self):
        self.editODeleteBags(1)

    def addBags(self):
        if self.checkData():
            bags = Bags(int(self.entryBagQuantity.get()), float(self.entryBagLength.get()), float(self.entryBagHeight.get()), float(self.entryBagWidth.get()), True)
            self.bagsList.append(bags)
            self.hideErrors()
            self.addObject2ListBox()
            self.entryBagQuantity.delete(0,"end")
            self.entryBagLength.delete(0,"end")
            self.entryBagHeight.delete(0,"end")
            self.entryBagWidth.delete(0,"end")

    def modifyBags(self):
        if self.checkData():
            IDSelection = self.idBags
            self.bagsList[IDSelection].quantity = int(self.entryBagQuantity.get())
            self.bagsList[IDSelection].length = float(self.entryBagLength.get())
            self.bagsList[IDSelection].height = float(self.entryBagHeight.get())
            self.bagsList[IDSelection].width = float(self.entryBagWidth.get())
            self.listBoxBags.delete(0, END)
            self.showObjectsListBox()
            self.returnToAdd()

    '''
        TERMINAN LOS METODOS PARA LAS ACCIONES DE LAS BOLSAS

    '''


initApp = App()

initApp.start()

    