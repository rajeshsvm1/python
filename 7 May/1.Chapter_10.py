class Employee:
    company="bakerhughes"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"{self.name} is in {self.company} company, working for {self.product} product.")
rajesh=Employee("rajesh","gas turbine")
rajesh.getInfo()

