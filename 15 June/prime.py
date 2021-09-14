num=int(input("please enter your number: "))
flag=False
for n in range(2,num):
    if num%n==0:
        flag=True
        break
if flag:
    print("not prime")
else:
    print("prime")
