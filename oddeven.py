b=int(input("enter start number: \n"))
c=int(input("enter end number: \n"))
odd=[]
even=[]
for a in range(b,c+1):
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
print("odd", len(odd))
print("even", len(even))