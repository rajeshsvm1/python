a=range(1,51,1)
b=[]
for x in a:
    if x%15==0:
        b.append("FizzBuzz")
    elif x%3==0:
        b.append("Fizz")
    elif x%5==0:
        b.append("Buzz")
    else:
        b.append(x)
print(b)