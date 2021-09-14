def fraction(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fraction(n-1)

print(fraction(11))