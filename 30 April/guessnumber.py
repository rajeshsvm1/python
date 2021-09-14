import random
user=int(input("enter the number between 1 to 10 : "))
randno=random.randint(1,10)
print(f"correct number is {randno}")
if randno==user:
    print(f"guessed number is {user}")
    print("you have guessed correct number !")
elif user>randno:
    print(f"guessed number is {user}")

    print("entered number is HI")
else:
    print(f"guessed number is {user}")

    print("entered number is LOW")

