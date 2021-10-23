while True:
    try:
        a=int(input("Please enter the number: "))
        b=1/a
        print(b)
        break
    except ValueError:
        print("Error Found")