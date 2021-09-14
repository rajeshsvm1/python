class RailwayForm:
    def __init__(self,train,seats,fare):
        self.train=train
        self.seats=seats
        self.seatlist=list(range(1,(seats+1))) # seats = list(range(1, 5))
        self.a=len(self.seatlist)
        self.new=[]
        self.fare=fare
    def getInfo(self):
        print(f"Train Name: {self.train}, Seat Available: {self.new}, Fare: {self.fare}")
    def bookTicket(self):
        if self.seats<1:
            print("seat is not available")
        else:
            for i in (self.seatlist):
                self.new=self.seatlist.pop()
                print(self.seatlist)
                print(self.a)

    def cancelTicket(self):
        pass
rajesh=RailwayForm("Rajdhani",10,296)
rajesh.getInfo()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.bookTicket()
rajesh.bookTicket()

rajesh.getInfo()