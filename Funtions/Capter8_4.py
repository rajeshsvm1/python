# a=int(input("Enter the number: "))
def pattern(a):
    for i in range(a,0,-1):
        for j in range(0,i):
            print("*",end="")
        print()

pattern(3)