#/usr/bin/env python3
#date1 = (1,2,3)
#date2 = (date1,)
#print(date2)

sql = "select "
paramaters = ("1", "2", "3", 4)
conditions = {'name': '1', 'age': "2"}
data = ()

for i in range(len(paramaters)):
    temp = ", " if i != len(paramaters) - 1 else " "
    sql = sql + str(paramaters[i]) + temp

sql = sql + "from sap "

if len(conditions) != 0:
    tempd = []
    sql = sql + "where "
    kv = list(conditions.items())
    for i in range(len(kv)):
        temp = ", " if i != len(kv) - 1 else " "
        sql = sql + str(kv[i][0]) + " = ?" + temp
        tempd.append(kv[i][1])
    data = tuple(tempd)
print(sql, data)