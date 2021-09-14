with open("pythonpresent.txt","r") as f:
    data1=f.read()
with open("copy.txt","r") as f:
    data2=f.read()
if data1==data2:
    print("both files are same")
else:
    print("both files are not same")