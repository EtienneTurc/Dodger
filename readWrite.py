import csv


def readCsv():
    with open('people.csv', 'r') as readFile:
        spamreader = csv.reader(readFile, delimiter=',')
        for row in spamreader:
            return(row)
    readFile.close()


def writeInCsv():
    with open('people.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        row = ['Simon', 'Score']
        writer.writerow(row)
    writeFile.close()


writeInCsv()
readCsv()
