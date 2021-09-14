with open("log.txt","r") as f:
    data=f.read().lower()
if "java" in data:
    print("python is available in log")
else:
    print("python is not available in log")

