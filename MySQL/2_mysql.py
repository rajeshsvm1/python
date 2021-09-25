import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="rajesh",passwd="3327912",database="python")

# mycusrsor=mydb.cursor()
# mycusrsor.execute("show databases")
# # multiple execution will not work.

# # userid=mydb.cursor()
# # userid.execute("use ")
# # # print(mycusrsor): multiple commmands will not work.
data=mydb.cursor()
data.execute("select * from shares where percentage between 60 and 100 and hold>3000000 and type='EQ'")
for i in data:
    print(i)