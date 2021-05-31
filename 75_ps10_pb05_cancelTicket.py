
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.available_seats = []
        self.soldSeat = []

        for i in range(1, seats+1):
            self.available_seats.append(i)

    def getStatus(self):
        print("")
        print(f"Name of the train: {self.name}")
        print(f"Fare of the train: {self.fare}")
        print(f"Seats available in the train: {len(self.available_seats)}")
        print("\n")

    def bookTicket(self):
        if len(self.available_seats) != 0:
            print(f"Contrats!!, Your ticket is booked. Your seat no. is {self.available_seats[len(self.available_seats)-1]}") #This will allot available seat from the ending.
            (self.soldSeat).append(self.available_seats[len(self.available_seats)-1])
            self.available_seats.remove(self.available_seats[len(self.available_seats)-1]) #This will remove available seat from the ending.
        else:
            print(f"Sorry!!, No ticket is available. Try in tatkal.")

    def cancelTicket(self, seatNum):
        print(f"cancelliing ticket number: {seatNum}")
        self.soldSeat.remove(seatNum)
        self.available_seats.append(seatNum)

tkt = Train("Rajdhani Express", 500, 3)
tkt.getStatus()
tkt.bookTicket()
tkt.bookTicket()
tkt.bookTicket()
tkt.getStatus()
tkt.cancelTicket(2)
tkt.getStatus()
tkt.cancelTicket(1)
tkt.getStatus()
tkt.bookTicket()
tkt.getStatus()
tkt.bookTicket()
tkt.getStatus()

'''OUTPUT'''

# Name of the train: Rajdhani Express
# Fare of the train: 500
# Seats available in the train: 3


# Contrats!!, Your ticket is booked. Your seat no. is 3   
# Contrats!!, Your ticket is booked. Your seat no. is 2   
# Contrats!!, Your ticket is booked. Your seat no. is 1   

# Name of the train: Rajdhani Express
# Fare of the train: 500
# Seats available in the train: 0


# cancelliing ticket number: 2

# Name of the train: Rajdhani Express
# Fare of the train: 500
# Seats available in the train: 1


# cancelliing ticket number: 1

# Name of the train: Rajdhani Express
# Fare of the train: 500
# Seats available in the train: 2


# Contrats!!, Your ticket is booked. Your seat no. is 1   

# Name of the train: Rajdhani Express
# Fare of the train: 500
# Seats available in the train: 1


# Contrats!!, Your ticket is booked. Your seat no. is 2   

# Name of the train: Rajdhani Express
# Fare of the train: 500
# Seats available in the train: 0
