class Bag:
    def __init__(self, height, length, width):
        self.length = length
        self.height = height
        self.width = width
        self.status = True
        self.weight = 0.0
        self.productList = []

class Product:
    def __init__(self, name, weight, length, height, width, type, fragile, temperature):  
        self.name = name
        self.weight = weight
        self.length = length
        self.height = height
        self.width = width
        self.type = type
        self.fragile = fragile
        self.temperature = temperature


class App:
    def __init__(self):
        self.productTypes = ["Comida / bebida", "Limpieza / aseo personal", "Otro"]
        self.temperaturesList = ["No aplica", "Caliente", "Frio / congelado"]
        self.bagsList = []
        self.allProductsList =[]

    def start(self):
        self.preparedBags =[]
        bag = Bag(10,10,5)
        self.preparedBags.append(bag)
        bag = Bag(10,10,5)
        self.preparedBags.append(bag)
        bag = Bag(10,20,7)
        self.preparedBags.append(bag)
        bag = Bag(20,10,5)
        self.preparedBags.append(bag)
        bag = Bag(15,15,6)
        self.preparedBags.append(bag)
        bag = Bag(25,20,5)
        self.preparedBags.append(bag)
        bag = Bag(15,10,7)
        self.preparedBags.append(bag)

        self.preparedProducts = []
        product = Product("Comida perro", 0.1, 5, 5, 1.5, "Comida / bebida", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Comida perro", 0.1, 5, 5, 1.5, "Comida / bebida", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Comida perro", 0.1, 5, 5, 1.5, "Comida / bebida", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Comida perro", 0.1, 5, 5, 1.5, "Comida / bebida", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Comida perro", 0.1, 5, 5, 1.5, "Comida / bebida", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Comida perro", 0.1, 5, 5, 1.5, "Comida / bebida", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Pollo", 0.5, 30, 12, 14, "Comida / bebida", True, "Caliente")
        self.preparedProducts.append(product)
        product = Product("Pollo", 0.5, 30, 12, 14, "Comida / bebida", True, "Caliente")
        self.preparedProducts.append(product)
        product = Product("refresco", 0.1, 25, 7, 7, "Comida / bebida", False, "Frío")
        self.preparedProducts.append(product)
        product = Product("refresco", 0.1, 25, 7, 7, "Comida / bebida", False, "Frío")
        self.preparedProducts.append(product)
        product = Product("refresco", 0.1, 25, 7, 7, "Comida / bebida", False, "Frío")
        self.preparedProducts.append(product)
        product = Product("refresco", 0.1, 25, 7, 7, "Comida / bebida", False, "Frío")
        self.preparedProducts.append(product)
        product = Product("Cloro", 0.1, 25, 7, 7, "Quimicos", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Shampoo", 0.1, 25, 7, 7, "Otro", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Acondicionador", 0.1, 25, 7, 7, "Otro", False, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Pasta de dientes", 0.05, 2, 10, 3, "Otro", True, "No aplica")
        self.preparedProducts.append(product)
        product = Product("Helado", 0.5, 15, 9, 9, "Comida / bebida", False, "Frío")
        self.preparedProducts.append(product)

        
        self.preparedProducts.sort(key=lambda x: (x.temperature, x.type, x.weight), reverse=True)
        self.preparedBags.sort(key=lambda x: (x.height, x.length, x.width), reverse=True)
        print("--------------------- Productos ---------------------")
        for product in self.preparedProducts:
                print(product.name+" - Peso: "+str(product.weight)+" - Temperatura: "+product.temperature+" - Tipo: "+product.type)

        print("--------------------- BOLSAS ---------------------")
        for bag in self.preparedBags:
                print("Altura: "+str(bag.height)+" - Largo: "+str(bag.length)+" - Ancho: "+str(bag.width))

initApp = App()

initApp.start()