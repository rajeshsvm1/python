# def game():
#     return 465
# user=game()
with open("hiscore.txt","r") as f:
    user=int(input("user hi-score: "))
    hi=(f.read())
    if hi=="":
        with open("hiscore.txt","w") as f:
            f.write(str(user))
    elif user>int(hi):
        with open("hiscore.txt","w") as f:
            f.write(str(user))
    else:
        pass
# with open("hiscore.txt","w") as f:
# user=int(input("user hi-score: "))
# a=str(user)
# f.write(a)

