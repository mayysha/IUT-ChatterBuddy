import sqlite3

conn = sqlite3.connect('info.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE MESSAGES(
        TO_USER VARCHAR2(100),
        FROM_USER VARCHAR2(100),
        MESSAGE VARCHAR2(100000)
    );
""")
