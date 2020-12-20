import csv

row = [2, 'marie', 'california']

with open('info.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row

with open('info.csv', 'w') as write_file:
    writer = csv.writer(write_file)
    writer.writerows(lines)

readFile.close()
write_file.close()