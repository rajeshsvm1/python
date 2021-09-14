# with open("multiplication of 2",'w') as f:
#     for i in range(1,11):
#         f.write(f"{2}x{i}={2*i}\n")
       
#     # # b=("{2}x{i}={a}")
    
#     #     f.write(str(a))

for i in range(2,21):
    with open(f"Multitable of {i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")
         