import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='',
                              host='127.0.0.1',
                              database='py_crud')


cursor = cnx.cursor()

# cursor.execute("SELECT * FROM pessoa")

# print(cursor.fetchall())

# cnx.close()

# costumerList = []
# query = ("SELECT * FROM pessoa")
# cursor.execute(query)
# #print(cursor.fetchall())
# for row in cursor.fetchall():
#     print (row)
#     costumerList.append([row[0],row[1],row[2],row[3]])

# print (costumerList)
