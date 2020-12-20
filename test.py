import csv

usernames = {}
with open('info.csv', 'r') as read_file:
    reader = csv.reader(read_file)
    line = 0
    for row in reader:
        if line == 0:
            line += 1
            continue
        if len(row) == 0:
            continue
        else:
            usernames.update( {row[1]: row[2]} )

print(usernames)