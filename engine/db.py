import sqlite3
conn = sqlite3.connect("Alexa.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# #TO INSERT SYSTME APP
# query = "INSERT INTO sys_command VALUES (null,'Excel','C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# #TO INSERT web app ENTRY
query = "INSERT INTO web_command VALUES (null,'instagram','https://www.instagram.com/')"
cursor.execute(query)
conn.commit()

#TO DELETE ENTRY
# query = "DELETE FROM sys_command WHERE id = 2"
# cursor.execute(query)
# conn.commit()