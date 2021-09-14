def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print (greatest(5,6,7))
print (greatest(5,6,2))
print (greatest(99,1,1003))
