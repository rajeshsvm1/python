import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="g":
            return True
        else:
            return False
    elif comp=="w":
        if you=="s":
          return True
        else:
            return False
    elif comp=="g":
        if you=="w":
            return True
        else:
            return False



a=random.randint(1,3)
you=input("Your turn: Snake(s) Water(w) Gun(g): ")
if a==1:
    comp="s"
elif a==2:
    comp="w"
else:
    comp="g"
b=gameWin(comp,you)
if b==None:
    print("This game is Tie")
elif b:
    print("you won the game !!")
else:
    print("You loose the game")

print(f"Comp has selected {comp}")
print(f"you have selected {you}")











