a=[1,2,3,4,5,6]
b=[]
for x in a:
    if x==3 or x==6:
        continue
    b.append(x)
print(b)