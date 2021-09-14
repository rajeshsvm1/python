content="true"
i=1
with open("log.txt","r") as f:
    while content:
        content=f.readline().lower()
        if "python" in content:
            print(content)
            print(f"python is present in line {i}\n")
        i=i+1

