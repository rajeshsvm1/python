class RailwayForm:
    def __init__(self,train,seats,fare):
        self.train=train
        self.seats=seats
        self.seatlist=list(range(1,(seats+1))) # seats = list(range(1, 5))
        self.fare=fare
    def getInfo(self):
        print(f"Train Name: {self.train}, Seat Available: {self.seats}, Fare: {self.fare}")
        # print(self.seatlist)
    def bookTicket(self):
        if self.seats<1:
            print("seat is not available")
        else:
            print(f"your seat no is {self.seatlist[-1]}")

            self.seatlist.pop()
            self.seats=len(self.seatlist)

    def cancelTicket(self):
        self.ticketNo=int(input("enter your ticket number: "))
        self.seatlist.append(self.ticketNo)
        self.seats=len(self.seatlist)
        

rajesh=RailwayForm("Rajdhani",20,296)
rajesh.getInfo()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.getInfo()
rajesh.cancelTicket()
rajesh.cancelTicket()
rajesh.getInfo()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.bookTicket()



