class employee:
    company="microsoft"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
    def getInfo(self):
        return (f"{self.name} is working in {self.company} with salary {self.salary} in product {self.subunit}")

rajesh=employee("Rajesh",1000,"skype")
print(rajesh.getInfo())
print(rajesh.company)

