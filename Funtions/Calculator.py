def sum(a,b):
    return (f"Total sum = {a+b}")
def sub(a,b):
    return (f"Substraction = {a-b}")
def mul(a,b):
    return(f"Multiplication = {a*b}")
def div(a,b):
    return (f"Division = {a/b}")
while True:
    func=input("Welcome to Rajesh's calculator\nfor addition,press +\nfor subtraction,press -\nfor multiplication,press *\nfor Division,press /\nTo exit,press e\n: ")
    if func=="e":
        print("*****Thanks for Using*****")
        break
    else:
        a1=int(input("enter first num: "))
        a2=int(input("enter second num: "))
        if func=="+":
            print("******************************************")
            print(sum(a1,a2))
            print("******************************************")
        elif func=="-":
            print("******************************************")
            print(sub(a1,a2))
            print("******************************************")
        elif func=="*":
            print("******************************************")
            print(mul(a1,a2))
            print("******************************************")
        elif func=="/":
            print("******************************************")
            print(div(a1,a2))
            print("******************************************")
# need to add error handling program