import os
with open("renamed.txt","r") as f:
    data=f.read()
with open("renamed2.txt","w") as f:
    f.write(data)
os.remove("renamed.txt")

