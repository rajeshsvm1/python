f=open("poems.txt","r")
data=f.readline()
if "twinkle" in data:
    print ("Yes")
else:
    print("No")    
f.close()
