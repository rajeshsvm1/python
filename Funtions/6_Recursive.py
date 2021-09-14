def recurse(n):
    if n<0:
        return 0
    else:
        return (n+(recurse(n-1)))

a=recurse(10)
print(a)