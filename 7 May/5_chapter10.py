class Train:
    def __init__(self,name,status,fare):
        self.name=name
        self.status=status
        self.fare=fare
    def getInfo(self):
        print(f"Train number is {self.name}")
        print(f"Seat Availability {self.status}")
        print(f"Fare is {self.fare}")
    def bookTicket(self):
        if self.status>0:
            print(f"Ticket confirmed ! your seat number is {self.status}")
            self.status=self.status-1
        else:
            print("seat is not available")   
intercity=Train("17775",1,300)
intercity.getInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
