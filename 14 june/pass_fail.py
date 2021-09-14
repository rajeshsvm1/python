sub1=int(input("please enter sub1 marks: "))
sub2=int(input("please enter sub2 marks: "))
sub3=int(input("please enter sub3 marks: "))
b=((sub1+sub2+sub3)/3)
if sub1>=33 and sub2>=33 and sub3>=33 and b>=40:
    print("student is pass")
else:
    print("student is fail")