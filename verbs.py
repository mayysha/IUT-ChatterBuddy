import csv


def create_dictionary():
    f = open('verbs-in-english.csv', 'r')
    reader = csv.reader(f)

    keywords = {}
    for row in reader:
        keywords[row[0]] = [row[0], row[1], row[2], row[3], row[4]]

    return keywords
