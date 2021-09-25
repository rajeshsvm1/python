import random
num=random.randint(1,10)
guesses=0
# print(num)
while True:
    a=int(input("Enter the number: "))
    guesses=guesses+1
    if a==num:
        print(f"You have guessed correct number in {guesses} try.")
        break
    elif a>(num):
        print("Guessed number is high")
    else:
        print("Guessed number is lower")