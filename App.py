from tkinter import *
import random
import math

class Bag:
    def __init__(self, height, length, width):
        self.length = length
        self.height = height
        self.width = width
        self.status = True
        self.weight = 0.0
        self.productList = []
        self.volume = height * length * width

class Bags:
    def __init__(self, quantity, height, length, width):
        self.quantity = quantity
        self.length = length
        self.height = height
        self.width = width

class Product:
    def __init__(self, id, name, weight, price, height, length, width, type, fragile, temperature):  
        self.id = id
        self.name = name
        self.weight = weight
        self.price = price
        self.length = length
        self.height = height
        self.width = width
        self.type = type
        self.fragile = fragile
        self.temperature = temperature
        self.volume = self.height * self.length * self.width

class Products:
    def __init__(self, name, quantity, weight, price, height, length, width, type, fragile, temperature):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.price = price
        self.length = length
        self.height = height
        self.width = width
        self.type = type
        self.fragile = fragile
        self.temperature = temperature
        

class App:
    def __init__(self):
        self.productTypes = ["Comida / Bebida", "Quimicos / Limpieza", "Otro"]
        self.temperaturesList = ["No aplica", "Caliente", "Frio / Congelado"]
        self.bagsList = []
        self.allProductsList =[]
        self.green="#4FB172"
        self.blue="#538CC0"
        self.red="#CE2644"
        self.activeWindow = 0
    
    '''
        EMPIEZAN LOS METODOS PARA LOS PRODUCTOS

    '''
    def getIdFromAList(self, strSearch, list):
        if list == "type":
            for i in range(len(self.productTypes)):
                if self.productTypes[i] == strSearch:
                    return int(i)
        else:
            for i in range(len(self.temperaturesList)):
                if self.temperaturesList[i] == strSearch:
                    return int(i)


    def editODeleteProducts(self, action):
        if len(self.allProductsList) == 0:
            self.hideErrors()
            self.labelErrorEmptyList.place(x=0, y=430)
        else:
            try:
                self.listBoxProducts.get(self.listBoxProducts.curselection())
            except TclError:
                self.hideErrors()
                self.labelErrorNotSelected.place(x=0, y=430)
            else:
                self.hideErrors()
                self.idProducts = self.listBoxProducts.curselection()[0]
                if action == 0:
                    self.entryProductName.delete(0, END)
                    self.entryProductName.insert(0, self.allProductsList[self.idProducts].name)
                    self.entryProductQuantity.delete(0, END)
                    self.entryProductQuantity.insert(0, self.allProductsList[self.idProducts].quantity)
                    self.entryProductPrice.delete(0, END)
                    self.entryProductPrice.insert(0, self.allProductsList[self.idProducts].price)
                    self.entryProductWeight.delete(0, END)
                    self.entryProductWeight.insert(0, self.allProductsList[self.idProducts].weight)
                    self.entryProductLength.delete(0, END)
                    self.entryProductLength.insert(0, self.allProductsList[self.idProducts].length)
                    self.entryProductHeight.delete(0, END)
                    self.entryProductHeight.insert(0, self.allProductsList[self.idProducts].height)
                    self.entryProductWidth.delete(0, END)
                    self.entryProductWidth.insert(0, self.allProductsList[self.idProducts].width)
                    self.varProductType.set(self.productTypes[self.getIdFromAList(self.allProductsList[int(self.idProducts)].type, "type")])
                    
                    self.varProductTemp.set(self.temperaturesList[self.getIdFromAList(self.allProductsList[self.idProducts].temperature, "temperature")])
                    self.showEditButtons()
                else:
                    self.allProductsList.pop(self.idProducts)
                    self.listBoxProducts.delete(ANCHOR)

    def editProducts(self):
        self.editODeleteProducts(0)

    def deleteProducts(self):
        self.editODeleteProducts(1)

    def addProduct(self):
        if self.entryProductName.get() == "t3st":
            self.allProductsList = []
            products = Products("Comida perro", 6, 0.1, 60, 8, 8, 2.5, "Comida / Bebida", False, "No aplica")
            self.allProductsList.append(products)
            products = Products("Bolsas de gomitas", 5, 0.03, 18, 12.5, 8, 2.5, "Comida / Bebida", False, "No aplica")
            self.allProductsList.append(products)
            products = Products("Pollo", 2, 2.5, 120, 14, 30, 12, "Comida / Bebida", True, "Caliente")
            self.allProductsList.append(products)
            products = Products("refresco", 4, 0.6, 25, 13, 7, 7, "Comida / Bebida", False, "Frio / Congelado")
            self.allProductsList.append(products)
            products = Products("Botellas de agua", 25, 0.6, 15, 13, 8, 8, "Comida / Bebida", False, "No aplica")
            self.allProductsList.append(products)
            products = Products("Cloro", 1, 0.95, 50, 28, 8, 8, "Quimicos / Limpieza", False, "No aplica")
            self.allProductsList.append(products)
            products = Products("Shampoo", 1, 0.67, 50, 24.5, 8.5, 6, "Otro", False, "No aplica")
            self.allProductsList.append(products)
            products = Products("Acondicionador", 1, 0.67, 60, 24.5, 8.5, 6, "Otro", False, "No aplica")
            self.allProductsList.append(products)
            products = Products("Pasta de dientes", 2, 0.17, 30, 18, 6, 3.5, "Otro", True, "No aplica")
            self.allProductsList.append(products)
            products = Products("Helado", 1, 0.595, 70, 14.3, 9.8, 9.8, "Comida / Bebida", False, "Frio / Congelado")
            self.allProductsList.append(products)
            products = Products("Palomitas de pollo", 2, 2.5, 120, 8, 12, 12, "Comida / Bebida", True, "Caliente")
            self.allProductsList.append(products)
            self.showObjectsListBox()
            self.hideErrors()
            self.entryProductName.delete(0, END)
            self.entryProductQuantity.delete(0, END)
            self.entryProductPrice.delete(0, END)
            self.entryProductWeight.delete(0, END)
            self.entryProductLength.delete(0, END)
            self.entryProductHeight.delete(0, END)
            self.entryProductWidth.delete(0, END)
            self.varProductType.set(self.productTypes[0])
            self.varProductTemp.set(self.temperaturesList[0])
        elif self.checkData():
            products = Products(self.entryProductName.get(), int(self.entryProductQuantity.get()), float(self.entryProductWeight.get()), float(self.entryProductPrice.get()), float(self.entryProductHeight.get()), float(self.entryProductLength.get()), float(self.entryProductWidth.get()), str(self.varProductType.get()), False, str(self.varProductTemp.get()))
            self.allProductsList.append(products)
            self.hideErrors()
            self.addObject2ListBox()
            self.entryProductName.delete(0, END)
            self.entryProductQuantity.delete(0, END)
            self.entryProductPrice.delete(0, END)
            self.entryProductWeight.delete(0, END)
            self.entryProductLength.delete(0, END)
            self.entryProductHeight.delete(0, END)
            self.entryProductWidth.delete(0, END)
            self.varProductType.set(self.productTypes[0])
            self.varProductTemp.set(self.temperaturesList[0])
    
    def modifyProducts(self):
        if self.checkData():
            IDSelection = self.idProducts
            self.allProductsList[IDSelection].name = str(self.entryProductName.get())
            self.allProductsList[IDSelection].quantity = int(self.entryProductQuantity.get())
            self.allProductsList[IDSelection].price = float(self.entryProductPrice.get())
            self.allProductsList[IDSelection].weight = float(self.entryProductWeight.get())
            self.allProductsList[IDSelection].length = float(self.entryProductLength.get())
            self.allProductsList[IDSelection].height = float(self.entryProductHeight.get())
            self.allProductsList[IDSelection].width = float(self.entryProductWidth.get())
            self.allProductsList[IDSelection].type = str(self.varProductType.get())
            self.allProductsList[IDSelection].temperature = str(self.varProductTemp.get())
            self.listBoxProducts.delete(0, END)
            self.showObjectsListBox()
            self.returnToAdd()

    '''
        TERMINAN LOS METODOS PARA LOS PRODUCTOS

    '''

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
        self.entryProductName = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=17)
        labelProductQuantity = Label(root2, text="Cantidad: ", background="#FFFFFF", font=("Arial", 16))
        self.entryProductQuantity = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductPrice = Label(root2, text="Precio: ", background="#FFFFFF", font=("Arial", 16))
        self.entryProductPrice = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=6)
        labelProductWeight = Label(root2, text="Ingresa peso aprox. del producto en Kg: ", background="#FFFFFF", font=("Arial", 16))
        self.entryProductWeight = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=5)
        labelProductSize = Label(root2, text="Ingresa tamaño aprox. del producto en cm: ", background="#FFFFFF", font=("Arial", 16))
        labelProductHeight = Label(root2, text="Altura: ", background="#FFFFFF", font=("Arial", 16))
        self.entryProductHeight = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductLength = Label(root2, text="Largo: ", background="#FFFFFF", font=("Arial", 16))
        self.entryProductLength = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductWidth = Label(root2, text="Ancho: ", background="#FFFFFF", font=("Arial", 16))
        self.entryProductWidth = Entry(root2, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=4)
        labelProductType = Label(root2, text="Tipo de producto: ", background="#FFFFFF", font=("Arial", 16))
        self.varProductType = StringVar(root2)
        self.varProductType.set(self.productTypes[0])
        menuProductType = OptionMenu(root2, self.varProductType, *self.productTypes)
        menuProductType.config(width=21, font=("Arial", 10))
        labelProductTemp = Label(root2, text="Temperatura de producto: ", background="#FFFFFF", font=("Arial", 16))
        self.varProductTemp = StringVar(root2)
        self.varProductTemp.set(self.temperaturesList[0])
        menuProductTemp = OptionMenu(root2, self.varProductTemp, *self.temperaturesList)
        menuProductTemp.config(width=21, font=("Arial", 10))
        labelBGList = Label(root2, text="BG", width=60, height=22, background=self.green)
        labelProductsEntered = Label(root2, text="Productos ingresados", background="#DDF5F4", font=("Arial", 13), width=46)
        self.listBoxProducts = Listbox(root2, width=52, height=16, highlightcolor=self.green, highlightthickness=2, background="#DDF5F4", border=0, font=("Arial", 11))
        
        buttonEditProducts = Button(root2, text="Editar producto/s", font=("Arial", 12), background="#26BDB4", foreground="#FFFFFF", border=0, activebackground="#53C0BA", activeforeground="#FFFFFF", command=self.editProducts)
        buttonDeleteProducts = Button(root2, text="Eliminar producto/s", font=("Arial", 12), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", command=self.deleteProducts)
        self.labelErrorMissing = Label(root2, text="Falta uno o más datos para ingresar productos.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        self.labelErrorEmptyList = Label(root2, text="No hay productos en la lista.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        self.labelErrorNotSelected = Label(root2, text="Selecciona un dato de la lista de productos.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)
        self.labelErrorValue = Label(root2, text="Se deben ingresar solamente numeros con o sin punto decimal en las casillas de los tamaños y cantidades.", font=("Arial", 12), width=105, background="#FFFFFF", foreground=self.red)

        self.buttonBack = Button(root2, text="< Regresar", font=("Arial", 16), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", width=13, command=self.return2FirstPhase)
        self.buttonAddItems = Button(root2, text="Agregar producto/s", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF", command=self.addProduct)
        self.buttonModifyProduct = Button(root2, text="Modificar producto/s", font=("Arial", 16), background=self.green, foreground="#FFFFFF", border=0, activebackground="#0F861A", activeforeground="#FFFFFF", command=self.modifyProducts)
        self.buttonCancelProduct = Button(root2, text="Cancelar", font=("Arial", 16), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", width=13, command=self.returnToAdd)
        buttonNextWindow = Button(root2, text="Siguiente >", font=("Arial", 16), background=self.blue, foreground="#FFFFFF", border=0, activebackground="#43709A", activeforeground="#FFFFFF", width=13, command=self.thirdPhase)

        labelWelcome.place(x=0, y=0)
        labelProductName.place(x=30, y=63)
        self.entryProductName.place(x=30, y=95)
        labelProductQuantity.place(x=272, y=60)
        self.entryProductQuantity.place(x=369, y=60)
        labelProductPrice.place(x=272, y=100)
        self.entryProductPrice.place(x=347, y=100)
        labelProductWeight.place(x=30, y=155)
        self.entryProductWeight.place(x=410, y=155)
        labelProductSize.place(x=30, y=210)
        labelProductHeight.place(x=30, y=245)
        self.entryProductHeight.place(x=99, y=245)
        labelProductLength.place(x=168, y=245)
        self.entryProductLength.place(x=235, y=245)
        labelProductWidth.place(x=303, y=245)
        self.entryProductWidth.place(x=375, y=245)
        labelProductType.place(x=30, y=308)
        menuProductType.place(x=200, y=308)
        labelProductTemp.place(x=30, y=367)
        menuProductTemp.place(x=280, y=367)
        labelBGList.place(x=515, y=61)
        labelProductsEntered.place(x=518, y=68)
        self.listBoxProducts.place(x=518, y=99)

        buttonEditProducts.place(x=580, y=400)
        buttonDeleteProducts.place(x=750, y=400)
        self.buttonBack.place(x=110, y=460)
        self.buttonAddItems.place(x=375, y=460)
        buttonNextWindow.place(x=668, y=460)

        self.showObjectsListBox()
        self.hideErrors()


    '''
        EMPIEZAN LOS METODOS PARA EL MOVIMIENTO ENTRE VENTANAS
    
    '''

    def secondPhase(self):
        if len(self.bagsList) > 0:
            self.window1.destroy()
            self.secondWindow()
        else:
            self.hideErrors()
            self.labelErrorEmptyList.place(x=0, y=430)

    def thirdPhase(self):
        if len(self.allProductsList) == 0:
            self.hideErrors()
            self.labelErrorEmptyList.place(x=0, y=430)
        else:
            self.prepareBags()
            self.prepareProducts()
            self.preparedBags.sort(key=lambda x: x.volume, reverse=True)
            self.totalProducts = len(self.preparedProducts)
            self.remainingFoodProducts = []
            self.hotProducts = []
            self.popList = []
            

            for i in range(len(self.preparedProducts)):
                if self.preparedProducts[i].temperature == "Caliente":
                    self.hotProducts.append(self.preparedProducts[i])
                    self.popList.append(i)
                elif self.preparedProducts[i].temperature == "Frio / Congelado" or self.preparedProducts[i].type == "Comida / Bebida":
                    self.remainingFoodProducts.append(self.preparedProducts[i])
                    self.popList.append(i)
            
            if len(self.popList) > 0:
                i = len(self.popList)-1
                while i >= 0:
                    self.preparedProducts.pop(self.popList[i])
                    i = i-1

            for i in range(len(self.preparedBags)):
                self.hillClimbing(i)

            print("--------------------- BOLSAS ---------------------")
            for bag in self.preparedBags:
                    print("Altura: "+str(bag.height)+" - Largo: "+str(bag.length)+" - Ancho: "+str(bag.width) + " - Volumen: "+str(bag.volume) + " - Peso: "+str(bag.weight) + " - Cantidad de productos: "+str(len(bag.productList)) + " - Status: "+str(bag.status))
            
            self.window2.destroy()
            self.thirdWindow()


    def return2FirstPhase(self):
        self.window2.destroy()
        self.start()
    
    def return2SecondPhase(self):
        self.window3.destroy()
        self.secondWindow()

    def startAllOverAgain(self):
        self.bagsList = []
        self.allProductsList =[]
        self.window3.destroy()
        self.start()


    '''
        TERMINAN LOS METODOS PARA EL MOVIMIENTO ENTRE VENTANAS
    
    '''

    
    '''
        EMPIEZAN LOS METODOS PARA ACCIONES DE LAS VENTANAS 1 Y 2

    '''

    def hideErrors(self):
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
        elif self.activeWindow == 2:
            if len(self.entryProductName.get()) == 0 or len(self.entryProductQuantity.get()) == 0 or len(self.entryProductWeight.get()) == 0 or len(self.entryProductPrice.get()) == 0 or len(self.entryProductLength.get()) == 0 or len(self.entryProductHeight.get()) == 0 or len(self.entryProductWidth.get()) == 0:
                self.hideErrors()
                self.labelErrorMissing.place(x=0, y=430)
                return False
            elif not self.checkIfNotStr():
                self.hideErrors()
                self.labelErrorValue.place(x=0, y=430)
                return False
            return True
        

    def checkIfNotStr(self):
        
        try:
            if self.activeWindow == 1:
                float(self.entryBagQuantity.get())
                float(self.entryBagLength.get())
                float(self.entryBagHeight.get())
                float(self.entryBagWidth.get())
            else:
                float(self.entryProductQuantity.get())
                float(self.entryProductWeight.get())
                float(self.entryProductPrice.get())
                float(self.entryProductLength.get())
                float(self.entryProductHeight.get())
                float(self.entryProductWidth.get())
        except ValueError:
            return False
        else:
            return True

    def showObjectsListBox(self):
        if self.activeWindow == 1: 
            if len(self.bagsList) > 0:
                for bag in self.bagsList:
                    strBag = str(bag.quantity)+" bolsa/s, altura: "+str(bag.height)+" cm, largo: "+str(bag.length)+" cm, ancho: "+str(bag.width)+" cm."
                    self.listBoxBags.insert("end", strBag)
        elif self.activeWindow == 2:
            if len(self.allProductsList) > 0:
                for product in self.allProductsList:
                    strProd = product.name+" Cantidad: "+str(product.quantity)+"."
                    self.listBoxProducts.insert("end", strProd)
        elif self.activeWindow == 3:
            if len(self.preparedProducts) > 0:
                for product in self.preparedProducts:
                    strProd = product.name+"."
                    self.listBoxProducts2.insert("end", strProd)
            if len(self.remainingFoodProducts) > 0:
                for product in self.remainingFoodProducts:
                    strProd = product.name+"."
                    self.listBoxProducts2.insert("end", strProd)
            if len(self.hotProducts) > 0:
                for product in self.hotProducts:
                    strProd = product.name+"."
                    self.listBoxProducts2.insert("end", strProd)
            for bag in self.preparedBags:
                if len(bag.productList) == 0:
                    strBag = str(bag.height)+" X "+str(bag.length)+" X "+str(bag.width)
                    self.listBoxProducts3.insert("end", strBag)
            currentBag = self.preparedBags[0]
            strBag ="Bolsa: Alt: " + str(currentBag.height)+" Larg: "+str(currentBag.length)+" Ach: "+str(currentBag.width)
            self.labelProductsEntered4.config(text=strBag)
            if len(currentBag.productList) > 0:
                for product in currentBag.productList:
                    strProd = product.name+"."
                    self.listBoxProducts4.insert("end", strProd)
            
            
                

                

    def addObject2ListBox(self):
        if self.activeWindow == 1:
            strBag = str(self.entryBagQuantity.get())+" bolsa/s, altura: "+str(self.entryBagHeight.get())+" cm, largo: "+str(self.entryBagLength.get())+" cm, ancho: "+str(self.entryBagWidth.get())+" cm."
            self.listBoxBags.insert(END, strBag)
        elif self.activeWindow == 2:
            strProd = str(self.entryProductName.get())+" - Cantidad: "+str(self.entryProductQuantity.get())+"."
            self.listBoxProducts.insert(END, strProd)

    def showEditButtons(self):
        if self.activeWindow == 1:
            self.buttonAddBags.place_forget()
            self.buttonModifyBags.place(x=390, y=460)
            self.buttonCancelBags.place(x=110, y=460)
        elif self.activeWindow == 2:
            self.buttonAddItems.place_forget()
            self.buttonBack.place_forget()
            self.buttonModifyProduct.place(x=390, y=460)
            self.buttonCancelProduct.place(x=110, y=460)
    
    def hideEditButtons(self):
        if self.activeWindow == 1:
            self.buttonAddBags.place(x=390, y=460)
            self.buttonModifyBags.place_forget()
            self.buttonCancelBags.place_forget()
        elif self.activeWindow == 2:
            self.buttonAddItems.place(x=390, y=460)
            self.buttonBack.place(x=110, y=460)
            self.buttonModifyProduct.place_forget()
            self.buttonCancelProduct.place_forget()

    def returnToAdd(self):
        if self.activeWindow == 1:
            self.entryBagQuantity.delete(0, END)
            self.entryBagLength.delete(0, END)
            self.entryBagHeight.delete(0, END)
            self.entryBagWidth.delete(0, END)
            self.listBoxBags.selection_clear(0, END)
            self.hideEditButtons()
        elif self.activeWindow == 2:
            self.entryProductName.delete(0, END)
            self.entryProductQuantity.delete(0, END)
            self.entryProductWeight.delete(0, END)
            self.entryProductPrice.delete(0, END)
            self.entryProductLength.delete(0, END)
            self.entryProductHeight.delete(0, END)
            self.entryProductWidth.delete(0, END)
            self.varProductType.set(self.productTypes[0])
            self.varProductTemp.set(self.temperaturesList[0])
            self.listBoxProducts.selection_clear(0, END)
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
        labelBagHeight = Label(root1, text="Altura: ", background="#FFFFFF", font=("Arial", 16))
        self.entryBagHeight = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
        labelBagLength = Label(root1, text="Largo: ", background="#FFFFFF", font=("Arial", 16))
        self.entryBagLength = Entry(root1, highlightthickness=2, highlightcolor=self.green, font=("Arial", 16), width=7)
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
        labelBagHeight.place(x=30, y=210)
        self.entryBagHeight.place(x=100, y=210)
        labelBagLength.place(x=30, y=260)
        self.entryBagLength.place(x=100, y=260)
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
        if self.entryBagQuantity.get() == "test":
            self.bagsList = []
            bags = Bags(2, 30, 30, 10)
            self.bagsList.append(bags)
            bags = Bags(3, 40, 30, 10)
            self.bagsList.append(bags)
            self.showObjectsListBox()
            self.hideErrors()
            self.entryBagQuantity.delete(0,"end")
            self.entryBagLength.delete(0,"end")
            self.entryBagHeight.delete(0,"end")
            self.entryBagWidth.delete(0,"end")
        elif self.checkData():
            bags = Bags(int(self.entryBagQuantity.get()), float(self.entryBagHeight.get()), float(self.entryBagLength.get()), float(self.entryBagWidth.get()))
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

    def prepareBags(self):
        self.preparedBags = []
        for i in range(len(self.bagsList)):
            currentBag = self.bagsList[i]
            for j in range(currentBag.quantity):
                bag = Bag(currentBag.height, currentBag.length, currentBag.width)
                self.preparedBags.append(bag)

    def prepareProducts(self):
        self.preparedProducts = []
        id = 0
        for i in range(len(self.allProductsList)):
            currentProduct = self.allProductsList[i]
            for j in range(currentProduct.quantity):
                product = Product(id, currentProduct.name, currentProduct.weight, currentProduct.price, currentProduct.height, currentProduct.length, currentProduct.width, currentProduct.type, currentProduct.fragile, currentProduct.temperature)
                self.preparedProducts.append(product)
                id+=1
    
    def hillClimbing(self, idxBag):
        # Este metodo retorna una solucion inicial
        # Se obtiene la bolsa que se esta rellenando
        currentBag = self.preparedBags[idxBag]
        preparedProducts = self.preparedProducts
        remainingFoodProducts = self.remainingFoodProducts
        hotProducts = self.hotProducts
        c = 0
        # Este booleano sirve para saber si hay algun producto nuevo a ingresar dentro de la bolsa, ni no lo hay
        # y ya recorrio la lista, entonces se sale del while
        noMoreProducts = False
        # Mientras que la lista de los otros productos esté llena y la bolsa esté disponible...
        while len(preparedProducts)> 0 and currentBag.status:
            if len(preparedProducts)<= 0 or noMoreProducts:
                break
            # Se tiene una lista random...
            index = 0
            bestValue = 0
            noMoreProducts = True
            # Obtenemos el objeto con mayor valor monetario
            for i in range(len(preparedProducts)):
                # Se guarda el producto en la variable "selectedProduct"
                selectedProduct = preparedProducts[i]
                # Se calcula el nuevo peso de la bolsa con el producto
                newWeight = currentBag.weight + selectedProduct.weight
                # Se calcula el nuevo volumen de la bolsa con el producto
                newVolume = currentBag.volume - selectedProduct.volume
                # Se obtiene un booleano si entra o no el producto dentro de la bolsa...
                enters = self.enters(selectedProduct, currentBag.height, currentBag.length, currentBag.width)
                # Si el precio del producto es mayor al mejor valor guardado,
                # si el producto puede entrar a la bolsa,
                # si el nuevo peso de la bolsa no pasa de los 8 kilos,
                # y si el nuevo volumen no es negativo...
                if selectedProduct.price > bestValue and enters and newWeight <= 8.0 and newVolume >= 0:
                    # Se guarda el valor de la posición del producto que se encuentra dentro de la
                    # lista "preparedProducts"
                    index = i
                    # Se establece un nuevo mejor valor
                    bestValue = selectedProduct.price
                    noMoreProducts = False
                    c+=1
            bestProduct = preparedProducts[index]
            # Una vez que se tenga el producto con mayor valor, se evalua si se ingresará dentro de la bolsa...
            # Se calcula el nuevo peso de la bolsa con el producto
            newWeight = currentBag.weight + bestProduct.weight
            # Se calcula el nuevo volumen de la bolsa con el producto
            newVolume = currentBag.volume - bestProduct.volume
            # Se calcula si el objeto entra a la bolsa o no...
            enters = self.enters(bestProduct, currentBag.height, currentBag.length, currentBag.width)
            if enters and newWeight <= 8.0 and newVolume >= 0 and not noMoreProducts:
                # Se ingresa el producto a la bolsa
                currentBag.productList.append(bestProduct)
                # Se actualiza el peso de la bolsa...
                currentBag.weight = newWeight
                # se actualiza el volumen de la bolsa...
                currentBag.volume = newVolume
                # Se elimina el producto de la lista "preparedProducts"
                preparedProducts.pop(index)
            # Se repite el procedimiento hasta que se acaba la lista
            else:
                break

        noMoreProducts = False

        # Mientras que la lista de los productos de comida restantes esté llena y la bolsa esté disponible...
        while len(remainingFoodProducts)> 0 and currentBag.status:
            if len(remainingFoodProducts)<= 0 or noMoreProducts:
                break
            # Se tiene una lista random...
            index = 0
            bestValue = 0
            noMoreProducts = True
            # Obtenemos el objeto con mayor valor monetario
            for i in range(len(remainingFoodProducts)):
                # Se guarda el producto en la variable "selectedProduct"
                selectedProduct = remainingFoodProducts[i]
                # Se calcula el nuevo peso de la bolsa con el producto
                newWeight = currentBag.weight + selectedProduct.weight
                # Se calcula el nuevo volumen de la bolsa con el producto
                newVolume = currentBag.volume - selectedProduct.volume
                # Se obtiene un booleano si entra o no el objeto dentro de la bolsa...
                enters = self.enters(remainingFoodProducts[i], currentBag.height, currentBag.length, currentBag.width)
                # Si el precio del producto es mayor al mejor valor guardado,
                # si el producto puede entrar a la bolsa,
                # si el nuevo peso de la bolsa no pasa de los 8 kilos,
                # y si el nuevo volumen no es negativo...
                if selectedProduct.price > bestValue and enters and newWeight <= 8.0 and newVolume >= 0:
                    # Se guarda el valor de la posición del producto que se encuentra dentro de la
                    # lista "remainingFoodProducts"
                    index = i
                    # Se establece un nuevo mejor valor
                    bestValue = remainingFoodProducts[i].price
                    noMoreProducts = False
            bestProduct = remainingFoodProducts[index]
            # Una vez que se tenga el producto con mayor valor, se evalua si se ingresará dentro de la bolsa...
            # Se calcula el nuevo peso de la bolsa con el producto
            newWeight = currentBag.weight + bestProduct.weight
            # Se calcula el nuevo volumen de la bolsa con el producto
            newVolume = currentBag.volume - bestProduct.volume
            # Se calcula si el objeto entra a la bolsa o no...
            enters = self.enters(bestProduct, currentBag.height, currentBag.length, currentBag.width)
            if enters and newWeight <= 8.0 and newVolume >= 0 and not noMoreProducts:
                # Se ingresa el producto a la bolsa
                currentBag.productList.append(bestProduct)
                # Se actualiza el peso de la bolsa...
                currentBag.weight = newWeight
                # se actualiza el volumen de la bolsa...
                currentBag.volume = newVolume
                # Se elimina el producto de la lista "remainingFoodProducts"
                remainingFoodProducts.pop(index)
                # Se repite el procedimiento hasta que se acaba la lista
            else:
                break

        noMoreProducts = False

        # Mientras que la lista de los productos calientes esté llena y la bolsa esté disponible...
        while len(hotProducts)> 0 and currentBag.status:
            if len(hotProducts)<= 0 or noMoreProducts:
                break
            # Se tiene una lista random...
            index = 0
            bestValue = 0
            noMoreProducts = True
            # Obtenemos el objeto con mayor valor monetario
            for i in range(len(hotProducts)):
                # Se guarda el producto en la variable "selectedProduct"
                selectedProduct = hotProducts[i]
                # Se calcula el nuevo peso de la bolsa con el producto
                newWeight = currentBag.weight + selectedProduct.weight
                # Se calcula el nuevo volumen de la bolsa con el producto
                newVolume = currentBag.volume - selectedProduct.volume
                # Se obtiene un booleano si entra o no el objeto dentro de la bolsa...
                enters = self.enters(hotProducts[i], currentBag.height, currentBag.length, currentBag.width)
                # Si el precio del producto es mayor al mejor valor guardado,
                # si el producto puede entrar a la bolsa,
                # si el nuevo peso de la bolsa no pasa de los 8 kilos,
                # y si el nuevo volumen no es negativo...
                if selectedProduct.price > bestValue and enters and newWeight <= 8.0 and newVolume >= 0:
                    # Se guarda el valor de la posición del producto que se encuentra dentro de la
                    # lista "hotProducts"
                    index = i
                    # Se establece un nuevo mejor valor
                    bestValue = hotProducts[i].price
                    noMoreProducts = False
            bestProduct = hotProducts[index]
            # Una vez que se tenga el producto con mayor valor, se evalua si se ingresará dentro de la bolsa...
            # Se calcula el nuevo peso de la bolsa con el producto
            newWeight = currentBag.weight + bestProduct.weight
            # Se calcula el nuevo volumen de la bolsa con el producto
            newVolume = currentBag.volume - bestProduct.volume
            # Se calcula si el objeto entra a la bolsa o no...
            enters = self.enters(bestProduct, currentBag.height, currentBag.length, currentBag.width)
            if enters and newWeight <= 8.0 and newVolume >= 0 and not noMoreProducts:
                # Se ingresa el producto a la bolsa
                currentBag.productList.append(bestProduct)
                # Se actualiza el peso de la bolsa...
                currentBag.weight = newWeight
                # se actualiza el volumen de la bolsa...
                currentBag.volume = newVolume
                # Se elimina el producto de la lista "hotProducts"
                hotProducts.pop(index)
                # Se repite el procedimiento hasta que se acaba la lista
            else:
                break
            
        # Se regresa la solucion inicial
        currentBag.status = False
        return currentBag

    def enters(self, product, height, length, width):
        
        if product.height <= height and product.length <= length and product.width <= width:
            return True
        elif product.height <= height and product.width <= length and product.length <= width:
            return True
        elif product.length <= height and product.height <= length and product.width <= width:
            return True
        elif product.width <= height and product.height <= length and product.length <= width:
            return True
        elif product.length <= height and product.width <= length and product.height <= width:
            return True
        elif product.width <= height and product.length <= length and product.height <= width:
            return True
        elif product.length <= height and product.height <= length and product.width <= width:
            return True
        elif product.length <= height and product.width <= length and product.height <= width:
            return True
        elif product.height <= height and product.length <= length and product.width <= width:
            return True
        elif product.width <= height and product.length <= length and product.height <= width:
            return True
        elif product.height <= height and product.width <= length and product.length <= width:
            return True
        elif product.width <= height and product.height <= length and product.length <= width:
            return True
        elif product.width <= height and product.height <= length and product.length <= width:
            return True
        elif product.width <= height and product.length <= length and product.height <= width:
            return True
        elif product.height <= height and product.width <= length and product.length <= width:
            return True
        elif product.length <= height and product.width <= length and product.height <= width:
            return True
        elif product.height <= height and product.length <= length and product.width <= width:
            return True
        elif product.length <= height and product.height <= length and product.width <= width:
            return True
        else:
            return False

    def thirdWindow(self):
        self.activeWindow = 3
        root3 = Tk()
        self.window3 = root3
        root3.title("Bolsas organizadas")
        root3.resizable(False, False)
        root3.geometry("950x540")
        root3.config(bg="#FFFFFF")
        self.actualBag = 0


        labelWelcome = Label(root3, text="Bolsas organizadas", background=self.green, font=("Arial", 22), foreground="#FFFFFF", width=56, height=1)
        self.labelBGList2 = Label(root3, text="BG", width=38, height=12, background=self.green)
        self.labelProductsEntered2 = Label(root3, text="Productos no ingresados", background="#DDF5F4", font=("Arial", 13), width=28)
        self.listBoxProducts2 = Listbox(root3, width=32, height=8, highlightcolor=self.green, highlightthickness=2, background="#DDF5F4", border=0, font=("Arial", 11))
        self.labelBGList3 = Label(root3, text="BG", width=38, height=9, background=self.green)
        self.labelProductsEntered3 = Label(root3, text="Bolsas sin utilizar", background="#DDF5F4", font=("Arial", 13), width=28)
        self.listBoxProducts3 = Listbox(root3, width=32, height=5, highlightcolor=self.green, highlightthickness=2, background="#DDF5F4", border=0, font=("Arial", 11))
        self.labelBGList4 = Label(root3, text="BG", width=38, height=22, background=self.green)
        self.labelProductsEntered4 = Label(root3, text="Productos ingresados", background="#DDF5F4", font=("Arial", 13), width=28)
        self.listBoxProducts4 = Listbox(root3, width=32, height=16, highlightcolor=self.green, highlightthickness=2, background="#DDF5F4", border=0, font=("Arial", 11))

        self.buttonLastBag = Button(root3, text="< Anterior", font=("Arial", 12), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", command=self.moveToLastBag)
        self.buttonNextBag = Button(root3, text="Siguiente >", font=("Arial", 12), background="#26BDB4", foreground="#FFFFFF", border=0, activebackground="#53C0BA", activeforeground="#FFFFFF", command=self.moveToNextBag)

        self.buttonBack = Button(root3, text="< Regresar", font=("Arial", 16), background=self.red, foreground="#FFFFFF", border=0, activebackground="#981930", activeforeground="#FFFFFF", width=13, command=self.return2SecondPhase)
        buttonNextWindow = Button(root3, text="Empezar de nuevo", font=("Arial", 16), background=self.blue, foreground="#FFFFFF", border=0, activebackground="#43709A", activeforeground="#FFFFFF", width=15, command=self.startAllOverAgain)

        labelWelcome.place(x=0, y=0)
        self.labelBGList2.place(x=138, y=64)
        self.labelProductsEntered2.place(x=144, y=68)
        self.listBoxProducts2.place(x=143, y=99)
        self.labelBGList3.place(x=138, y=254)
        self.labelProductsEntered3.place(x=144, y=261)
        self.listBoxProducts3.place(x=143, y=294)
        self.labelBGList4.place(x=535, y=61)
        self.labelProductsEntered4.place(x=541, y=68)
        self.listBoxProducts4.place(x=540, y=99)

        
        self.buttonBack.place(x=110, y=460)
        buttonNextWindow.place(x=645, y=460)

        self.showObjectsListBox()
        self.checkMovementButtons()

    def checkMovementButtons(self):
        cantidadBolsas = len(self.preparedBags)
        if self.actualBag == cantidadBolsas-1:
            self.buttonNextBag.place_forget()
        else:
            if len(self.preparedBags[self.actualBag+1].productList) == 0:
                self.buttonNextBag.place_forget()
            else:
                self.buttonNextBag.place(x=690, y=400)
        
        if self.actualBag == 0:
            self.buttonLastBag.place_forget()
        else:
            self.buttonLastBag.place(x=565, y=400)
            

    def showBagInList(self):
        self.listBoxProducts4.delete(0, END)
        currentBag = self.preparedBags[self.actualBag]
        strBag ="Bolsa: " + str(currentBag.height)+" X "+str(currentBag.length)+" X "+str(currentBag.width)
        self.labelProductsEntered4.config(text=strBag)
        if len(currentBag.productList) > 0:
            for product in currentBag.productList:
                strProd = product.name+"."
                self.listBoxProducts4.insert("end", strProd)

    def moveToNextBag(self):
        self.actualBag = self.actualBag + 1
        self.checkMovementButtons()
        self.showBagInList()
    
    def moveToLastBag(self):
        self.actualBag = self.actualBag - 1
        self.checkMovementButtons()
        self.showBagInList()






initApp = App()

initApp.start()

    