import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(15000000)

def natSum(a):
    if a<1:
        return 0
    else:
        return a+(natSum(a-1))

a=natSum(5000)
print(a)