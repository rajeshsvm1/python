# with open("replace.txt","w") as f:
#     f.write("donkey\n")
#     f.write("mango\n")
#     f.write("book\n")
#     f.write("laptop\n")
words=["donkey","mango","laptop","book"]
with open("replace.txt","r") as f:
    data=f.read()
for i in words:
    data=data.replace(i,"@#$$#")
    
# data=data.replace("donkey","#######")
# data=data.replace("mango","#######")
# data=data.replace("laptop","#######")

with open("replace.txt","w") as f:
    f.write(data)

    


