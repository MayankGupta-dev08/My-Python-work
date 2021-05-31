class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print("*****************")
        print(f"Name of the train: {self.name}")
        print(f"Fare of the train: {self.fare}")
        print(f"Seats available in the train: {self.seats}")
        print("*****************\n")

    def bookTicket(self):
        if self.seats>0:
            print(f"Contrats!!, Your ticket is booked. Your seat no. is {self.seats}")
            self.seats -= 1
        else:
            print(f"Sorry!!, No ticket is available. Try in tatkal.")

tkt = Train("Rajdhani Express", 500, 3)
tkt.getStatus()
tkt.bookTicket()
tkt.bookTicket()
tkt.bookTicket()
tkt.bookTicket()
tkt.getStatus()
