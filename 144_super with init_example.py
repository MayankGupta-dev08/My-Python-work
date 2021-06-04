class Vehicle:
    def __init__(self, price, v_type, wheels):
        self.price = price
        self.v_type = v_type
        self.wheels = wheels
        self.colour = "Black"

    def v_info(self):
        print("Type: " + self.v_type + "\ncolour: " + self.colour + "\n Wheels: " + str(self.wheels))


class Bike(Vehicle):

    def __init__(self, price, model):
        super().__init__(price, "Bike", 2)
        self.model = model

    def info(self):
        print("model: " + self.model + "\n price: Rs." + str(self.price) + "\n Type: " + self.v_type + "\n Wheels: " + str(self.wheels) + "colour: " + self.colour) 


class Car(Vehicle):

    def __init__(self, price, model):
        super().__init__(price, "Car", 4)
        self.model = model

    def info(self):
        print("model: " + self.model + "\n price: Rs." + str(self.price) + "\n Type: " + self.v_type + "\n Wheels: " + str(self.wheels) + "colour: " + self.colour) 


b1 = Bike(30000, "Honda")
b2 = Bike(50000, "Karisma")
b3 = Bike(100000, "Kawasaki")
c1 = Car(900000, "Amaze")
c2 = Car(500000, "Baleno")
c3 = Car(100000, "Wagonr")


b1.info()
b2.info()
b3.info()
print("")
c1.info()
c2.info()
c3.info()
print("")
b1.v_info()
c1.v_info()