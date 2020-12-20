import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE EMPLOYEES (
#             FIRST VARCHAR2(100),
#             LAST VARCHAR2(100),
#             PAY NUMBER
#             );""")

# c.execute("INSERT INTO EMPLOYEES VALUES('RAFID', 'HAQUE', 10000000);")

c.execute("SELECT * FROM EMPLOYEES WHERE LAST = 'HAQUE'")

print(c.fetchall())

conn.commit()

conn.close()
