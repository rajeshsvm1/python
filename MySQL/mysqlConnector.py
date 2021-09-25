import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="rajesh",passwd="3327912",database="python")

# mycusrsor=mydb.cursor()
# mycusrsor.execute("show databases")
# # multiple execution will not work.

# # userid=mydb.cursor()
# # userid.execute("use ")
# # # print(mycusrsor): multiple commmands will not work.
mycusrsor=mydb.cursor()
mycusrsor.execute("select* from persons where name=('rajesh')")
# m=[]
print("id and name")
for i in mycusrsor:
    # m.append(i)
    print(i)
#     for j in range (len(i)):
#         c=i[j]
#         m.append(c)
# print(m)
print("city name")
userid=mydb.cursor()
userid.execute("select city from persons where city NOT IN ('ranchi')")
c=[]
for i in userid:
    for j in range (len(i)):
        if i[j] not in c:
            c.append(i[j])
print(c)

    