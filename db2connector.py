import pyodbc

import re

con = pyodbc.connect("DSN=(--datasourcename--); UID=; PWD=")

print("Connection succesful")

cur = con.cursor()

cur.execute("Select * from --table--")

table_data = cur.fetchall()

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

for index, column1 in enumerate(table_data):
    if (regex.search(column1[0]) == None):
        print('continue program')
    else:
        re.sub('[@_!#$%^&*()<>?/\|}{~:]', 'NUM', column1[0])
        print('Special Character Removed')

print(table_data)
