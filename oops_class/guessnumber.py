import random
num=random.randint(1,10)
# print(num)
while True:
    a=int(input("Enter the number: "))
    if a==num:
        print("You have guessed correct number")
        break
    elif a>(num):
        print("Guessed number is high")
    else:
        print("Guessed number is lower")