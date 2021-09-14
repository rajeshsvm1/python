# E pattern

# for i in range(8):
#     for j in range(8):
#         if (i==0 or i==7 or i==1 or i==6) or (j==0 or j==1) or (i==3 and j==2) or (i==4 and j==2) or (i==3 and j==3) or (i==4 and j==3):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print(" ")


# # D Pattern
# for i in range(7):
#     for j in range(6):
#         if (j<4 and i==0) or (j<4 and i==6) or j==0 or ((i>0 and i<6) and j==5):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print(" ")

# 20. Write a Python program to print alphabet pattern 'G'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
for i in range(7):
    for j in range(4):
        if (i>1):
            print("*",end="")
        else:
            print(" ")
    print("")