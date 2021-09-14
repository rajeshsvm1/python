a=int(input("num a :"))
b=int(input("num b :"))
c=int(input("num c :"))
d=int(input("num d :"))

if (a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c)
else:
    print(d)

