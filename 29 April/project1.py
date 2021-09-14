import random
def game(comp, you):
    if comp==you:
        return None
    elif comp=='g' and you=='s':
        return True
    elif comp=='w'and you=='g':
        return True
    elif comp=='s' and you=='w':
        return True
    else:
        return False
# print("comp turn: snake(s) water(w) gun(g) ?")
randNo=random.randint(1,3)
if randNo==1:
    comp='g'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='s'

you=input("your turn: snake(s) water(w) gun(g) ?")
a=game(comp, you)
if a==None:
    print("game is tie")
elif a:
    print("comp is winner")
else:
    print("you are winner")


