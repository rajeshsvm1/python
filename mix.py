a="Python 3.2"
b=[]
c=[]
for x in a:
    if x.isdigit():
        b.append(x)
    elif x.isalpha():
        c.append(x)

print(len(b))
print(len(c))
        