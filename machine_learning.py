import sqlite3

conn = sqlite3.connect('info.db')

c = conn.cursor()

# c.execute("""
#     CREATE TABLE LEARNING (
#         QUESTION VARCHAR2(1000),
#         ANSWER VARCHAR2(100)
#     );
# """)

dict = {}

line = """
    SELECT QUESTION, ANSWER
    FROM LEARNING
"""

c.execute(line)

messages = c.fetchall()

for i in range(len(messages)):
    question = messages[i][0]
    answer = messages[i][1]

    dict.update({question: answer})

print(dict)